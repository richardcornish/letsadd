from random import randint

from django import forms


class AlphabetizeForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter text'}))
    reverse = forms.BooleanField(label='Reverse?', required=False)

    def alphabetize(self):
        text = self.cleaned_data['text']
        reverse = self.cleaned_data['reverse']
        iterable = text.splitlines()
        l = sorted(iterable, key=str.casefold, reverse=reverse)
        return '\n'.join(l)
