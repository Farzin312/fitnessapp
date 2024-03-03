from rest_framework import serializers
from .models import UserHappinessLog

class UserHappinessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHappinessLog
        fields = ['id', 'user', 'date', 'happiness_score', 'notes']
