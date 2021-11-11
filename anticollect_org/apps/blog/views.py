from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from index.models import Contacts

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    slug_field = 'slug'
    ordering = 'idsort'
    context_object_name = 'blog_all'
    paginate_by = 12
    queryset = Blog.objects.filter(status='published').order_by('idsort')

    # def get_context_data(self, **kwargs):
    #     context = super(BlogListView, self).get_context_data(**kwargs)
    #     # context['index_all'] = Blocks.objects.filter(status='published').order_by('idsort')
    #     # context['contacts'] = Contacts.objects.get(id=1)
    #     return context

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog_one'
    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)
    #     context['index_all'] = Blocks.objects.filter(status='published').order_by('idsort')
    #     context['contacts'] = Contacts.objects.get(id=1)
    #     return context