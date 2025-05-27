from django import template
import os
from django.conf import settings

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter(name='has_image')
def has_image(product):
    try:
        if product.image and product.image.name:
            return os.path.isfile(os.path.join(settings.MEDIA_ROOT, product.image.name))
    except Exception:
        return False
    return False 