from django.shortcuts import render
from django.utils import timezone
from .models import UserLevel, Record

def add_experience(user, exp):
    user_level, _ = UserLevel.objects.get_or_create(user=user)
    user_level.experience_points += exp
    while user_level.experience_points >= next_level_exp(user_level.level):
        user_level.level += 1
        user_level.experience_points = 0  
    user_level.save()
    Record.objects.create(user=user, experience_points=exp, date=timezone.now())

def next_level_exp(level):
    base_exp = 1000
    growth_rate = 1.2
    return int(base_exp * (growth_rate ** level))

def get_ranking():
    ranking = UserLevel.objects.all().order_by('-level', '-experience_points')
    return ranking
