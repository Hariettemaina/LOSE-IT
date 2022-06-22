from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from datetime import datetime
from .filters import FoodFilter





# Create your views here.



@login_required(login_url='login')
def HomepageView(request):
    calories = Profile.objects.filter(person_of=request.user).last()
    calorie_goal = calories.calorie_goal
    
    
    if date.today() > calories.date:
        profile=Profile.objects.create(person_of=request.user).last()
        profile.save()
    

    calories = Profile.objects.filter(person_of=request.user).last()
		
        
    all_food_today=PostFood.objects.Filter(profile=calories)
    
    calorie_goal_status = calorie_goal -calories.total_calorie
    over_calorie = 0
    if calorie_goal_status < 0 :
        over_calorie = abs(calorie_goal_status)

    context = {
	'total_calorie':calories.total_calorie,
	'calorie_goal':calorie_goal,
	'calorie_goal_status':calorie_goal_status,
	'over_calorie' : over_calorie,
	'food_selected_today':all_food_today
	}
	   
    
    
    
