from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from .models import Todo

def home(request):
    return render(request, 'to_do/index.html')


# def todoList(request):
    # tarefas = [{
    #     'id': '1',
    #     'Tarefa': 'Comprar fralda'
    # }]
    # tasks = Todo.objects.all()
    
    # return render(request, 'to_do/todoList.html', {'tasks': tasks})

class todoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['tittle', 'date_final'] #lsita de campos que usuário pode alterar
    