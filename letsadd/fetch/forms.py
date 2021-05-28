from django import forms
from django.db.models import Q

from .models import Post


class SearchForm(forms.Form):
    q = forms.CharField(label='Query', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Post Search..',
    }))

    def get_results(self, query):
        qs = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(image__icontains=query))
        return qs
