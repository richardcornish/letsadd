from random import randint

from django import forms


class RandomForm(forms.Form):
    min = forms.IntegerField(initial=1, label='Minimum')
    max = forms.IntegerField(initial=10, label='Maximum')

    def generate_number(self):
        a = self.cleaned_data['min']
        b = self.cleaned_data['max']
        return randint(a, b)

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('min')
        b = cleaned_data.get('max')
        if a and b:
            if a >= b:
                message = 'Ensure the minimum value is less than the maximum value.'
                raise forms.ValidationError(message, code='min_value')
