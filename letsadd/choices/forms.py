from django import forms

from .models import Bot


class BotForm(forms.ModelForm):
    SITE_SUPPORTED_CHOICES = [
        ('Adidas', 'Adidas'),
        ('Shopify', 'Shopify'),
        ('Supreme', 'Supreme'),
        ('Footsites', 'Footsites'),
        ('YeezySupply', 'YeezySupply'),
        ('Mesh', 'Mesh'),
        ('AIO', 'AIO'),
    ]
    site_supported = forms.MultipleChoiceField(choices=SITE_SUPPORTED_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Bot
        fields = (
            'name',
            'site_supported',
        )

    def clean_site_supported(self):
        return ', '.join(self.cleaned_data['site_supported'])
