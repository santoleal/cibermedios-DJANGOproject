from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mediosDigitales.models import Cibermedios, Investigadores, Investigaciones

# Create your views here.

## 1. Trabajar con ver y agregar Cibermedios
def agregar_cibermedios(request):
    return HttpResponse("Agregar Ciber...")

def listar_cibermedios(request):
    return HttpResponse("Listar Ciber...")


## 2.- Trabajar con ver y agregar Investigaciones
def agregar_investigaciones(request):
    return HttpResponse("Agregar Investigaciones")

def listar_investigaciones(request):
    return HttpResponse("Listar Investigaciones")



## 3.- Trabajar con ver y agregar Investigadores
def agregar_investigadores(request):
    return HttpResponse("Agregar Ivestigadores")

def listar_investigadores(request):
    return HttpResponse("Listar Ivestigadores")


# Se crea la vista para la plantilla HTML
def index(request):
    return render(request, 'index.html')