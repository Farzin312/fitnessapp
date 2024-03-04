from rest_framework import serializers
from .models import UserBodyPart, UserWorkout

class UserBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBodyPart
        fields = ['id', 'name']

class UserWorkoutSerializer(serializers.ModelSerializer):
    primary_target = UserBodyPartSerializer(read_only=True)
    secondary_targets = UserBodyPartSerializer(many=True, read_only=True)

    class Meta:
        model = UserWorkout
        fields = ['id', 'user', 'date', 'exercise_name', 'sets', 'reps', 'rpe', 'percentage_of_max', 'primary_target', 'secondary_targets']
