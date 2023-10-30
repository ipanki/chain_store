from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from applications.companies.models import Company, CompanyProduct, Address


@admin.action(description="Cancel debt")
def cancel_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Address)
class Address(admin.ModelAdmin):
    model = Address
    list_display = ('country', 'city', 'street', 'house')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'supplier_name', 'debt', 'email')
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


@admin.register(CompanyProduct)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'product', 'company')
