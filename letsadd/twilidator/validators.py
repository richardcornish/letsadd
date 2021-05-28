from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class TwitterURLValidator(RegexValidator):
    regex = r'(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?!home|share|privacy|tos)(?P<username>[A-z0-9_]+)\/?'
    message = _('Please enter a valid URL of your Twitter profile')
    code = 'twitter'
