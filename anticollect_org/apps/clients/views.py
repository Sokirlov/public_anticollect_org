from django.views.generic import CreateView
from .models import Clients
from bot.tbb import new_clients
from .forms import ClientsForm
from django.core.mail import send_mail

class ClientsView(CreateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'clients/form.html'
    success_url = '/thanks/'

    def form_valid(self, form):
            cd = form.cleaned_data
            subject = 'Новая заявка от {} - сумму удержания {} '.format(cd['name'], cd['summ'], )
            message = '{} из {}. Имеет {} на сумму {} Планирует заказать пакет {} Телефон:{}. Коротко про{}'.format(
                cd['name'], cd['region'],cd['penalty'], cd['summ'], cd['price'], cd['tel'], cd['about'])
            html_message = '{} из {}.<br /> Имеет {} на сумму {}<br /> Планирует заказать пакет {}<br /> Телефон:{}<br/><hr/>{}'.format(
                cd['name'], cd['region'], cd['penalty'], cd['summ'], cd['price'], cd['tel'], cd['about'])
            send_mail(subject, message, 'send@fotka.kiev.ua', ['v.shestakov@dgfinance.com.ua', 'e.kiyanitsa@dgfinance.com.ua', 'soxwhite@gmail.com'], html_message=html_message)
            new_clients(message)

            return super(ClientsView, self).form_valid(form)
