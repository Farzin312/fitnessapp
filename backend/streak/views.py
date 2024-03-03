from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserStreak, UserStreakRecord
from .serializers import UserStreakSerializer, UserStreakRecordSerializer

def update_streaks(user):
    streak, _ = UserStreak.objects.get_or_create(user=user)
    
    if streak.last_update_date == timezone.localtime().date() - timedelta(days=1):
        streak.super_streak += 1
        streak.casual_streak += 1
        streak.highest_super_streaks = max(streak.highest_super_streaks, streak.super_streak)  
        streak.highest_casual_streaks = max(streak.highest_casual_streaks, streak.casual_streak)  
    elif streak.last_update_date < timezone.localtime().date() - timedelta(days=1):
        end_streak_record(user, 'super', streak.last_update_date)
        end_streak_record(user, 'casual', streak.last_update_date)
        streak.super_streak = 1
        streak.casual_streak = 1
        start_streak_record(user, 'super', timezone.localtime().date())
        start_streak_record(user, 'casual', timezone.localtime().date())

    streak.last_update_date = timezone.localtime().date()
    streak.save()
def start_streak_record(user, streak_type, start_date):
    UserStreakRecord.objects.create(
        user=user,
        streak_type=streak_type,
        start_date=start_date
    )

def end_streak_record(user, streak_type, end_date):
    streak_record = UserStreakRecord.objects.filter(
        user=user,
        streak_type=streak_type,
        end_date__isnull=True
    ).last()
    if streak_record:
        streak_record.end_date = end_date
        streak_record.save()

def get_highest_streak_records():
    return UserStreak.objects.all().order_by('-highest_super_streaks', '-highest_casual_streaks')

class UserStreakViewSet(viewsets.ModelViewSet):
    queryset = UserStreak.objects.all()
    serializer_class = UserStreakSerializer

    def list(self, request, *args, **kwargs):
        queryset = get_highest_streak_records()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UserStreakRecordViewSet(viewsets.ModelViewSet):
    queryset = UserStreakRecord.objects.all()
    serializer_class = UserStreakRecordSerializer
