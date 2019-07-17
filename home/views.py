import logging
from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import PiSwitchSettings
from pprint import pformat

logger = logging.getLogger('app')


def show_settings(request):
    #  View: /
    data = {}
    form = PiSwitchSettings()
    return render(request, 'home.html', {'data': data, 'form': form})


def save_settings(request):
    #  View: /save
    logger.debug(pformat(request.POST))
    form = PiSwitchSettings(request.POST)
    logger.info(form)
    if not form.is_valid():
        logger.info('INVALID FORM --------------')
        messages.add_message(request, messages.ERROR, form.errors, extra_tags='danger')
        return redirect('home:show')
    else:
        logger.info('VALID FORM ++++++++++++++++')
        return redirect('home:show')
