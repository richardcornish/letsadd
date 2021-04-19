from django import forms


class AddForm(forms.Form):
    one = forms.IntegerField(initial=0, label='Number one')
    two = forms.IntegerField(initial=0, label='Number two')

    def add_numbers(self):
        one = self.cleaned_data['one']
        two = self.cleaned_data['two']
        return one + two
