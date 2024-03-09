from django.test import TestCase
from .models import UserHappinessLog
from django.contrib.auth.models import User
from datetime import date

class UserHappinessLogTests(TestCase):

    def test_happiness_log_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        happiness_log = UserHappinessLog.objects.create(
            user=user,
            date=date.today(),
            happiness_score=80
        )
        self.assertEqual(happiness_log.happiness_score, 80)
        self.assertEqual(happiness_log.user.username, 'testuser')

