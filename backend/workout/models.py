from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class UserBodyPart(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class UserExercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    primary_target = models.ForeignKey(UserBodyPart, related_name='primary_target', on_delete=models.SET_NULL, null=True)
    secondary_targets = models.ManyToManyField(UserBodyPart, related_name='secondary_targets', blank=True)
    is_user_added = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class UserWorkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    exercise = models.ForeignKey(UserExercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    reps = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    rpe = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    one_rep_max = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    one_set_max_reps = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    percentage_of_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}: {self.exercise.name}"
