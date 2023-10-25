from django.contrib import admin

from applications.authentication.models import User


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups',
                                    'user_permissions')}),
        ('Custom info', {'fields': ('title', 'role')}),
    )
