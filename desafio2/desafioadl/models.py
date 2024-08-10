from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descripcion

class Subtarea(models.Model):
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion