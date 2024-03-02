from datetime import timedelta
from django.utils import timezone
from .models import Streak, StreakRecord

def update_streaks(user):
    streak, _ = Streak.objects.get_or_create(user=user)
    
    if streak.last_update_date == timezone.localdate() - timedelta(days=1):
        streak.super_streak += 1
        streak.casual_streak += 1
    elif streak.last_update_date < timezone.localdate() - timedelta(days=1):
        end_streak_record(user, 'super', streak.last_update_date)
        end_streak_record(user, 'casual', streak.last_update_date)
        streak.super_streak = 1
        streak.casual_streak = 1
        start_streak_record(user, 'super', timezone.localdate())
        start_streak_record(user, 'casual', timezone.localdate())

    streak.last_update_date = timezone.localdate()
    streak.save()

def start_streak_record(user, streak_type, start_date):
    StreakRecord.objects.create(
        user=user,
        streak_type=streak_type,
        start_date=start_date
    )

def end_streak_record(user, streak_type, end_date):
    streak_record = StreakRecord.objects.filter(
        user=user,
        streak_type=streak_type,
        end_date__isnull=True
    ).last()
    if streak_record:
        streak_record.end_date = end_date
        streak_record.save()
