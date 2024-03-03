from rest_framework import serializers
from .models import UserLevel, UserRecord

class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = ['id', 'user', 'experience_points', 'level']

class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecord
        fields = ['id', 'user', 'experience_points', 'date']
