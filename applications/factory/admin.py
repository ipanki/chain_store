from django.contrib import admin

from applications.factory.models import Factory


class EmployeeInline(admin.TabularInline):
    model = Factory.employees.through


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline,)
    list_display = ('name', 'email', 'created_date')
    list_filter = ('contacts__location__city',)

    def email(self, obj):
        return obj.contacts.email
