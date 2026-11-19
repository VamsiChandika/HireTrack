from django.contrib import admin
from .models import Job

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = (
        'id',
        'title',
        'company_name',
        'recruiter',
        'job_type',
        'location',
        'is_active',
        'created_at',
    )
    list_filter = (
        'job_type',
        'is_active',
        'location',
    )
    search_fields = (
        'title',
        'company_name',
        'location',
    )
    
