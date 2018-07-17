from rest_framework import permissions
# from django.contrib.auth.models import User  # , Group


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        print(request.user)

        # return obj.owner == request.user
#        user = User.objects.get(username=request.user)

#        return user.is_staff()
        return request.user.is_staff
