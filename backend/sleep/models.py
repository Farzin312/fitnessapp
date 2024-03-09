from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class UserSleep(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    sleep_minutes = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(1440)
    ]
    )

    class Meta:
        ordering = ['-date']
    def __str__(self):
        hours, minutes = divmod(self.sleep_minutes, 60)
        return f"{self.user.username} - {self.date}: Sleep {hours}h {minutes}m"
