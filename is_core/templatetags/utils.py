from django.template.base import Library

register = Library()


@register.filter
def to_list(value):
    if isinstance(value, (list, tuple)):
        return value

    return [value]
