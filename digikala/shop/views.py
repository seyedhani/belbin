from django.shortcuts import render , HttpResponse ,redirect , get_list_or_404
from .models import *   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserRegisterForm , ScoreFormForm
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
def MQ(request ):
    records =  MainQ.objects.all( )                           
    return render(request , 'ques.html' , {'records' : records} )
def fpq(request , pk ):
    start = (pk-1) *8
    end =start+8
    records =  AggrQ.objects.all( )[start:end]                              
    return render(request , 'new.html' , {'records' : records} )
def PQ(request , pk , sec):
    main = MainQ.objects.get(id = pk)
    detail_records =  AggrQ.objects.get(id= sec)
    if request.method == "POST":
        form = ScoreFormForm(request.POST)
        if form.is_valid():
            same = ScoreForm.objects.filter(main_q = main ,part_q = detail_records ,  user =request.user ).first()      
            if same :
                score_form = same
                score_form.Score= form.cleaned_data.get('Score')
            else :  
                score_form = form.save(commit=False)
                score_form.user = request.user
                score_form.main_q = main
                score_form.part_q = detail_records
            score_form.save()
            
            records =  AggrQ.objects.all( )[sec::]   
            if sec % 8 == 0:
                q = 0
                start = sec - 7
                end = sec +1 
                all_scored = True  # فرض بر این است که همه امتیاز داده شده‌اند
                all = [ ]
                for i in range(start, end):
                    try:
                        pq = AggrQ.objects.get(id=i)
                    except AggrQ.DoesNotExist:
                        continue  # اگر سوالی وجود نداشته باشد، ادامه می‌دهیم
                    new = ScoreForm.objects.filter(main_q=main, part_q=pq, user=request.user).first()
                    if new:
                        all.append(new.Score )
                    else:
                        all_scored = False  # اگر به یکی از سوالات امتیاز داده نشده باشد، flag را False می‌کنیم
                if all_scored:
                    print("All questions in the range have been scored.")
                    res = sum(all)
                    if res > 10 :
                        m = "قبل از ادامخ کلیک کنید و برخی پاسخ هارا ویرایش کنید تا امتیاز زیر ده باشد"
                        messages.success(request, m , 'success')   
                    
                else:   
                    print("Not all questions in the range have been scored.")
                    
                 
        return render(request , 'new.html' , {'records' : records} )
    else:
        form = ScoreFormForm()
    return render(request , 'qp.html' ,{'form' :form  })

        
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
