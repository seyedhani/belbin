from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
class singupForms(UserCreationForm):
    name = forms.CharField(
        max_length=100 ,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name'}))
    
    email = forms.EmailInput(
        max_length=100 ,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    
    username = forms.CharField(
        max_length=100 ,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your username'}))
        
    pass1 = forms.EmailInput(
        max_length=100 ,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','name':'password','type':'password','placeholder':'your pass'}))
            
    pass2 = forms.EmailInput(
        max_length=100 ,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','name':'password','type':'password','placeholder':'enter again'}))
    class meta:
        model =User
        fields =('name','email','username' ,'pass1','pass2')
    
    