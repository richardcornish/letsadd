from django import forms


class SeriesForm(forms.Form):
    previous = forms.IntegerField(initial=0, widget=forms.HiddenInput)
    current = forms.IntegerField(initial=0, label='Number')

    def add_numbers(self):
        previous = self.cleaned_data['previous']
        current = self.cleaned_data['current']
        return previous + current
