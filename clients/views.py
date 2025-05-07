from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from clients.forms import ClientForm
from clients.models import Client


class HomeView(TemplateView):
    template_name = 'clients/index.html'


class AddClientView(TemplateView):
    template_name = 'clients/add_client.html'

    def get(self, request, *args, **kwargs):
        form = ClientForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:clients-list')
        return self.render_to_response({'form': form})  # Щоб залишитися на формі з помилками


class ClientsListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'  # Шаблон для отображения списка клиентов
    context_object_name = 'clients'  # Имя переменной для доступа к объектам в шаблоне
    paginate_by = 10  # Количество клиентов на одной странице
