from django.contrib import admin
from django.urls import path,include
from .views import *




urlpatterns = [
    path('',HomepageView, name = 'home'),
    path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
    path('register/',RegisterPage,name='register'),
    path('add_food/',add_food,name='add_food'),
    path('select_food/',select_food,name='select_food'),
    path('update_food/<str:pk>/',update_food,name='update_food'),
    path('delete_food/<str:pk>/',delete_food,name='delete_food'),
    path('profile/',ProfilePage,name='profile'),
]