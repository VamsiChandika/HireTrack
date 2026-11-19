"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views

    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Backend Urls imports
from django.contrib import admin
from django.urls import path, include

# Frontend Urls imports
from .views import home, login_page, register_page, dashboard_page, jobs_page, logout_page, job_detail_page
from .views import apply_job, my_applications_page, candidate_profile_page, resume_management_page, recruiter_jobs_page 
from .views import create_job_page, edit_job_page, delete_job_page, recruiter_applications_page, update_application_status_page

urlpatterns = [
    # Backend Urls paths
    path('admin/', admin.site.urls),
    path('api/accounts/',include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/applications/', include('applications.urls')),
    path('api/dashboard/', include('dashboard.urls')),

    # Frontend Urls paths
    # Url   View_Function  Html_Url
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('jobs/', jobs_page, name='jobs'),
    path('logout/', logout_page, name='logout'),
    path('jobs/<int:id>/', job_detail_page, name='job_detail'),
    path('jobs/<int:id>/apply/', apply_job, name='apply_job'),
    path('my-applications/', my_applications_page, name='my_applications'),
    path('profile/', candidate_profile_page, name='candidate_profile'),
    path('resume/', resume_management_page, name='resume_management'),
    path('recruiter/jobs/',recruiter_jobs_page,name='recruiter_jobs'),
    path('recruiter/jobs/create/',create_job_page,name='create_job'),
    path('recruiter/jobs/<int:id>/edit/',edit_job_page,name='edit_job'),
    path('recruiter/jobs/<int:id>/delete/',delete_job_page,name='delete_job'),
    path('recruiter/applications/',recruiter_applications_page,name='recruiter_applications'),
    path('recruiter/applications/<int:id>/update-status/',update_application_status_page,name='update_application_status'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )




