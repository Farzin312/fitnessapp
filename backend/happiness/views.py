from rest_framework import viewsets
from .models import UserHappinessLog
from .serializers import UserHappinessLogSerializer

class UserHappinessLogViewSet(viewsets.ModelViewSet):
    queryset = UserHappinessLog.objects.all()
    serializer_class = UserHappinessLogSerializer
