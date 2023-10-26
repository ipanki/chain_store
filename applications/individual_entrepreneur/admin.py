from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from applications.individual_entrepreneur.models import IndividualEntrepreneur


@admin.action(description="Cancel debt")
def cancel_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class EmployeeInline(admin.TabularInline):
    model = IndividualEntrepreneur.employees.through


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline,)
    list_display = ('name', 'email', 'supplier_name', 'debt', 'created_date')
    list_filter = ('contacts__location__city',)
    actions = [cancel_debt]

    def email(self, obj):
        return obj.contacts.email

    def supplier_name(self, obj):
        app_label = obj.supplier._meta.app_label
        model_label = obj.supplier._meta.model_name
        url = reverse(
            f'admin:{app_label}_{model_label}_change', args=(obj.supplier.id,)
        )
        return mark_safe(f'<a href="{url}">{obj.supplier.name}</a>')
