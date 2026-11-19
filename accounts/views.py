from django.shortcuts import render

# Create your views here.


from rest_framework import generics, permissions
from .models import CandidateProfile
from .serializers import CandidateProfileSerializer
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer

# For Candidate profile creation

class CandidateProfileCreateView(generics.CreateAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# For Candidate profile details

class CandidateProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CandidateProfile.objects.filter(
            user=self.request.user
        )

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

# For User Registration

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# For Skills 

from .serializers import CandidateSkillsSerializer

class CandidateSkillsUpdateView(generics.UpdateAPIView):
    serializer_class = CandidateSkillsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            CandidateProfile,
            user=self.request.user
        )