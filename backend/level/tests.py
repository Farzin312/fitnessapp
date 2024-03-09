from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserLevel
from .views import add_experience, next_level_exp

class LevelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_add_experience(self):
        add_experience(self.user, 500)
        user_level = UserLevel.objects.get(user=self.user)
        self.assertEqual(user_level.experience_points, 500)

        add_experience(self.user, 600)
        user_level.refresh_from_db()
        self.assertEqual(user_level.level, 1)
        self.assertEqual(user_level.experience_points, 100)

    def test_next_level_exp(self):
        self.assertEqual(next_level_exp(0), 1000)
        self.assertEqual(next_level_exp(1), 1200)
