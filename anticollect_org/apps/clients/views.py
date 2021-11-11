from django.views.generic import CreateView
from .models import Clients
from bot.tbb import new_clients
from .forms import ClientsForm
from django.contrib.auth.models import User


#from django.core.mail import send_mail


def operator_sort():
    previus = []
    cols = User.objects.filter(groups__name='Operators').count()
    serched = cols - 1
    for i in range(serched):
        previus.append(str(Clients.objects.filter(pathFrom='site').order_by('-dateAdd')[i].operator))
    thisOperator = User.objects.filter(groups__name='Operators').exclude(username__in=previus)
    return thisOperator[0]


class ClientsView(CreateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'clients/form.html'
    success_url = '/thanks/' #reverse_lazy('/')

    def form_valid(self, form):
            cd = form.cleaned_data
            # subject = 'Новая заявка от {} - сумму удержания {} '.format(cd['name'], cd['summ'], )
            message = '{}. На сумму {} Планирует заказать пакет {} Телефон:{}. Коротко про {}'.format(cd['name'], cd['summ'], cd['price'], cd['tel'], cd['about'])
            # html_message = '{} из {}.<br /> Имеет {} на сумму {}<br /> Планирует заказать пакет {}<br /> Телефон:{}<br/><hr/>{}'.format(
            #     cd['name'], cd['region'], cd['penalty'], cd['summ'], cd['price'], cd['tel'], cd['about'])
            # send_mail(subject, message, 'send@fotka.kiev.ua', ['v.shestakov@dgfinance.com.ua'], html_message=html_message)
            # send_mail(subject, message, 'send@fotka.kiev.ua', ['e.kiyanitsa@dgfinance.com.ua'], html_message=html_message)
            # send_mail(subject, message, 'send@fotka.kiev.ua', ['soxwhite@gmail.com'], html_message=html_message)
            # TODO uncoment send messages
            new_clients(message)

            form.instance.pathFrom = 'site'
            form.instance.operator =operator_sort()

            return super(ClientsView, self).form_valid(form)