"""imports for admin page"""

from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""
    list_display = (
        'name',
        'email',
        'enquiry_type',
        'date',
    )


admin.site.register(Contact, ContactAdmin)
