from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user_profile = UserProfile.objects.create(user=user, **request.data)
            serializer = self.get_serializer(user_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_data = request.data.pop('user')
        user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

        for attr, value in request.data.items():
            setattr(instance, attr, value)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def send_phone_verification(self, request, pk=None):
        user_profile = self.get_object()
        user_profile.user.generate_phone_verification_code()
        return Response({'message': 'Verification code sent'})

    @action(detail=True, methods=['post'])
    def verify_phone(self, request, pk=None):
        user_profile = self.get_object()
        code = request.data.get('code')
        if user_profile.user.phone_verification_code == code and timezone.now() < user_profile.user.phone_verification_expires:
            user_profile.user.is_phone_verified = True
            user_profile.user.save()
            return Response({'message': 'Phone number verified'})
        return Response({'message': 'Invalid or expired code'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def change_email(self, request, pk=None):
        user_profile = self.get_object()
        if not user_profile.user.is_phone_verified:
            return Response({'message': 'Phone number not verified'}, status=status.HTTP_400_BAD_REQUEST)
        new_email = request.data.get('new_email')
        user_profile.user.email = new_email
        user_profile.user.save()
        return Response({'message': 'Email updated'})

    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated])
    def delete_account(self, request, pk=None):
        user_profile = self.get_object()
        if not (user_profile.user.is_email_verified or user_profile.user.is_phone_verified):
            return Response({'message': 'Email or phone number not verified'}, status=status.HTTP_400_BAD_REQUEST)
        user_profile.user.delete()
        return Response({'message': 'Account deleted'}, status=status.HTTP_204_NO_CONTENT)
