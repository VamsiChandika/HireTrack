from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CandidateProfile, Skill

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
    )

    list_filter = ('role', 'is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('HireTrack Role', {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('HireTrack Role', {'fields': ('role',)}),
    )


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'phone_number',
        'location',
        'professional_title',
        'experience_years',
    )

    search_fields = ('user__username', 'location')

    list_filter = ('location', 'experience_years')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)