from rest_framework import viewsets
from .models import UserSteps 
from .serializers import UserStepsSerializer

class UserStepsViewSet(viewsets.ModelViewSet):
    queryset = UserSteps.objects.all()
    serializer_class = UserStepsSerializer

