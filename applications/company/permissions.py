from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions


class CompanyPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['create', 'update', 'partial_update', 'retrieve', 'delete']:
            return obj.user == request.user
        return False


class CompanyProductPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['create', 'update', 'partial_update', 'delete']:
            return obj.company.user == request.user
        elif view.action in ['retrieve']:
            return True
        return False