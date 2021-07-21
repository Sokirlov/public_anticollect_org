from django import template
from clients.forms import ClientsForm


register = template.Library()

@register.inclusion_tag('clients/form.html')
def clients_form():
    return {'clients_form': ClientsForm()}


@register.inclusion_tag('clients/small-form.html')
def small_form():
    return {'clients_form': ClientsForm()}
