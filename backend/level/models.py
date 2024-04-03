from django.db import models
from django.conf import settings

class UserLevel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='userlevel', on_delete=models.CASCADE, null=True)
    experience_points = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile - Level: {self.level}, Exp: {self.experience_points}"

class UserRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    experience_points = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Record for {self.user.username} on {self.date}: {self.experience_points} exp"
