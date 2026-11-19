from django.test import TestCase
from accounts.models import User

class UserModelTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            role='JOB_SEEKER'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'JOB_SEEKER')
        self.assertTrue(user.check_password('testpassword123'))

