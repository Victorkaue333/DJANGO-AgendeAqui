from django.urls import reverse_lazy
from django.views import generic
from .models import Sala


class SalaListView(generic.ListView):
    model = Sala
    template_name = 'salas/list.html'
    context_object_name = 'salas'


class SalaCreateView(generic.CreateView):
    model = Sala
    fields = ['nome', 'capacidade', 'bloco', 'recursos']
    template_name = 'salas/form.html'
    success_url = reverse_lazy('salas:list')


class SalaUpdateView(generic.UpdateView):
    model = Sala
    fields = ['nome', 'capacidade', 'bloco', 'recursos']
    template_name = 'salas/form.html'
    success_url = reverse_lazy('salas:list')


class SalaDeleteView(generic.DeleteView):
    model = Sala
    template_name = 'salas/confirm_delete.html'
    success_url = reverse_lazy('salas:list')
