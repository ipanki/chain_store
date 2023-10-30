from rest_framework.permissions import BasePermission


class CompanyPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['create', 'update', 'partial_update', 'retrieve', 'destroy']:
            return obj.owner == request.user
        return False


class CompanyProductPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'create', 'update', 'partial_update', 'destroy']:
            return obj.company.owner == request.user
        return False
