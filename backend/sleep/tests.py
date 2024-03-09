from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserSleep
from datetime import date

class UserSleepTests(TestCase):

    def test_user_sleep_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        sleep_log = UserSleep.objects.create(
            user=user,
            date=date.today(),
            sleep_minutes=480  
        )
        self.assertEqual(sleep_log.sleep_minutes, 480)
        self.assertEqual(sleep_log.user.username, 'testuser')
