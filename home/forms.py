from django import forms
from django.conf import settings

import logging
logger = logging.getLogger('app')


class PiSwitchSettings(forms.Form):
    twitch_user = forms.CharField(max_length=255)
    redis_pass = forms.CharField(max_length=255)
    redis_host = forms.CharField(max_length=255)
    redis_port = forms.IntegerField()
    wifi_sec_before_auto = forms.IntegerField()
    wifi_auto_config = forms.BooleanField(required=False)

    def clean_redis_port(self):
        data = self.cleaned_data['redis_port']
        try:
            return int(data)
        except:
            raise forms.ValidationError('Please specify a valid port number.')

    def clean_wifi_sec_before_auto(self):
        data = self.cleaned_data['wifi_sec_before_auto']
        try:
            return int(data)
        except:
            raise forms.ValidationError('Please specify a valid number of seconds.')
