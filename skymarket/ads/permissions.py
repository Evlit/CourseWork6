from rest_framework import permissions
from users.models import UserRoles


class AdminPermission(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user and request.user.is_authenticated
    #
    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class OwnerPermission(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
