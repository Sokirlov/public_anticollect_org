from django import template
import markdown
from django.utils.safestring import mark_safe
# from index.views import FooterListView

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)

#
# @register.inclusion_tag('index/footer.html')
# def footer():
#     return {'footer': FooterListView()}