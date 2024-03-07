from rest_framework import serializers
from .models import UserFoodItem, UserDietLogEntry, UserDietLog

class UserFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodItem
        fields = ['id', 'name', 'calories', 'fat', 'carbs', 'protein', 'serving_size', 'is_user_added']

class UserDietLogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDietLogEntry
        fields = ['id', 'date', 'food_item', 'servings_consumed']

class UserDietLogSerializer(serializers.ModelSerializer):
    entries = UserDietLogEntrySerializer(many=True, read_only=True)

    class Meta:
        model = UserDietLog
        fields = ['id', 'date', 'entries', 'total_calories', 'total_fat', 'total_carbs', 'total_protein']


