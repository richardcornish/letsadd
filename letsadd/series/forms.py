from django import forms


class SeriesForm(forms.Form):
    prev = forms.IntegerField(label='Previous', initial=0, widget=forms.HiddenInput)
    num = forms.IntegerField(label='Number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num'].initial = None

    def add_numbers(self):
        prev = self.cleaned_data['prev']
        num = self.cleaned_data['num']
        return prev + num
