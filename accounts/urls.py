from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import (
    CandidateProfileCreateView,
    CandidateProfileDetailView,
    UserRegistrationView,
    CandidateSkillsUpdateView,
)

urlpatterns = [
    path(
        'profile/create/',
        CandidateProfileCreateView.as_view(),
        name='candidate-profile-create'
    ),

    path(
        'profile/',
        CandidateProfileDetailView.as_view(),
        name='candidate-profile-detail'
    ),
    path(
        'register/',
        UserRegistrationView.as_view(),
        name='user-register'
    ),
    path(
        'login/',
        ObtainAuthToken.as_view(),
        name='user-login'
    ),
    path(
        'profile/skills/',
        CandidateSkillsUpdateView.as_view(),
        name='profile-skills'
    ),
]