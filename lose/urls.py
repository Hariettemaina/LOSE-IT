from django.contrib import admin
from django.urls import path,include
from .views import *




urlpatterns = [
    path('',HomepageView, name = 'home'),
    path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
    path('register/',RegisterPage,name='register'),
]