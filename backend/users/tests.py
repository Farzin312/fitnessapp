from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import UserProfile
from django.utils import timezone

User = get_user_model()

class UserProfileTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'user': {
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'testpassword123',
                'phone_number': '1234567890'
            },
            'secret_question': 'What is your pet\'s name?',
            'secret_answer': 'Fluffy',
            'sex': 'male',
            'age': 25
        }

    def test_create_user_profile(self):
        response = self.client.post('/api/userprofiles/', self.user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_update_user_profile(self):
        self.test_create_user_profile()
        user_profile = UserProfile.objects.first()
        update_data = {
            'user': {
                'username': 'updateduser',
                'email': 'updated@example.com',
                'password': 'updatedpassword123'
            },
            'secret_question': 'Updated question?',
            'secret_answer': 'Updated answer',
            'sex': 'female',
            'age': 30
        }
        response = self.client.put(f'/api/userprofiles/{user_profile.id}/', update_data, format='json')
        self.assertEqual(response.status_code, 200)
        user_profile.refresh_from_db()
        self.assertEqual(user_profile.user.username, 'updateduser')
        self.assertEqual(user_profile.sex, 'female')

    def test_send_phone_verification(self):
        self.test_create_user_profile()
        user_profile = UserProfile.objects.first()
        response = self.client.post(f'/api/userprofiles/{user_profile.id}/send_phone_verification/')
        self.assertEqual(response.status_code, 200)
        user_profile.user.refresh_from_db()
        self.assertIsNotNone(user_profile.user.phone_verification_code)
        self.assertTrue(timezone.now() < user_profile.user.phone_verification_expires)

    def test_verify_phone(self):
        self.test_send_phone_verification()
        user_profile = UserProfile.objects.first()
        code = user_profile.user.phone_verification_code
        response = self.client.post(f'/api/userprofiles/{user_profile.id}/verify_phone/', {'code': code})
        self.assertEqual(response.status_code, 200)
        user_profile.user.refresh_from_db()
        self.assertTrue(user_profile.user.is_phone_verified)

    def test_change_email_with_verification(self):
        self.test_verify_phone()
        user_profile = UserProfile.objects.first()
        new_email = 'newemail@example.com'
        response = self.client.post(f'/api/userprofiles/{user_profile.id}/change_email/', {'new_email': new_email})
        self.assertEqual(response.status_code, 200)
        user_profile.user.refresh_from_db()
        self.assertEqual(user_profile.user.email, new_email)

    def test_delete_user_profile_with_verification(self):
        self.test_verify_phone()
        user_profile = UserProfile.objects.first()
        response = self.client.delete(f'/api/userprofiles/{user_profile.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(UserProfile.objects.count(), 0)
