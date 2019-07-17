from django import forms


class RedisSettings(forms.Form):
    twitch_user = forms.CharField(max_length=255, label='Twitch Username')
    redis_pass = forms.CharField(max_length=255, label='Redis Password')
    redis_host = forms.CharField(max_length=255, label='Redis Hostname')
    redis_port = forms.IntegerField(label='Redis Port')
    redis_db = forms.IntegerField(label='Redis DB')

    def clean_redis_port(self):
        data = self.cleaned_data['redis_port']
        try:
            return int(data)
        except:
            raise forms.ValidationError('Please specify a valid port number.')

    def clean_redis_db(self):
        data = self.cleaned_data['redis_db']
        try:
            return int(data)
        except:
            raise forms.ValidationError('Please specify a valid db number.')


class WiFiSettings(forms.Form):
    wifi_sec_before_auto = forms.IntegerField()
    wifi_auto_config = forms.BooleanField(required=False)

    def clean_wifi_sec_before_auto(self):
        data = self.cleaned_data['wifi_sec_before_auto']
        try:
            return int(data)
        except:
            raise forms.ValidationError('Please specify a valid number of seconds.')
