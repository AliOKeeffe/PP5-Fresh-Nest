"""Bag Views"""

from django.shortcuts import render

def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')