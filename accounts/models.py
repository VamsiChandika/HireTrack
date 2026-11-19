from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    class Role(models.TextChoices):
        JOB_SEEKER = 'JOB_SEEKER', 'Job Seeker'
        RECRUITER = 'RECRUITER', 'Recruiter'
        ADMIN = 'ADMIN', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER
    )

    def __str__(self):
        return self.username



class CandidateProfile(models.Model):

    user = models.OneToOneField(User,    
        on_delete=models.CASCADE,        
        related_name='candidate_profile'
    )
    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )
    skills = models.ManyToManyField('Skill',
        blank=True,
        related_name='candidates'
    )

    # 1. OneToOneField : Connects one candidate profile to exactly one user account.
    # 2. on_delete=models.CASCADE : If the associated user is deleted, their candidate profile is deleted automatically.
    # 3. related_name='candidate_profile' : Allows us to access a user's profile -- user.candidate_profile


    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    professional_title = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=200, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    linkedin_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Candidate Profile"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name