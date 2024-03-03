from rest_framework import serializers
from .models import UserStreak, UserStreakRecord

class UserStreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStreak
        fields = [
            'id',
            'user',
            'super_streak',
            'casual_streak',
            'last_update_date',
            'highest_super_streaks',
            'highest_casual_streaks',
        ]

class UserStreakRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStreakRecord
        fields = [
            'id',
            'user',
           'streak_type',
           'start_date',
           'end_date'
        ]