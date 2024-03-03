from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings

class UserHappinessLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    happiness_score = models.IntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    notes =models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}: Score {self.happiness_score}"