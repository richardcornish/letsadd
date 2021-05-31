import json
import urllib.parse
import urllib.request

from django import forms
from django.conf import settings

from .choices import TYPE_CHOICES

DEFAULT_ADDRESS = '90210'
MINIMUM_RADIUS = 1  # miles
MAXIMUM_RADIUS = 30  # miles (30 ≈ 50000 / 1609.344)
METERS_IN_MILE = 1609.344  # meters


class SearchForm(forms.Form):
    PRICE_CHOICES = [
        (None, '(Optional)'),
        (0, '$'),
        (1, '$$'),
        (2, '$$$'),
        (3, '$$$$'),
        (4, '$$$$$'),
    ]
    address = forms.CharField(label='Location', initial=DEFAULT_ADDRESS, help_text='Any address, city, ZIP code, etc.', widget=forms.TextInput(attrs={
        'type': 'search',
    }))
    type = forms.ChoiceField(initial='restaurant', choices=TYPE_CHOICES, required=False)
    radius = forms.IntegerField(initial=MAXIMUM_RADIUS, min_value=MINIMUM_RADIUS, max_value=MAXIMUM_RADIUS, help_text='In miles')
    keyword = forms.CharField(required=False, help_text='Any additional term to filter')
    opennow = forms.BooleanField(label='Open now', required=False)
    minprice = forms.ChoiceField(label='Minimum price', initial=None, required=False, choices=PRICE_CHOICES)
    maxprice = forms.ChoiceField(label='Maximum price', initial=None, required=False, choices=PRICE_CHOICES)

    def to_meters(self, miles):
        return int(miles * METERS_IN_MILE)

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
                    }
                except KeyError:
                    return {}
                except IndexError:
                    return {}
            return {}

    def get_places(self, point):
        output = 'json'
        parameters = {
            'key': settings.GOOGLE_API_KEY,
            'location': '%s,%s' % (point['latitude'], point['longitude']),
            'radius': '%s' % self.to_meters(self.cleaned_data['radius']),
            'type': self.cleaned_data['type'],
        }
        if self.cleaned_data['keyword']:
            parameters['keyword'] = self.cleaned_data['keyword']        
        if self.cleaned_data['minprice']:
            parameters['minprice'] = self.cleaned_data['minprice']
        if self.cleaned_data['maxprice']:
            parameters['maxprice'] = self.cleaned_data['maxprice']
        if self.cleaned_data['opennow']:
            parameters['opennow'] = ''
        parameters = urllib.parse.urlencode(parameters)
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/%s?%s' % (output, parameters)
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read().decode('utf-8'))
            if body['status'] == 'OK':
                try:
                    return body['results']
                except KeyError:
                    return []
            return []
