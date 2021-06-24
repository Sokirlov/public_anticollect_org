from django.urls import path
from .views import BlocksListView

app_name = 'index'

urlpatterns = [
    path('', BlocksListView.as_view(), name='index_page'),
]