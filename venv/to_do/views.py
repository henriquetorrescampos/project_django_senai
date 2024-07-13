from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home(request):
    return render(request, 'to_do/index.html')


def todoListar(request):
    # tarefas = [{
    #     'id': '1',
    #     'Tarefa': 'Comprar fralda'
    # }]
    tasks = Todo.objects.all()
    
    return render(request, 'to_do/todoList.html', {'tasks': tasks})