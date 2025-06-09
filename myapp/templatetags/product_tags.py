from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def get_product_info(pid, name, price):
    return mark_safe(f"<h1>{pid}-{name}-{price}</h1>")