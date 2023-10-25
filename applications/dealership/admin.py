from django.contrib import admin

from applications.dealership.models import Dealership


class MembershipInline(admin.TabularInline):
    model = Dealership.employees.through


@admin.register(Dealership)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name', 'contacts')

