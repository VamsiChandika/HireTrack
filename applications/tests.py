
from django.test import TestCase
from accounts.models import User
from jobs.models import Job
from applications.models import Application


class ApplicationModelTest(TestCase):

    def setUp(self):
        self.recruiter = User.objects.create_user(
            username='recruiter_test',
            password='testpassword123',
            role='RECRUITER'
        )
        self.job_seeker = User.objects.create_user(
            username='seeker_test',
            password='testpassword123',
            role='JOB_SEEKER'
        )
        self.job = Job.objects.create(
            recruiter=self.recruiter,
            title='Python Developer',
            company_name='Tech Solutions',
            description='Python developer required',
            location='Hyderabad',
            job_type='FULL_TIME',
            experience_required=0,
            skills_required='Python, Django',
            is_active=True
        )

    def test_application_creation(self):
        application = Application.objects.create(
            job=self.job,
            applicant=self.job_seeker,
            cover_letter='I am interested in this job.'
        )
        self.assertEqual(application.job, self.job)
        self.assertEqual(application.applicant, self.job_seeker)
        self.assertEqual(application.status, 'APPLIED')

    def test_duplicate_application_prevention(self):
        Application.objects.create(
            job=self.job,
            applicant=self.job_seeker
        )
        with self.assertRaises(Exception):
            Application.objects.create(
                job=self.job,
                applicant=self.job_seeker
            )
