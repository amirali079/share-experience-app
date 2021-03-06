from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from socialmedia.models import User


class IsSelfOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.method in SAFE_METHODS and not obj.is_superuser:
            return True
        elif request.user == obj:
            return True
        else:
            return False
