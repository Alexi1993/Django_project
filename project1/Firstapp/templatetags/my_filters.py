from django import template

register = template.Library()
@register.filter(name='sort&censor')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        return str(value)
    else:
        raise ValueError(f'You cannot find{type(value)}')