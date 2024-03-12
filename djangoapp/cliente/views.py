from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Cliente
from .forms import ClienteForm

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/pages/index.html'
    