from django import forms

from .models import Profile
from .validators import TwitterURLValidator


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['twitter_url'].validators.append(TwitterURLValidator())

    class Meta:
        model = Profile
        fields = (
            'twitter_url',
        )
