from rest_framework import viewsets
from .models import UserSleep
from .serializers import UserSleepSerializer

class UserSleepViewSet(viewsets.ModelViewSet):
    queryset = UserSleep.objects.all()
    serializer_class = UserSleepSerializer
