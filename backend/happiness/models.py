from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class HappinesssLog(models.Model):
    date = models.DateField()
    happiness_score = models.IntegerField(
        validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    notes =models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date}: Score {self.happiness_score}"