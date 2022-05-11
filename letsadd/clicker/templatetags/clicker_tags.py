from datetime import datetime

from django import template


register = template.Library()


@register.filter
@register.simple_tag
def iso8601(value):
    """
    Convert Python datetime to JavaScript ISO-8601 date format
    * Convert 6 microsecond places to 3 (a.k.a. milliseconds)
    * Replace +00:00 with Z

    https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators
    https://docs.python.org/3/library/datetime.html#datetime.time.isoformat
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    https://stackoverflow.com/questions/19654578/python-utc-datetime-objects-iso-format-doesnt-include-z-zulu-or-zero-offset
    """
    return value.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
