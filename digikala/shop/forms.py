from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']
class ScoreFormForm(forms.ModelForm):
    class Meta:
        model = ScoreForm
        fields = ['Score']
       
class SuperUserForm(forms.ModelForm):

    class Meta:
        model = SuperUser
        fields = [ 'phone_numb' , 'gender']
        
        # You can customize widgets if necessary
