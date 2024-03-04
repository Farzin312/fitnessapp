from rest_framework import viewsets, permissions
from .models import UserBodyPart, UserWorkout
from .serializers import UserBodyPartSerializer, UserWorkoutSerializer
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta

class UserBodyPartViewSet(viewsets.ModelViewSet):
    queryset = UserBodyPart.objects.all()
    serializer_class = UserBodyPartSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserWorkoutViewSet(viewsets.ModelViewSet):
    queryset = UserWorkout.objects.all()
    serializer_class = UserWorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

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
