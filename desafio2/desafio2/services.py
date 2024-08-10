import os
import sys
import django

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desafio2.settings')
django.setup()

from desafioadl.models import Tarea, Subtarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = Subtarea.objects.all()

#recupera_tareas_y_sub_tareas()

def crear_nueva_tarea():
    tarea = Tarea(descripcion="Nueva tarea")
    tarea.save()
    print(f"Tarea creada con id: {tarea.id}")

#crear_nueva_tarea()

def crear_sub_tarea():
    tarea = Tarea.objects.get(id=3)
    
    subtarea = Subtarea(descripcion="Nueva subtarea", eliminada=False, tarea=tarea)
    subtarea.save()
    print(f"Subtarea creada con id: {subtarea.id}")

#crear_sub_tarea()

def elimina_tarea():
    tarea = Tarea.objects.get(id=3)
    tarea.eliminada = True
    tarea.save()
    print(f"Tarea eliminada con id: {tarea.id}")

#elimina_tarea()

def elimina_sub_tarea():
    subtarea = Subtarea.objects.get(id=6)
    subtarea.eliminada = True
    subtarea.save()
    print(f"Subtarea eliminada con id: {subtarea.id}")

#elimina_sub_tarea()

def imprimir_en_pantalla():
    tareas = Tarea.objects.all()
    for pos, tarea in enumerate(tareas):
        print(f"[{pos + 1}] {tarea.descripcion}")
        subtareas = Subtarea.objects.filter(tarea=tarea)
        for pos, subtarea in enumerate(subtareas):
            print(f".... [{pos + 1}] {subtarea.descripcion}")

imprimir_en_pantalla()