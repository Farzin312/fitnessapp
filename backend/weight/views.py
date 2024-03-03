from rest_framework import viewsets
from .models import UserWeight
from .serializers import UserWeightSerializer

class UserWeightViewSet(viewsets.ModelViewSet):
    queryset = UserWeight.objects.all()
    serializer_class = UserWeightSerializer
