from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = (
        'id',
        'job',
        'applicant',
        'status',
        'applied_at',
    )
    list_filter = ('status', 'applied_at')
    search_fields = (
        'applicant__username',
        'job__title',
    )
    