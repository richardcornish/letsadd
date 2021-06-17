from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    export = forms.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = [
            'flag',
        ]
