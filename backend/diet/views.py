from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import UserFoodItem, UserDietLogEntry, UserDietLog
from .serializers import UserFoodItemSerializer, UserDietLogEntrySerializer, UserDietLogSerializer

class UserFoodItemViewSet(viewsets.ModelViewSet):
    queryset = UserFoodItem.objects.all()
    serializer_class = UserFoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserDietLogEntryViewSet(viewsets.ModelViewSet):
    queryset = UserDietLogEntry.objects.all()
    serializer_class = UserDietLogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserDietLogViewSet(viewsets.ModelViewSet):
    queryset = UserDietLog.objects.all()
    serializer_class = UserDietLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
