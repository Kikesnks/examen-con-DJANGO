from django.shortcuts import render
from plantilla import models as mod
# Create your views here.

def index(request):
    return render(request, 'index.html')

def plantilla(request):
    servicio = mod.ServicioPlantilla()
    lista = servicio.getPlantilla()
    informacion = {
        "plantilla": lista
    }
    print (lista)
    return render(request, 'plantilla.html', informacion)