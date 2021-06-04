from django import template

register = template.Library()


@register.simple_tag
def get_field_display(field, choice):
    return ''.join([u[1] for u in field.field.choices if u[0] == choice])
