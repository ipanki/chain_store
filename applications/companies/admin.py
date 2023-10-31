from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from applications.companies.models import (Address, Company, CompanyProduct,
                                           Employee)
from applications.companies.tasks import async_cancel_debt


@admin.action(description="Cancel debt")
def cancel_debt(modeladmin, request, queryset):
    if len(queryset) > 20:
        companies_id = queryset.values_list("pk", flat=True)
        async_cancel_debt.delay(list(companies_id))
    else:
        queryset.update(debt=0)


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'supplier_name',
                    'debt', 'email', 'copy_email')
    list_filter = ('address__city',)
    actions = [cancel_debt]

    def supplier_name(self, obj):
        if not obj.supplier:
            return "-"
        app_label = obj._meta.app_label
        model_label = obj._meta.model_name
        url = reverse(
            f'admin:{app_label}_{model_label}_change', args=(obj.supplier.id,)
        )
        return mark_safe(f'<a href="{url}">{obj.supplier.name}</a>')

    def copy_email(self, obj):
        return format_html(
            '<button onclick="copyToClipBoard(\'{}\')">Copy email</button>', obj.email)

    class Media:
        js = [
            'clipboard.js'
        ]


@admin.register(CompanyProduct)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'product', 'company')


@admin.register(Employee)
class Address(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company')
