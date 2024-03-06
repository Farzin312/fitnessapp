from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class UserFoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    serving_size = models.DecimalField(max_digits=5, decimal_places=2, help_text="Serving size in grams", null=True, blank=True) 

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class UserDietLogEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    food_item = models.ForeignKey(UserFoodItem, on_delete=models.CASCADE)
    servings_consumed = models.DecimalField(max_digits=5, decimal_places=2, help_text="Amount consumed in servings")
    satisfaction_level = models.IntegerField(default=0, help_text="Satisfaction level on a scale of 1-10")

    def clean(self):
        if self.food_item.user and self.food_item.user != self.user:
            raise ValidationError('The FoodItem must belong to the same user as the DietLogEntry.')

    def __str__(self):
        return f"{self.food_item.name} on {self.date} for {self.user.username}"

class UserDietLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    entries = models.ManyToManyField(UserDietLogEntry)
    daily_satisfaction = models.IntegerField(default=0, help_text="Overall daily satisfaction level on a scale of 1-10")

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
