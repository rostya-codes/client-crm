from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from clients.forms import ClientForm
from clients.models import Client


class HomeView(TemplateView):
    template_name = 'clients/index.html'


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm


class AddClientView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/add_client.html'
    success_url = reverse_lazy('clients:clients-list')


class ClientsListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'  # Шаблон для отображения списка клиентов
    context_object_name = 'clients'  # Имя переменной для доступа к объектам в шаблоне
    paginate_by = 10  # Количество клиентов на одной странице
