"""imports for admin page"""

from django.contrib import admin
from .models import Service, Testimonial, PreviousProject


class ServiceAdmin(admin.ModelAdmin):
    """Allows admin to manage Services via the admin panel"""
    list_display = (
        'type',
        'image',
    )


class TestimonialAdmin(admin.ModelAdmin):
    """Allows admin to manage Testimonials via the admin panel"""
    list_display = (
        'name',
        'service',
        'created_on'
    )


class PreviousProjectAdmin(admin.ModelAdmin):
    """Allows admin to manage Previous Projects via the admin panel"""
    list_display = (
        'service',
        'location',
        'image',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(PreviousProject, PreviousProjectAdmin)
