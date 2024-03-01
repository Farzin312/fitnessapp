from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    serving_size = models.DecimalField(max_digits=5, decimal_places=2, help_text="Serving size in grams")

    def __str__(self):
        return self.name

class DietLogEntry(models.Model):
    date = models.DateField()
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    servings_consumed = models.DecimalField(max_digits=5, decimal_places=2, help_text="Amount consumed in servings")

    def __str__(self):
        return f"{self.food_item.name} on {self.date}"

class DietLog(models.Model):
    date = models.DateField(unique=True)
    entries = models.ManyToManyField(DietLogEntry)

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

    def __str__(self):
        return f"Diet Log for {self.date}"
