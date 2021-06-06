import json
import urllib.parse
import urllib.request
from math import pi

from django import forms
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.exceptions import ValidationError

from .managers import DEFAULT_UNITS, EARTH_RADIUS, METERS_IN

DEFAULT_RADIUS = 500  # miles

MINIMUM_RADIUS = 1  # miles


class SearchForm(forms.Form):
    UNITS_CHOICES = [
        ('mi', 'miles'),
        ('km', 'kilometers'),
    ]
    address = forms.CharField(label='Location', widget=forms.TextInput(attrs={
        'placeholder': 'Any address, city, ZIP code, etc.',
        'type': 'search',
    }))
    radius = forms.IntegerField(initial=DEFAULT_RADIUS, min_value=MINIMUM_RADIUS)
    units = forms.ChoiceField(initial=DEFAULT_UNITS, choices=UNITS_CHOICES)

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

    def clean(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get('radius')
        units = cleaned_data.get('units')
        if radius and units:
            if radius > pi * EARTH_RADIUS / METERS_IN[units]:
                units_display = ''.join([c[1] for c in self.UNITS_CHOICES if c[0] == units])
                radius_display = intcomma(radius)
                raise ValidationError('The radius %s %s exceeds half the circumference of Earth.' % (radius_display, units_display), code='max_value')
