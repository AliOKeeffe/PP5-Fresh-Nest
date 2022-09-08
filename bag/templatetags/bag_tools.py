from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ returns the subtotal of a product line item """
    return price * quantity
