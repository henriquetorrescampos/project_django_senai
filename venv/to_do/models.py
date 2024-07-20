from django.db import models

# Create your models here. 
#connect in database
class Todo(models.Model):
    # id = models.PositiveIntegerField()
    # history = models.IntegerField(default=0)
    tittle = models.CharField(
        verbose_name='Titutlo da Tarefa',
        max_length=150, 
        null=False, #não posso deixar como nulo
        blank=False) #não posso deixar vazio
    
    date_create = models.DateTimeField(
        verbose_name='Data da Criação',
        auto_now_add=True, 
        null=False, #false, não posso deixar como nulo
        blank=True) #true = eu posso deixar em branco
    
    date_final = models.DateTimeField(
        verbose_name='Data da Finalização',
        null=True,
        blank=True) 