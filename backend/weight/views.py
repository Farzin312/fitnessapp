from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import UserWeight
from .serializers import UserWeightSerializer

class UserWeightViewSet(viewsets.ModelViewSet):
    queryset = UserWeight.objects.all()
    serializer_class = UserWeightSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
