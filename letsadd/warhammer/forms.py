import random

from django import forms

from .utils.choices import chapters, humans


class ChapterForm(forms.Form):
    chapter = forms.CharField(required=False, widget=forms.HiddenInput)
    name = forms.CharField(required=False, widget=forms.HiddenInput)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not self.fields['chapter'].initial:
    #         self.fields['chapter'].initial = self.generate_chapter()
    #     if not self.fields['name'].initial:
    #         self.fields['name'].initial = self.generate_name()
