"""imports for admin page"""

from django.contrib import admin
from .models import Service, Testimonial

class ServiceAdmin(admin.ModelAdmin):
    """Allows admin to manage Services via the admin panel"""
    list_display = (
        'type',
        "description",
        'image',
    )

class TestimonialAdmin(admin.ModelAdmin):
    """Allows admin to manage Testimonials via the admin panel"""
    list_display = (
        'service',
        "body",
    )



admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)


