
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRecruiterOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.role in [
                'RECRUITER',
                'ADMIN'
            ]
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == 'ADMIN':
            return True
        return obj.recruiter == request.user
