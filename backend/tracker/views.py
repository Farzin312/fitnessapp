from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from users.serializers import UserSerializer, UserProfileSerializer
from happiness.serializers import UserHappinessLogSerializer
from diet.serializers import UserFoodItemSerializer, UserDietLogEntrySerializer, UserDietLogSerializer
from level.serializers import UserLevelSerializer, UserRecordSerializer
from sleep.serializers import UserSleepSerializer
from steps.serializers import UserStepsSerializer
from streak.serializers import UserStreakSerializer, UserStreakRecordSerializer
from weight.serializers import UserWeightSerializer
from workout.serializers import UserWorkoutSerializer, UserExerciseSerializer, UserTargetSetsSerializer


class UserAggregateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = UserSerializer(user).data
        profile_data = UserProfileSerializer(user.profile).data if hasattr(user, 'profile') else {}
        happiness_data= UserHappinessLogSerializer(user.userhappinesslog_set.all(), many=True).data
        food_item_data = UserFoodItemSerializer(user.userfooditem_set.all(), many=True).data
        diet_log_data = UserDietLogSerializer(user.userdietlog_set.all(), many=True).data
        diet_log_entry_data = UserDietLogEntrySerializer(user.userdietlogentry_set.all(), many=True).data
        try:
            level_data = UserLevelSerializer(user.userlevel).data
        except ObjectDoesNotExist:
            level_data = None
        record_data = UserRecordSerializer(user.userrecord_set.all(), many=True).data
        sleep_data = UserSleepSerializer(user.usersleep_set.all(), many=True).data
        steps_data = UserStepsSerializer(user.usersteps_set.all(), many=True).data
        try:
            streak_data = UserStreakSerializer(user.userstreak).data
        except ObjectDoesNotExist:
            streak_data = None
        streak_record_data = UserStreakRecordSerializer(user.userstreakrecord_set.all(), many=True).data
        weight_data = UserWeightSerializer(user.userweight_set.all(), many=True).data
        workout_data = UserWorkoutSerializer(user.userworkout_set.all(), many=True).data
        exercise_data = UserExerciseSerializer(user.userexercise_set.all(), many=True).data
        target_sets_data = UserTargetSetsSerializer(user.usertargetsets_set.all(), many=True).data
        
        return Response({
            'user': user_data,
            'profile': profile_data,
            'happiness_data': happiness_data,
            'food_item_data': food_item_data,
            'diet_log_data': diet_log_data,
            'diet_log_entry_data': diet_log_entry_data,
            'level_data': level_data,
            'record_data': record_data,
            'sleep_data': sleep_data,
            'steps_data': steps_data,
            'streak_data': streak_data,
            'streak_record_data': streak_record_data,
            'weight_data': weight_data,
            'workout_data': workout_data,
            'exercise_data': exercise_data,
            'target_sets_data': target_sets_data
        })

