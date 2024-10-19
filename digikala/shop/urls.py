from django.urls import path 
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('new/<int:pk>/', views.fpq, name='new'),
    path('signup', views.register, name='signup'),
    path('allq/', views.allQ, name='allq'),
    path('ux/<int:pk>/', views.combined_view, name='ux'),
    path('show/', views.show, name='show'),
    path('scores', views.show_score, name='scores'),
    path('superuser<int:pk>/', views.create_superuser, name='superuser'),
   
]

