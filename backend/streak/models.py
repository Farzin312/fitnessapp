from django.db import models
from django.conf import settings

class Streak(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    super_streak = models.PositiveIntegerField(default=0)
    casual_streak = models.PositiveIntegerField(default=0)
    last_update_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - All Trackers: {self.super_streak}, Casual: {self.casual_streak}"

class StreakRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    streak_type = models.CharField(max_length=20, choices=[('all', 'Super Trackers'), ('casual', 'Casual')])
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date', '-end_date']
    def __str__(self):
        return f"{self.user.username} - {self.streak_type} Streak: {self.start_date} to {self.end_date}"