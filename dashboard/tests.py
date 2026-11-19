
from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import User


class DashboardTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_job_seeker_dashboard(self):
        user = User.objects.create_user(
            username='seeker_test',
            password='testpassword123',
            role='JOB_SEEKER'
        )
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['role'], 'JOB_SEEKER')
        self.assertEqual(response.data['total_applications'], 0)

    def test_recruiter_dashboard(self):
        user = User.objects.create_user(
            username='recruiter_test',
            password='testpassword123',
            role='RECRUITER'
        )
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['role'], 'RECRUITER')
        self.assertEqual(response.data['total_jobs'], 0)

    def test_admin_dashboard(self):
        user = User.objects.create_superuser(
            username='admin_test',
            password='testpassword123',
            email='admin@example.com',
            role='ADMIN'
        )
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['role'], 'ADMIN')
        self.assertEqual(response.data['total_users'], 1)

    def test_unauthenticated_dashboard_access(self):
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, 401)
