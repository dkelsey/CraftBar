from rest_framework import permissions
# from django.contrib.auth.models import User  # , Group


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow employees edit.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed by staff.
        return request.user.is_staff

    def has_permission(self, request, view):
        """
        Custom permission to only allow employees to edit.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff
