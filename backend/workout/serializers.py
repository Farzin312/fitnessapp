from rest_framework import serializers
from .models import UserBodyPart, UserExercise, UserWorkout, UserTargetSets

class UserBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBodyPart
        fields = ['id', 'name']

class UserExerciseSerializer(serializers.ModelSerializer):
    primary_target = UserBodyPartSerializer(read_only=True)
    secondary_targets = UserBodyPartSerializer(many=True, read_only=True)

    class Meta:
        model = UserExercise
        fields = ['id', 'name', 'primary_target', 'secondary_targets', 'is_user_added']

class UserWorkoutSerializer(serializers.ModelSerializer):
    exercise = UserExerciseSerializer(read_only=True)

    class Meta:
        model = UserWorkout
        fields = ['id', 'date', 'exercise', 'sets', 'reps', 'rpe', 'percentage_of_max']

class UserTargetSetsSerializer(serializers.ModelSerializer):
    body_part = UserBodyPartSerializer(read_only=True)

    class Meta:
        model = UserTargetSets
        fields = ['id', 'date', 'body_part_name', 'total_primary_sets', 'total_secondary_sets']

