from django.urls import path
from .views import (
    ApplicationCreateView,
    MyApplicationsView,
    RecruiterApplicationsView,
    ApplicationStatusUpdateView,
)
urlpatterns = [
    path(
        '',
        ApplicationCreateView.as_view(),
        name='application-create'
    ),
    path(
        'my/',
        MyApplicationsView.as_view(),
        name='my-applications'
    ),
    path(
        'recruiter/',
        RecruiterApplicationsView.as_view(),
        name='recruiter-applications'
    ),
    path(
        '<int:pk>/status/',
        ApplicationStatusUpdateView.as_view(),
        name='application-status-update'
    ),
]