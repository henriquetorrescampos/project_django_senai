from django.db import models

# Create your models here. 
#connect in database
class Todo(models.Model):
    tittle = models.CharField(
        verbose_name = 'Titutlo da Tarefa',
        max_length = 150, 
        null = True, 
        blank = False)
    date_create = models.DateTimeField(
        verbose_name = 'Data da Criação',
        auto_now_add = True, 
        null = False, 
        blank = False)
    date_final = models.DateTimeField(
        verbose_name = 'Data da Finalização',
        null = False,
        blank = False) 