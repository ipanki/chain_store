from django.contrib import admin

from applications.contacts.models import Contacts, Location


class ContactsInline(admin.TabularInline):
    model = Contacts
    fields = ('email', 'location')


@admin.register(Location)
class ContactsAdmin(admin.ModelAdmin):
    inlines = (ContactsInline,)
