from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    export = forms.BooleanField(label='Export?', required=False)

    class Meta:
        model = Customer
        fields = [
            'flag',
        ]
