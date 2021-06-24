from django.views.generic import CreateView
from .models import Clients
from index.models import Blocks
from .forms import ClientsForm
# from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.detail import DetailView


class ClientsView(CreateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'clients/form.html'
    success_url = '/thanks/' #reverse_lazy('/')

def index(request):
    if request.POST:
        form = ClientsView(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Новая заявка от {} , на сумму {} '.format(cd['name'], cd['summ'],)
            message = '{} из {}.\n Имеет {} на сумму {}\n\'s comments:'.format(cd['name'], cd['region'], cd['penalty'], cd['price'],)
            send_mail(subject, message, 'send@fotka.kiev.ua', ['k.sokolov@dgfinance.com.ua'], fail_silently=False)
            # sent = True

            cd.save()  # use form to save it in DB
        else:
            return render(request, 'index/blocks_list.html' )
    context = {'price': price, 'clients_form':form}
    return render(request, 'index/blocks_list.html', context)


class Thanks(DetailView):
    model = Blocks
    context_object_name = 'index_all'
    queryset = Blocks.objects.filter(status='published').order_by('idsort')

    def get_context_data(self, **kwargs):
        context = super(BlocksListView, self).get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.get(id=1)
        return context

# 'name', 'tel', 'summ', 'region', 'penalty', 'price', 'about'