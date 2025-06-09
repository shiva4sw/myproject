from django import template
register = template.Library()

@register.simple_tag
def my_tag():
    return 'This is my tag'
