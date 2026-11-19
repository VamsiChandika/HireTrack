from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from accounts.models import User
from jobs.models import Job
from applications.models import Application


class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

     # If Role is Recruiter
     #     
        if user.role == 'JOB_SEEKER':
            applications = Application.objects.filter(
                applicant=user
            )
            data = {
                "role": "JOB_SEEKER",
                "total_applications": applications.count(),
                "under_review": applications.filter(
                    status='UNDER_REVIEW').count(),
                "shortlisted": applications.filter(
                    status='SHORTLISTED').count(),
                "selected": applications.filter(
                    status='SELECTED').count(),
                "rejected": applications.filter(
                    status='REJECTED').count(),
            }
            return Response(data)

    # If Role is Recruiter
        
        if user.role == 'RECRUITER':
            jobs = Job.objects.filter(recruiter=user)
            applications = Application.objects.filter(
                job__recruiter=user
            )
            data = {
                "role": "RECRUITER",
                "total_jobs": jobs.count(),
                "active_jobs": jobs.filter(
                    is_active=True).count(),
                "total_applications": applications.count(),
                "under_review": applications.filter(
                    status='UNDER_REVIEW').count(),
                "shortlisted": applications.filter(
                    status='SHORTLISTED').count(),
                "selected": applications.filter(
                    status='SELECTED').count(),
                "rejected": applications.filter(
                    status='REJECTED').count(),
            }
            return Response(data)

    # If Role Is Admin

        if user.role == 'ADMIN':
            data = {
                "role": "ADMIN",
                "total_users": User.objects.count(),
                "total_job_seekers": User.objects.filter(
                    role='JOB_SEEKER').count(),
                "total_recruiters": User.objects.filter(
                    role='RECRUITER').count(),
                "total_jobs": Job.objects.count(),
                "active_jobs": Job.objects.filter(
                    is_active=True).count(),
                "total_applications": Application.objects.count(),
                "selected_applications": Application.objects.filter(
                    status='SELECTED').count(),
            }
            return Response(data)
        return Response({
            "message": "Invalid user role."
        })