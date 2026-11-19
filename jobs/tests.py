
from django.test import TestCase
from accounts.models import User
from jobs.models import Job


class JobModelTest(TestCase):

    def test_job_creation(self):
        recruiter = User.objects.create_user(
            username='recruiter_test',
            password='testpassword123',
            role='RECRUITER'
        )
        job = Job.objects.create(
            recruiter=recruiter,
            title='Python Developer',
            company_name='Tech Solutions',
            description='Python and Django developer required',
            location='Hyderabad',
            job_type='FULL_TIME',
            experience_required=0,
            skills_required='Python, Django',
            is_active=True
        )
        self.assertEqual(job.title, 'Python Developer')
        self.assertEqual(job.company_name, 'Tech Solutions')
        self.assertEqual(job.recruiter.role, 'RECRUITER')
        self.assertTrue(job.is_active)
