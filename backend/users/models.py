from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    secret_question = models.CharField(max_length=200)
    secret_answer = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    age = models.PositiveIntegerField()
    def __str__(self):
        return self.user.username
