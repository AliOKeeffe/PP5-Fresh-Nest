"""Product Views"""
from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, sorting and search queries """

    products = Product.objects.all().order_by('sku')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)