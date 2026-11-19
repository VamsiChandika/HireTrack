from rest_framework import generics, permissions
from .models import Application
from .serializer import ApplicationSerializer,     ApplicationStatusSerializer


# Create Jobseeker Applications View

from .permissions import IsJobSeeker

class ApplicationCreateView(generics.CreateAPIView):

    serializer_class = ApplicationSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        IsJobSeeker
    ]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class MyApplicationsView(generics.ListAPIView):

    serializer_class = ApplicationSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        IsJobSeeker
    ]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        )

# Create Recruiter Applications View

from .permissions import IsRecruiterOrAdmin

class RecruiterApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsRecruiterOrAdmin
    ]

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return Application.objects.all()
        return Application.objects.filter(
            job__recruiter=self.request.user
        )


# Its Application Status Update View

class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsRecruiterOrAdmin
    ]
    http_method_names = ['patch', 'put', 'head', 'options']

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return Application.objects.all()
        return Application.objects.filter(
            job__recruiter=self.request.user
        )