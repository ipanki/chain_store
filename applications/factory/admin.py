from django.contrib import admin

from applications.factory.models import Factory


class MembershipInline(admin.TabularInline):
    model = Factory.employees.through


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name', 'contacts')
