from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo

def home(request):
    return render(request, 'to_do/index.html')

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['tittle', 'date_final'] #lsita de campos que usuário pode alterar
    success_url = reverse_lazy('todo_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tittle'] = 'Adicionar Tarefa'
        return context

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['tittle', 'date_final'] #lsita de campos que usuário pode alterar
    success_url = reverse_lazy('todo_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tittle'] = 'Atualizar Tarefa'
        return context

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    template_name = 'to_do/confirm_delete.html'