from django.urls import path 
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('ques/', views.MQ, name='ques'),
    path('qp/<int:pk>/', views.PQ, name='qp'),
    path('signup', views.signupUser, name='signup'),
]

