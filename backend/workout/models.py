from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class UserBodyPart(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class UserWorkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    exercise_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    reps = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    primary_target = models.ForeignKey(UserBodyPart, related_name='primary_workouts', on_delete=models.SET_NULL, null=True)
    secondary_targets = models.ManyToManyField(UserBodyPart, related_name='secondary_workouts', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}: {self.exercise_name}"
