from django import template
register = template.Library()
from django.utils.safestring import mark_safe
import markdown


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)