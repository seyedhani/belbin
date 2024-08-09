from django.urls import path
from . import views

urlpatterns = [
    path('ques/', views.members, name='members'),
]