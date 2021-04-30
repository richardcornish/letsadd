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
        min_ = cleaned_data.get('min')
        max_ = cleaned_data.get('max')

        if min_ and min_:
            if min_ ==  max_:
                message = 'The minimum field is equal to the maximum field.'
                raise forms.ValidationError(message, code='invalid')
            elif min_ >  max_:
                message = 'The minimum field is greater than the maximum field.'
                raise forms.ValidationError(message, code='invalid')
