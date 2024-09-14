from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from django.http import JsonResponse
from .models import *   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserRegisterForm , ScoreFormForm
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


        
def signupUser(request ):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            pass1 = form.cleaned_data['password1']
            user = authenticate(request ,username = username , password =pass1)
            login(request ,user)
            
            return redirect('home')
        else:
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})


def combined_view(request, pk):
    start = (pk - 1) * 8
    end = start + 8
    main = MainQ.objects.get(id=pk)
    records = AggrQ.objects.all()[start:end]

    if request.method == "POST":
        question_id = request.POST.get('question_id')
        question = get_object_or_404(AggrQ, id=question_id)

        score_form = ScoreForm.objects.filter(main_q=main, part_q=question, user=request.user).first()
        form = ScoreFormForm(request.POST)

        if form.is_valid():
            if score_form:
                score_form.Score = form.cleaned_data.get('Score')
                score_form.save()
            else:
                score_form = form.save(commit=False)
                score_form.user = request.user
                score_form.main_q = main
                score_form.part_q = question
                score_form.save()
            
            sec = int(question_id)
            if sec % 8 == 0:
                start = sec - 7
                end = sec + 1
                all_scored = True
                all = []
                for i in range(start, end):
                    try:
                        pq = AggrQ.objects.get(id=i)
                    except AggrQ.DoesNotExist:
                        continue
                    new = ScoreForm.objects.filter(main_q=main, part_q=pq, user=request.user).first()
                    if new:
                        all.append(new.Score)
                    else:
                        all_scored = False
                if all_scored:
                    res = sum(all)
                    if res > 10:
                        m = " برخی پاسخ هارا ویرایش کنید تا مجموع امتیاز زیر ده باشد"
                        return JsonResponse({'status': 'error', 'message': m})
                else:
                    m = ""
                    return JsonResponse({'status': 'warning', 'message': m})
            return JsonResponse({'status': 'success', 'message': 'ثبت شد'})
    
    form = ScoreFormForm()
    mq = MainQ.objects.all()
    return render(request, 'ux.html', {
        'records': records,
        'main':main,
        'form': form,
        'mq':mq,
    })


def allQ(request ):
    records =  MainQ.objects.all( )                           
    return render(request , 'mainques.html' , {'records' : records} )

def result(request , pk ):
    records =  Result.objects.get( id = pk )                           
    return render(request , 'result.html' , {'records' : records} )
def show(request ):
    scores = ScoreForm.objects.filter(user=request.user).order_by('main_q' , 'part_q')
    comp = True
    if len(scores) == 56:
        all_score = [ ]
        for i in range(7):
            start = (i) * 8
            end = start + 8
            small = [ ]
            for j in range(start , end):
                main_ind = (i+1)
                part_index = (j+1)
                main_question = get_object_or_404(MainQ, id=main_ind)
                part_question = get_object_or_404(AggrQ, id=part_index)
                point = ScoreForm.objects.filter(main_q=main_question, part_q=part_question, user=request.user).first()
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
        return render(request , 'user.html' , {'scores' : scores , 'comp':comp , 'all_score' : all_score, 'res_ind' : result_ind,})
    else:
        comp = False
        return render(request , 'user.html' , {'scores' : scores , 'comp':comp})
