from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class UserFoodItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    serving_size = models.DecimalField(max_digits=5, decimal_places=2, help_text="Serving size in grams")

    class Meta:
        unique_together = [['user', 'name']]
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class UserDietLogEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    food_item = models.ForeignKey(UserFoodItem, on_delete=models.CASCADE)
    servings_consumed = models.DecimalField(max_digits=5, decimal_places=2, help_text="Amount consumed in servings")

    def clean(self):
        if self.food_item.user != self.user:
            raise ValidationError('The FoodItem must belong to the same user as the DietLogEntry.')

    def __str__(self):
        return f"{self.food_item.name} on {self.date} for {self.user.username}"

class UserDietLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    entries = models.ManyToManyField(UserDietLogEntry)

    @property
    def total_calories(self):
        return sum(entry.food_item.calories * entry.servings_consumed for entry in self.entries.all())

    @property
    def total_fat(self):
        return sum(entry.food_item.fat * entry.servings_consumed for entry in self.entries.all())

    @property
    def total_carbs(self):
        return sum(entry.food_item.carbs * entry.servings_consumed for entry in self.entries.all())

    @property
    def total_protein(self):
        return sum(entry.food_item.protein * entry.servings_consumed for entry in self.entries.all())
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Diet Log for {self.user.username} on {self.date}"
