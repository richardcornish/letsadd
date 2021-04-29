from random import randint

from django import forms


class RandomForm(forms.Form):
    min = forms.IntegerField(initial=1, label='Minimum')
    max = forms.IntegerField(initial=10, label='Maximum')

    def generate_number(self):
        a = self.cleaned_data['min']
        b = self.cleaned_data['max']
        return randint(a, b)
