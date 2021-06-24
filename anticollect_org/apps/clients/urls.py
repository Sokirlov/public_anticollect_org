from django.urls import path
from .views import ClientsView

app_name = 'clients'

urlpatterns =[
    path('', ClientsView.as_view(), name='clients')
]