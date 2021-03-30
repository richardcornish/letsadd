from django import forms


class AddForm(forms.Form):
    num_one = forms.IntegerField(label='Number one')
    num_two = forms.IntegerField(label='Number two')
