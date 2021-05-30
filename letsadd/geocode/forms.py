import json
import urllib

from django import forms
from django.conf import settings

DEFAULT_ADDRESS = '90210'
MINIMUM_RADIUS = 1  # miles
DEFAULT_RADIUS = 10  # miles
METERS_IN_MILE = 1609.344  # meters


class SearchForm(forms.Form):
    address = forms.CharField(label='Postal code', initial=DEFAULT_ADDRESS, widget=forms.TextInput(attrs={
        'type': 'search',
        'placeholder': 'Search places',
    }))
    radius = forms.IntegerField(initial=DEFAULT_RADIUS, min_value=MINIMUM_RADIUS, help_text='Miles')

    def as_meters(self, miles):
        return int(miles * METERS_IN_MILE)

    def geocode_query(self, address):
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
                    latitude = body['results'][0]['geometry']['location']['lat']
                    longitude = body['results'][0]['geometry']['location']['lng']
                    return (latitude, longitude)
                except KeyError:
                    return None
                except IndexError:
                    return None
            return None

    def search_nearby(self, latitude, longitude, radius):
        output = 'json'
        parameters = urllib.parse.urlencode({
            'location': '%s,%s' % (latitude, longitude),
            'radius': '%s' % self.as_meters(radius),
            'type': 'restaurant',
            'key': settings.GOOGLE_API_KEY,
        })
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/%s?%s' % (output, parameters)
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read().decode('utf-8'))
            if body['status'] == 'OK':
                return body['results']
            return None

    def get_results(self, query):
        latitude, longitude = self.geocode_query(query)
        if (latitude, longitude) is not None:
            data = self.search_nearby(latitude, longitude, self.cleaned_data['radius'])
            if data is not None:
                return {
                    'data': data,
                    'coords': {
                        'latitude': latitude,
                        'longitude': longitude,
                    },
                }
        return None
