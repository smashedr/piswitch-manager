from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='get_config')
def get_config(value):
    if value in settings:
        return getattr(settings, value)
    return None
