from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile_data = {
                'secret_question': request.data.get('secret_question'),
                'secret_answer': request.data.get('secret_answer'),
                'sex': request.data.get('sex'),
                'date_of_birth': request.data.get('date_of_birth'),
            }
            profile_serializer = UserProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save(user=user)
                return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
            else:
                user.delete() 
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)