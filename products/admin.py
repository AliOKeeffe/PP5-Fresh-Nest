"""imports for admin page"""

from django.contrib import admin
from .models import Product, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """Allows admin to manage categories via the admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    """Allows admin to manage products via the admin panel"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

