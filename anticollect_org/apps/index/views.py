from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blocks, Price, Contacts

class BlocksListView(ListView):
    model = Blocks
    slug_field = 'slug'
    ordering = 'idsort'
    context_object_name = 'index_all'
    # paginate_by = 12
    queryset = Blocks.objects.filter(status='published').order_by('idsort')

    def get_context_data(self, **kwargs):
        context = super(BlocksListView, self).get_context_data(**kwargs)
        context['price_all'] = Price.objects.filter(status='published').order_by('idsort')
        context['contacts'] = Contacts.objects.get(id=1)

        return context



class FooterListView(DetailView):
    model = Contacts
    template_name = 'index/footer.html'
    context_object_name = 'footer'
    queryset = Contacts.objects.all()


# class FooterListView(CreateView):
#     model = Contacts
#     context_object_name = 'footer'
#     # form_class = ZakazForm
#     # success_url = reverse_lazy('thanks')
#
# def index(request):
#     footer = FooterListView(request.GET)
#     context = {'footer':footer}
#
#     return render(request, 'index/footer.html', context)