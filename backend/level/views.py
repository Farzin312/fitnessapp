from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserLevel, UserRecord
from .serializers import UserLevelSerializer, UserRecordSerializer

def add_experience(user, exp):
    user_level, _ = UserLevel.objects.get_or_create(user=user)
    user_level.experience_points += exp
    while user_level.experience_points >= next_level_exp(user_level.level):
        user_level.level += 1
        user_level.experience_points = 0  
    user_level.save()
    UserRecord.objects.create(user=user, experience_points=exp, date=timezone.now())

def next_level_exp(level):
    base_exp = 1000
    growth_rate = 1.2
    return int(base_exp * (growth_rate ** level))

def get_ranking():
    return UserLevel.objects.all().order_by('-level', '-experience_points')

class UserLevelViewSet(viewsets.ModelViewSet):
    queryset = UserLevel.objects.all()
    serializer_class = UserLevelSerializer

    @action(detail=False, methods=['get'])
    def top_players(self, request):
        top_players = get_ranking()[:100]  
        serializer = self.get_serializer(top_players, many=True)
        return Response(serializer.data)

class UserRecordViewSet(viewsets.ModelViewSet):
    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer
