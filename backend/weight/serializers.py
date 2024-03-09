from rest_framework import serializers
from .models import UserWeight

class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = ['id', 'user', 'date', 'user_weight']
        