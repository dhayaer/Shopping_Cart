from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def to(value, arg):
    return range(1, arg + 1)
