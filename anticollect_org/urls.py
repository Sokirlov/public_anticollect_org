from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('botTelegram/', include('bot.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('index.urls'), name='main'),
    path('blog/', include('blog.urls'), name='blog'),
    path('clients/', include('clients.urls')),
    path('thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks')
)
