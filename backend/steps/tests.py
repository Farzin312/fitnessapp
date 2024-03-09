from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserSteps
from datetime import date

class UserStepsTests(TestCase):

    def test_user_steps_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        steps_log = UserSteps.objects.create(
            user=user,
            date=date.today(),
            steps=480
        )
        self.assertEqual(steps_log.steps, 480)
        self.assertEqual(steps_log.user.username, 'testuser')


