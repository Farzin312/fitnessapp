from rest_framework import serializers
from .models import UserSleep

class UserSleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSleep
        fields = ['id', 'user', 'date','sleep_minutes']