
from django.urls import path, include
from .views import *


urlpatterns = [
    #Paginas Inicio
    path('', home, name ="home"),
    #path('equipo/', equipo, name ="equipo"),
  
    #Pagina Futbolistas
    path('futbolistas/', FutbolistaList.as_view(), name ="futbolistas"),
    path('añadir_futbolista/', FutbolistaCreate.as_view(), name = "añadir_futbolista"),
    path('editar_futbolista/<int:pk>/', FutbolistaUpdate.as_view(), name = "editar_futbolista"),
    path('borrar_futbolista/<int:pk>/', FutbolistaDelete.as_view(), name = "borrar_futbolista"),
    path('buscar_futbolista', buscarFutbolista , name = "buscar_futbolista"),
    path('buscar/', buscar, name="buscar" ),


    #Pagina Entrenadores
    path('entrenador/', EntrenadorList.as_view(), name = "entrenador"),
    path('añadir_entrenador/', EntrenadorCreate.as_view(), name = "añadir_entrenador"),
    path('editar_entrenador/<int:pk>', EntrenadorUpdate.as_view(), name = "editar_entrenador"),
    path('borrar_entrenador/<int:pk>', EntrenadorDelete.as_view(), name = "borrar_entrenador"),
    path('buscar_entrenador', buscarEntrenador, name= "buscar_entrenador"),
    path('buscar_de_entrenador/', buscaDeEntrenador, name="buscar_e" ),

    #Pagina Equipos
    path('equipo/', EquipoList.as_view(), name = "equipo"),
    path('añadir_equipo/', EquipoCreate.as_view(), name = "añadir_equipo"),
    path('editar_equipo/<int:pk>', EquipoUpdate.as_view(), name = "editar_equipo"),
    path('borrar_equipo/<int:pk>', EquipoDelete.as_view(), name = "borrar_equipo"),
    path('buscar_equipo', buscarEquipo, name= "buscar_equipo"),
    path('buscar_de_equipo/', buscaDeEquipo, name="buscar_eq" ),

]