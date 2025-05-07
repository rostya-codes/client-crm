from django.urls import path

from . views import *


app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-client/', AddClientView.as_view(), name='add-client'),
    path('clients-list/', ClientsListView.as_view(), name='clients-list')
]
