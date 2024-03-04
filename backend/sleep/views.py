from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import UserSleep
from .serializers import UserSleepSerializer

class UserSleepViewSet(viewsets.ModelViewSet):
    queryset = UserSleep.objects.all()
    serializer_class = UserSleepSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
