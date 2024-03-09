from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class UserSteps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    date = models.DateField()
    user_steps = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f"{self.user.username} - {self.date}: {self.user_steps} steps"