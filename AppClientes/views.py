from django.shortcuts import render
from django.views.generic import ListView, CreateView,  DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    #queryset = Cliente.objects.all()
    template_name = "tempClientes/cliente_list.html"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tempClientes/cliente_form.html'
    success_url = reverse_lazy('AppClientes:list')

class ClienteDetalle(DetailView):
    model = Cliente
    template_name = 'tempClientes/cliente_detalle.html' # Nombre del template

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tempClientes/cliente_form.html'
    success_url = reverse_lazy('AppClientes:list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'tempClientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('AppClientes:list')