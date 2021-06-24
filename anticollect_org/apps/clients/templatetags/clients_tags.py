from django import template
from clients.forms import ClientsForm
from clients.views import Thanks

register = template.Library()

@register.inclusion_tag('clients/form.html')
def clients_form():
    return {'clients_form': ClientsForm()}

@register.inclusion_tag('thanks.html')
def thanks():
    return {'thanks': Thanks()}

