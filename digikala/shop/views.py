from django.shortcuts import render , HttpResponse ,redirect
from .models import *   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserRegisterForm , AcountForm
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
def PQ(request , pk ):
    # COULD USE GETMETHOD TO
    start = (pk-1)*8
    end = start+8
    detail_records =  AggrQ.objects.all()[start:end]
    return render(request , 'qp.html' , {'detail_records' : detail_records} )
                          
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
def UserAccount(request ):
    if request.method == 'POST':
        form = AcountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AcountForm()
    return render(request , 'account_form.html' , {'form':form})


def UserScore(request ):
    if request.method == 'POST':
        form = AcountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AcountForm()
    return render(request , 'account_form.html' , {'form':form})