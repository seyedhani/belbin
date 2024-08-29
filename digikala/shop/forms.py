from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class us(forms.Form):
    score = forms.IntegerField(label="enter")
    class Meta:
        model = Account
        fields = ('score' , )