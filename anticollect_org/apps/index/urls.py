from django.urls import path
# from . import views
from .views import index# BlocksListView

app_name = 'index'

urlpatterns = [
    # path('', BlocksListView.as_view(), name='index_page'),
    path('', index, name='index_page'),
]