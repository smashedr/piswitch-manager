import os
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='get_config')
def get_config(value):
    if value in settings:
        return getattr(settings, value)
    return None


@register.filter(name='check_service_status')
def check_service_status(service_name):
    a = os.system('/usr/bin/env systemctl is-active {}'.format(service_name))
    if a == 0:
        return True
    else:
        return False
