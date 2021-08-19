from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    """Allow User to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Update Own Status"""

    def has_object_permission(self, request, view, obj):
        """Checks User is updating thier own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
