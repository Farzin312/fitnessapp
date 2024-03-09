from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserWeight
from datetime import date

class UserWeightTests(TestCase):

    def test_user_weight_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        weight_log = UserWeight.objects.create(
            user=user,
            date=date.today(),
            user_weight=480
        )
        self.assertEqual(weight_log.user_weight, 480)
        self.assertEqual(weight_log.user.username, 'testuser')
