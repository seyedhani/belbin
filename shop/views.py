from django.shortcuts import render , HttpResponse ,redirect
from .models import *   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
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
    start = (pk-1)*8
    end = start+8
    detail_records =  AggrQ.objects.all()[start:end]
    return render(request , 'qp.html' , {'detail_records' : detail_records} )
                          
def signupUser(request ):
    
    return render(request , 'signup.html'  )
                          