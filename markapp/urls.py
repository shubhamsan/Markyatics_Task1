from django.contrib import admin
from django.urls import path
from markapp import views
from django.conf.urls import include, url



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('userpage/', views.userpage, name='userpage')
]