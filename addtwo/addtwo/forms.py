from django import forms


class AddForm(forms.Form):
    num_one = forms.IntegerField(label='Number one')
    num_two = forms.IntegerField(label='Number two')

    def add_numbers(self):
        num_one = self.cleaned_data['num_one']
        num_two = self.cleaned_data['num_two']
        return num_one + num_two
