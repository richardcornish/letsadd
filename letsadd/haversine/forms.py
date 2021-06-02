import json
import urllib.parse
import urllib.request

from django import forms
from django.conf import settings

DEFAULT_RADIUS = 500  # miles
MINIMUM_RADIUS = 1  # miles


class SearchForm(forms.Form):
    address = forms.CharField(label='Location', help_text='Any address, city, postal code, etc.', widget=forms.TextInput(attrs={
        'type': 'search',
    }))
    radius = forms.IntegerField(initial=DEFAULT_RADIUS, min_value=MINIMUM_RADIUS, help_text='Miles')

    def get_point(self, address):
        outputFormat = 'json'
        parameters = urllib.parse.urlencode({
            'address': address,
            'key': settings.GOOGLE_API_KEY,
        })
        url = 'https://maps.googleapis.com/maps/api/geocode/%s?%s' % (outputFormat, parameters)
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read().decode('utf-8'))
            if body['status'] == 'OK':
                try:
                    return {
                        'latitude': body['results'][0]['geometry']['location']['lat'],
                        'longitude': body['results'][0]['geometry']['location']['lng'],
                        'formatted_address': body['results'][0]['formatted_address'],
                    }
                except KeyError:
                    return {}
                except IndexError:
                    return {}
            return {}
