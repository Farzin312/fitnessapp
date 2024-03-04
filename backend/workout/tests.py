from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import UserBodyPart, UserWorkout
from datetime import date

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.body_part = UserBodyPart.objects.create(name='Chest')
        self.workout = UserWorkout.objects.create(
            user=self.user,
            date=date.today(),
            exercise_name='Bench Press',
            sets=4,
            reps=10,
            rpe=8.5,
            percentage_of_max=75,
            primary_target=self.body_part
        )

    def test_weekly_sets(self):
        response = self.client.get('/workouts/userworkout/weekly_sets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total_sets'], 4)
