from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_verification_code = models.CharField(max_length=6, blank=True, null=True)
    phone_verification_expires = models.DateTimeField(blank=True, null=True)
    email_verification_code = models.CharField(max_length=6, blank=True, null=True)
    email_verification_expires = models.DateTimeField(blank=True, null=True)

    def generate_phone_verification_code(self):
        self.phone_verification_code = str(uuid.uuid4())[:6]
        self.phone_verification_expires = timezone.now() + timedelta(minutes=10)
        self.save()

    def generate_email_verification_code(self):
        self.email_verification_code = str(uuid.uuid4())[:6]
        self.email_verification_expires = timezone.now() + timedelta(minutes=10)
        self.save()

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    secret_question = models.CharField(max_length=200)
    secret_answer = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
