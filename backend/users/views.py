from django.utils import timezone
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, CustomUser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, UserProfileSerializer, PasswordResetSerializer, PasswordResetRequestSerializer
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, HttpResponse


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['create', 'password_reset_request', 'password_reset_confirm']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_data = request.data.pop('user', None)
        user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

        for attr, value in request.data.items():
            setattr(instance, attr, value)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

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

@api_view(['POST'])
def password_reset_request(request):
    serializer = PasswordResetRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = CustomUser.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            reset_url = request.build_absolute_uri(reverse('password_reset_confirm', args=[user.pk, token]))
            send_mail(
                'Password Reset Request',
                f'Please follow this link to reset your password: {reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def password_reset_confirm(request, user_id, token):
    if request.method == 'GET':
        try:
            user = CustomUser.objects.get(pk=user_id)
            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)
            return render(request, 'confirm_reset_password.html', {'user_id': user_id, 'token': token})
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid user.'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        try:
            user = CustomUser.objects.get(pk=user_id)
            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = PasswordResetSerializer(data=request.data, context={'user': user})
            if serializer.is_valid():
                serializer.save()
                return HttpResponse('<h1>Password Reset Successful</h1>', content_type='text/html')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid user.'}, status=status.HTTP_404_NOT_FOUND)


 

    


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = UserModel.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        login_input = request.data.get('login_input')
        password = request.data.get('password')
        user = EmailOrUsernameModelBackend().authenticate(request, username=login_input, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

