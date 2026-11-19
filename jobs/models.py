from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):

    class JobType(models.TextChoices):
        FULL_TIME = 'FULL_TIME', 'Full Time'
        PART_TIME = 'PART_TIME', 'Part Time'
        INTERNSHIP = 'INTERNSHIP', 'Internship'
        CONTRACT = 'CONTRACT', 'Contract'

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )
    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices,
        default=JobType.FULL_TIME
    )
    salary_min = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    salary_max = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    experience_required = models.PositiveIntegerField(default=0)
    skills_required = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
