import json
import urllib.parse
import urllib.request

from django import forms
from django.conf import settings

from .choices import TYPE_CHOICES

DEFAULT_ADDRESS = '90210'
DEFAULT_RADIUS = 5  # miles
MINIMUM_RADIUS = 1  # miles
METERS_IN_MILE = 1609.344  # meters


class SearchForm(forms.Form):
    address = forms.CharField(label='Postal code', initial=DEFAULT_ADDRESS, widget=forms.TextInput(attrs={
        'type': 'search',
        'placeholder': 'Search places',
    }))
    type = forms.ChoiceField(initial='restaurant', choices=TYPE_CHOICES)
    radius = forms.IntegerField(initial=DEFAULT_RADIUS, min_value=MINIMUM_RADIUS, help_text='Miles')

    def to_meters(self, miles):
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
                    return {
                        'latitude': body['results'][0]['geometry']['location']['lat'],
                        'longitude': body['results'][0]['geometry']['location']['lng'],
                    }
                except KeyError:
                    return None
                except IndexError:
                    return None
            return None

    def search_nearby(self, coordinates, tipe, radius):
        output = 'json'
        parameters = urllib.parse.urlencode({
            'location': '%s,%s' % (coordinates['latitude'], coordinates['longitude']),
            'radius': '%s' % self.to_meters(radius),
            'type': tipe,
            'key': settings.GOOGLE_API_KEY,
        })
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/%s?%s' % (output, parameters)
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read().decode('utf-8'))
            if body['status'] == 'OK':
                return body['results']
            return None

    def get_results(self, query):
        coordinates = self.geocode_query(query)
        if coordinates is not None:
            data = self.search_nearby(coordinates, self.cleaned_data['type'], self.cleaned_data['radius'])
            if data is not None:
                return {
                    'data': data,
                    'coordinates': coordinates,
                }
        return None
