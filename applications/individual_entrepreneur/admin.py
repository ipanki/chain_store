from django.contrib import admin

from applications.individual_entrepreneur.models import IndividualEntrepreneur


class MembershipInline(admin.TabularInline):
    model = IndividualEntrepreneur.employees.through


@admin.register(IndividualEntrepreneur)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name', 'contacts')

