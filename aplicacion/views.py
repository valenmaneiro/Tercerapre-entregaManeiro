from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def futbolistas(request):
    return render(request, "aplicacion/futbolistas.html")

def equipo(request):
    return render(request, "aplicacion/equipo.html")

def entrenador(request):
    return render(request, "aplicacion/entrenador.html")

#Funciones para vista de Modelos
def futbolistas(request):
    ctx = {'futbolistas': Futbolista.objects.all()}
    return render(request, "aplicacion/futbolistas.html", ctx)
def entrenadores(request):
    ctx= {'entrenadores': Entrenador.objects.all()}
    return render (request, 'aplicacion/entrenadores.html', ctx)

#Funciones para Futbolistas
def buscarFutbolista(request):
    return render(request, "aplicacion/buscar_futbolista.html")

def buscar(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        futbolista = Futbolista.objects.filter(nombreCompleto=nombre)
        if futbolista:
            contexto = {"futbolista": futbolista, 'descripcion': f'Futbolista buscado: "{nombre}"'}
        else:
            contexto = {
                'descripcion': f"No se encontro un futbolista con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/futbolista.html", contexto)

# Vista de lista, update, create y delete de Futbolistas
class FutbolistaList(ListView):
    model = Futbolista
class FutbolistaCreate(CreateView):
    model = Futbolista
    fields = ['nombreCompleto', 'nacionalidad', 'equipo', 'dorsal']
    success_url = reverse_lazy('futbolistas')
class FutbolistaUpdate(UpdateView):
    model = Futbolista
    fields = ['nombreCompleto', 'nacionalidad', 'equipo', 'dorsal']
    success_url = reverse_lazy('futbolistas')
class FutbolistaDelete(DeleteView):
    model = Futbolista
    success_url = reverse_lazy('futbolistas')

#Vista de lista, update, create y delete de Entrenadores
class EntrenadorList(ListView):
    model = Entrenador
class EntrenadorCreate(CreateView):
    model = Entrenador
    fields = ['nombreCompleto', 'nacionalidad', 'equipo']
    success_url = reverse_lazy('entrenador')
class EntrenadorUpdate(UpdateView):
    model = Entrenador
    fields = ['nombreCompleto', 'nacionalidad', 'equipo']
    success_url = reverse_lazy('entrenador')
class EntrenadorDelete(DeleteView):
    model = Entrenador
    success_url = reverse_lazy('entrenador')

#Vista de lista, update, create y delete de Equipos
class EquipoList(ListView):
    model = Equipo
class EquipoCreate(CreateView):
    model = Equipo
    fields = ['nombre', 'pais', 'nroSocios', 'fechaFundacion']
    success_url = reverse_lazy('equipo')
class EquipoUpdate(UpdateView):
    model = Equipo
    fields = ['nombre', 'pais', 'nroSocios', 'fechaFundacion']
    success_url = reverse_lazy('equipo')
class EquipoDelete(DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipo')

#Funciones Entrenadores
def buscarEntrenador(request):
    return render(request, "aplicacion/buscar_entrenador.html")

def buscaDeEntrenador(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        entrenador = Entrenador.objects.filter(nombreCompleto=nombre)
        if entrenador:
            contexto = {"entrenador": entrenador, 'descripcion': f'Entrenador buscado: "{nombre}"'}
        else:
            contexto = {
                'descripcion': f"No se encontro un Entrenador con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/entrenador.html", contexto)

#Funciones Equipos
def buscarEquipo(request):
    return render(request, "aplicacion/buscar_equipo.html")

def buscaDeEquipo(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        equipo = Equipo.objects.filter(nombre=nombre)
        if equipo:
            contexto = {"equipo": equipo, 'descripcion': f'Equipo buscado: "{nombre}"'}
        else:
            contexto = {
                'descripcion': f"No se encontro un Equipo con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/equipo.html", contexto)
