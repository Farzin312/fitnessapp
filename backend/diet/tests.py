from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserFoodItem, UserDietLogEntry, UserDietLog

class DietTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.food_item = UserFoodItem.objects.create(
            user=self.user,
            name='Apple',
            calories=95,
            fat=0.3,
            carbs=25,
            protein=0.5,
            serving_size=100
        )
        self.diet_log_entry = UserDietLogEntry.objects.create(
            user=self.user,
            date='2024-03-10',
            food_item=self.food_item,
            servings_consumed=1
        )
        self.diet_log = UserDietLog.objects.create(user=self.user, date='2024-03-10')
        self.diet_log.entries.add(self.diet_log_entry)

    def test_food_item_creation(self):
        self.assertEqual(self.food_item.name, 'Apple')
        self.assertEqual(self.food_item.user, self.user)

    def test_diet_log_entry_creation(self):
        self.assertEqual(self.diet_log_entry.food_item, self.food_item)
        self.assertEqual(self.diet_log_entry.user, self.user)

    def test_diet_log_creation(self):
        self.assertEqual(self.diet_log.user, self.user)
        self.assertEqual(self.diet_log.entries.count(), 1)
