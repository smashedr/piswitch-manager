import logging
import os
from dotenv import load_dotenv
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import RedisSettings, WiFiSettings
from pprint import pformat

logger = logging.getLogger('app')


def show_redis(request):
    #  View: /
    data = get_redis_settings(settings_file=settings.PISWITCH_SETTINGS)
    logger.debug(data)
    form = RedisSettings()
    form.fields['twitch_user'].initial = data['TWITCH_USER']
    form.fields['redis_pass'].initial = data['REDIS_PASS']
    form.fields['redis_host'].initial = data['REDIS_HOST']
    form.fields['redis_port'].initial = data['REDIS_PORT']
    form.fields['redis_db'].initial = data['REDIS_DB']
    return render(request, 'home.html', {'data': data, 'form': form})


def save_redis(request):
    #  View: /saveredis
    logger.debug(pformat(request.POST))
    form = RedisSettings(request.POST)
    if not form.is_valid():
        logger.debug('INVALID FORM --------------')
        messages.add_message(request, messages.ERROR, form.errors, extra_tags='danger')
        return redirect('home:redis')
    else:
        logger.debug('VALID FORM ++++++++++++++++')
        data = {
            'TWITCH_USER': form.cleaned_data['twitch_user'],
            'REDIS_PASS': form.cleaned_data['redis_pass'],
            'REDIS_HOST': form.cleaned_data['redis_host'],
            'REDIS_PORT': form.cleaned_data['redis_port'],
            'REDIS_DB': form.cleaned_data['redis_db'],
        }
        logger.debug(data)
        write_settings(data, settings_file=settings.PISWITCH_SETTINGS)
        message = 'Redis settings successfully saved.'
        messages.add_message(request, messages.SUCCESS, message, extra_tags='success')
        return redirect('home:redis')


def show_wifi(request):
    #  View: /wifi
    form = WiFiSettings()
    form.fields['wifi_sec_before_auto'].initial = 300
    form.fields['wifi_auto_config'].initial = False
    return render(request, 'wifi.html', {'form': form})


def save_wifi(request):
    #  View: /savewifi
    logger.debug(pformat(request.POST))
    form = WiFiSettings(request.POST)
    if not form.is_valid():
        logger.debug('INVALID FORM --------------')
        messages.add_message(request, messages.ERROR, form.errors, extra_tags='danger')
        return redirect('home:wifi')
    else:
        logger.debug('VALID FORM ++++++++++++++++')
        data = {
            'wifi_sec_before_auto': form.cleaned_data['wifi_sec_before_auto'],
            'wifi_auto_config': form.cleaned_data['wifi_auto_config'],
        }
        logger.debug(data)
        write_settings(data, settings.WIFI_SETTINGS)
        message = 'WiFi settings successfully saved.'
        messages.add_message(request, messages.SUCCESS, message, extra_tags='success')
        return redirect('home:wifi')


def get_redis_settings(settings_file):
    load_dotenv(settings_file, override=True)
    return {
        'TWITCH_USER': os.environ.get('TWITCH_USER'),
        'REDIS_PASS': os.environ.get('REDIS_PASS'),
        'REDIS_HOST': os.environ.get('REDIS_HOST'),
        'REDIS_PORT': os.environ.get('REDIS_PORT'),
        'REDIS_DB': os.environ.get('REDIS_DB'),
    }


def write_settings(data, settings_file):
    output = ''
    for key, value in data.items():
        output += '{}={}\n'.format(key, value)
    with open(settings_file, 'w+') as f:
        f.write(output)
