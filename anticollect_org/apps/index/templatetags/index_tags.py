from django import template
import markdown
from django.utils.safestring import mark_safe
from index.models import Contacts, TopMenu
# from index.views import FooterListView

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)

#
@register.inclusion_tag('footer.html')
def footer():
    try:
        contacts = Contacts.objects.get()
    except:
        contacts = None
    return {'contacts': contacts}

@register.inclusion_tag('d-menu.html')
def navigation():
    navigation = TopMenu.objects.all().order_by('idsort')
    return {'navigation': navigation,}