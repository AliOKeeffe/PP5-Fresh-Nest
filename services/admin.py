"""imports for admin page"""

from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    """Allows admin to manage Services via the admin panel"""
    list_display = (
        'type',
        "description",
        'image',
    )

admin.site.register(Service, ServiceAdmin)


