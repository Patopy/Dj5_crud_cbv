from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    #queryset = Cliente.objects.all()
    template_name = "tempClientes/cliente_list.html"


