from rest_framework.permissions import BasePermission, SAFE_METHODS

class AllowReadOnlyForUnauthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access for unauthenticated users
        return request.user and request.user.is_authenticated  # Full access for authenticated users
