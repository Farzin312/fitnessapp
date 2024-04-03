from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from .models import UserBodyPart, UserExercise, UserWorkout, UserTargetSets
from .serializers import UserBodyPartSerializer, UserExerciseSerializer, UserWorkoutSerializer, UserTargetSetsSerializer
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

class UserTargetSetsViewSet(viewsets.ModelViewSet):
    queryset = UserTargetSets.objects.all()
    serializer_class = UserTargetSetsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def total_sets_by_date_range(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({'error': 'Start date and end date are required.'}, status=status.HTTP_400_BAD_REQUEST)

        primary_sets = self.get_queryset().filter(date__range=[start_date, end_date]).values('body_part__name').annotate(total_primary_sets=Sum('total_primary_sets')).order_by('body_part__name')
        secondary_sets = self.get_queryset().filter(date__range=[start_date, end_date]).values('body_part__name').annotate(total_secondary_sets=Sum('total_secondary_sets')).order_by('body_part__name')

        return Response({
            'start_date': start_date,
            'end_date': end_date,
            'primary_sets': primary_sets,
            'secondary_sets': secondary_sets
        })