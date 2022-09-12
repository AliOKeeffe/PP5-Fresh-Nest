"""Product Models"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Model for Category"""

    class Meta:
        """Set verbose name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model for Product"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=False, blank=False, unique=True)
    name = models.CharField(max_length=254)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    estimated_dispatch = models.CharField(
        max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    liked = models.ManyToManyField(
        User, related_name='liked', default=None, blank=True)

    def __str__(self):
        return self.name
