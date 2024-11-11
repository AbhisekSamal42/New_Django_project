from django import template
register=template.Library()

@register.filter('sw')
def swap(value):
    return value.swapcase()
@register.filter('sp')
def splitting(value,arg):
    return value.split(arg)
@register.filter('up')
def upper(value):
    return value.upper()
@register.filter('lw')
def lower(value):
    return value.lower()