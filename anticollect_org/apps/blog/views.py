from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    slug_field = 'slug'
    ordering = 'idsort'
    context_object_name = 'blog_all'
    paginate_by = 12
    queryset = Blog.objects.filter(status='published').order_by('idsort')


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog_one'
