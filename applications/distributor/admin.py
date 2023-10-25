from django.contrib import admin

from applications.distributor.models import Distributor


class MembershipInline(admin.TabularInline):
    model = Distributor.employees.through


@admin.register(Distributor)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name', 'contacts')

