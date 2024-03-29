from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from users.serializers import PasswordResetSerializer, PasswordResetRequestSerializer

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
            return render(request, 'auth/confirm_reset_password.html', {'user_id': user_id, 'token': token})
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

