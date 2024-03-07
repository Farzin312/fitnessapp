from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from .models import UserBodyPart, UserExercise, UserWorkout
from .serializers import UserBodyPartSerializer, UserExerciseSerializer, UserWorkoutSerializer
from django.db.models import Sum, Q
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta

class UserBodyPartViewSet(viewsets.ModelViewSet):
    queryset = UserBodyPart.objects.all()
    serializer_class = UserBodyPartSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class UserExerciseViewSet(viewsets.ModelViewSet):
    queryset = UserExercise.objects.all()
    serializer_class = UserExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(Q(user=user) | Q(is_user_added=False))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_user_added=True)

class UserWorkoutViewSet(viewsets.ModelViewSet):
    queryset = UserWorkout.objects.all()
    serializer_class = UserWorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_user_created:
            return Response({'detail': 'Cannot delete a pre-existing workout.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def weekly_sets(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date:
            start_date = datetime.now().date() - timedelta(days=datetime.now().weekday())
        if not end_date:
            end_date = start_date + timedelta(days=6)

        workouts = self.get_queryset().filter(date__range=[start_date, end_date])
        total_sets = workouts.aggregate(Sum('sets'))['sets__sum'] or 0

        return Response({'total_sets': total_sets, 'start_date': start_date, 'end_date': end_date})
