from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import UserSteps 
from .serializers import UserStepsSerializer

class UserStepsViewSet(viewsets.ModelViewSet):
    queryset = UserSteps.objects.all()
    serializer_class = UserStepsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

