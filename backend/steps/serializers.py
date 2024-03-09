from rest_framework import serializers
from .models import UserSteps

class UserStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSteps
        fields = ['id', 'user', 'date','steps']