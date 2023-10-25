from django.contrib import admin

from applications.retail_chain.models import RetailChain


class MembershipInline(admin.TabularInline):
    model = RetailChain.employees.through


@admin.register(RetailChain)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name', 'contacts')

