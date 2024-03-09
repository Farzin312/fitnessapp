from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import UserHappinessLog
from .serializers import UserHappinessLogSerializer

class UserHappinessLogViewSet(viewsets.ModelViewSet):
    queryset = UserHappinessLog.objects.all()
    serializer_class = UserHappinessLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
