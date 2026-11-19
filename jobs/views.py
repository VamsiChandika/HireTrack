from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Job
from .serializer import JobSerializer
from .permissions import IsRecruiterOrReadOnly

# Create your views here.

class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsRecruiterOrReadOnly
    ]
    filterset_fields = [
        'location',
        'job_type',
        'experience_required',
    ]
    search_fields = [
        'title',
        'company_name',
        'description',
        'skills_required',
    ]
    ordering_fields = [
        'created_at',
        'salary_min',
        'experience_required',
    ]

    def get_queryset(self):
        return Job.objects.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsRecruiterOrReadOnly
    ]

    def get_queryset(self):
        return Job.objects.all()
