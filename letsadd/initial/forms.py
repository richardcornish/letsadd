from django import forms

from .models import Post, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'residence',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['residence'].disabled = True


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'body',
        ]
