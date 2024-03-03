from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserStreak
from .views import update_streaks, get_highest_streak_records

class StreakTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_update_streaks(self):
        update_streaks(self.user1)
        streak = UserStreak.objects.get(user=self.user1)
        self.assertEqual(streak.super_streak, 1)
        self.assertEqual(streak.casual_streak, 1)

        update_streaks(self.user2)
        streak = UserStreak.objects.get(user=self.user2)
        self.assertEqual(streak.super_streak, 1)
        self.assertEqual(streak.casual_streak, 1)

    def test_get_highest_streak_records(self):
        update_streaks(self.user1)
        update_streaks(self.user2)
        highest_streaks = get_highest_streak_records()
        self.assertEqual(highest_streaks.count(), 2)
        self.assertEqual(highest_streaks.first().user.username, 'user1')
