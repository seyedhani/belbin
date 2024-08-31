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
            score_form = form.save(commit=False)
            score_form.user = request.user
            score_form.main_q = main
            score_form.part_q = detail_records
            score_form.save()
        return redirect('home')
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
