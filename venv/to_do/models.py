from django.db import models

# Create your models here. 
#connect in database
class Todo(models.Model):
    tittle = models.CharField(max_length=150, null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    date_final = models.DateTimeField(null=True) 