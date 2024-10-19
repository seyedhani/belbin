from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import *   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserRegisterForm , ScoreFormForm ,SuperUserForm
from django.http import JsonResponse
def main(request):
    return render(request , 'index.html' )          
def about(request):
    return render(request , 'about.html')
def logoutuser(request):
    logout(request)
    messages.success(request,(" خارج شدین "))
    return redirect('home')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pasword = request.POST['password']
        user = authenticate(request ,username = username , password =pasword)
        if user is not None:
            login(request , user)
            
            return redirect('home')
        else:
            messages.success(request ,("اشتباهه"))
            return redirect('login')
    else:
        return render(request, 'login.html')

def fpq(request , pk ):
    start = (pk-1) *8
    end =start+8
    main = MainQ.objects.get(id =pk)
    records =  AggrQ.objects.all( )[start:end]                              
    return render(request , 'ques.html' , {'records' : records ,  'main':main} )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # هدایت به صفحه لاگین پس از ثبت‌نام موفق
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})




def combined_view(request, pk):
    start = (pk - 1) * 8
    end = start + 8
    main = get_object_or_404(MainQ, id=pk)
    records = AggrQ.objects.all()[start:end]

    if request.method == "POST":
        for record in records:
            question_id = record.id
            score = request.POST.get(f'rating_{question_id}')  # دریافت امتیاز

            if score:  # بررسی اینکه امتیاز وجود داشته باشد
                try:
                    score = int(score)
                except ValueError:
                    score = 0  # مقدار پیش‌فرض

                # چاپ کردن داده‌ها برای بررسی
                print(f"سوال {question_id}: امتیاز {score}")

                question = get_object_or_404(AggrQ, id=question_id)

                # بررسی وجود امتیاز قبلی
                score_form = ScoreForm.objects.filter(main_q=main, part_q=question, user=request.user).first()

                if score_form:
                    if score_form.Score != score:
                        score_form.Score = score
                        score_form.save()
                        messages.success(request, f"امتیاز برای سوال {question_id} به‌روزرسانی شد.")
                else:
                    score_form = ScoreForm(
                        user=request.user,
                        main_q=main,
                        part_q=question,
                        Score=score
                    )
                    score_form.save()
                    messages.success(request, f"امتیاز برای سوال {question_id} ثبت شد.")
            else:
                messages.info(request, f"سوال {question_id} بدون امتیاز بود و نادیده گرفته شد.")

    form = ScoreFormForm()  # فرم خالی برای GET
    mq = MainQ.objects.all()

    return render(request, 'ux.html', {
        'records': records,
        'main': main,
        'form': form,
        'mq': mq,
    })
def allQ(request ):
    records =  MainQ.objects.all( )         
    parts = ['اول',"دوم" ,"سوم","چهارم ","پنجم","ششم","هفتم"]                  
    return render(request , 'mainques.html' , {'records' : records , 'parts':parts} )


def show(request ):
    scores = ScoreForm.objects.filter(user=request.user).order_by('main_q' , 'part_q')
    comp = True
    if len(scores) == 56:
        next = [ ]
        for a in scores:
            s = a.Score
            next.append(s)
        awn = check(next)
        sh_change = True
        if len(awn)>=1:
            sh_change=False
            return render(request , 'user.html' , {'comp':comp , 'awn' : awn , 'sh_change':sh_change})
            
        all_score = [ ]
        m = [ ]
        for i in range(7):
            start = (i) * 8
            end = start + 8
            small = [ ]
            main_question = get_object_or_404(MainQ, id=i+1)
            mini = AggrQ.objects.all()
            for min in mini :
                m.append(min)
            for k in range (start , end ):
                pq = m[k]
                point = ScoreForm.objects.filter(main_q=main_question, part_q=pq, user=request.user).first()
                point_numb = point.Score
             
                small.append(point_numb)
            all_score.append(small)
     
        columns = [
        [all_score[0][6], all_score[1][0], all_score[2][7], all_score[3][3], all_score[4][1], all_score[5][5], all_score[6][4]],
        [all_score[0][3], all_score[1][1], all_score[2][0], all_score[3][7], all_score[4][5], all_score[5][2], all_score[6][6]],
        [all_score[0][5], all_score[1][4], all_score[2][2], all_score[3][1], all_score[4][3], all_score[5][6], all_score[6][0]],
        [all_score[0][2], all_score[1][6], all_score[2][3], all_score[3][4], all_score[4][7], all_score[5][0], all_score[6][5]],
        [all_score[0][0], all_score[1][2], all_score[2][5], all_score[3][6], all_score[4][4], all_score[5][7], all_score[6][3]],
        [all_score[0][7], all_score[1][3], all_score[2][6], all_score[3][2], all_score[4][0], all_score[5][4], all_score[6][1]],
        [all_score[0][1], all_score[1][5], all_score[2][4], all_score[3][0], all_score[4][2], all_score[5][1], all_score[6][7]],
        [all_score[0][4], all_score[1][7], all_score[2][1], all_score[3][5], all_score[4][6], all_score[5][3], all_score[6][2]]]
        res = [sum(column) for column in columns]
        max_res = max(res)
        result_ind = res.index(max_res) +1
        index_list = list(enumerate(res))
        sorted_ind_list = sorted(index_list, key= lambda x: x[1], reverse=True)
        sorted_ind = [x[0] for x in sorted_ind_list]
        print(res)
        print(sorted_ind)
        sss = sum(res)
        percent= sorted([(z/sss )*100 for z in res] , reverse=True)
        x = InTeam(sorted_ind)
       
        return render(request , 'user.html' , {'scores' : scores , 'comp':comp , 'all_score' : all_score, 'res_ind' : result_ind ,'x':x , 'sorted_ind':percent})
    else:
        comp = False
        return render(request , 'user.html' , {'scores' : scores , 'comp':comp} )
   
def show_score(request):
    scores = ScoreForm.objects.filter(user=request.user).order_by('main_q' , 'part_q')
    numbs = [i for i in range (1,8)]
    return render(request , 'scores.html' , {'scores' : scores  , 'numbs':numbs})
def check (scores):
    changes = [ ]
    alls=[]
    for i in range (7):
        start = i*8
        end = start+8
        parts = [ ]
        for j in range(start , end ):
            s = scores[j]
            parts.append(s)
        sa = sum(parts)
        alls.append(sa)
    for k in range (7):
        if alls[k] > 10:
            changes.append(k+1)
    return changes
def create_superuser(request,pk):
    records =  Result.objects.get( id = pk )
    ex = SuperUser.objects.filter(user_id=request.user).first()
    if ex == None:
        if request.method == 'POST':
            form = SuperUserForm(request.POST)
            if form.is_valid():
                superuser = form.save(commit=False)
                superuser.user_id = request.user
                superuser.date = timezone.now()
                superuser.result = records
                superuser.save()
                return render(request ,'results.html' ,{'records':records})
        else:
            form = SuperUserForm()
        return render(request, 'superuser.html', {'form': form})
    else :
        return render(request ,'results.html' ,{'records':records})
def InTeam( arr):
    r =[ ]
    for i in arr:
        re = Result.objects.get(id = i+1)
        r.append(re)
    print(r)
    return r