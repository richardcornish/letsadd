from django import template

register = template.Library()


@register.simple_tag
def get_field_display(field, value):
    return ''.join([c[1] for c in field.field.choices if c[0] == value])[:-1]  # slice last 's'
