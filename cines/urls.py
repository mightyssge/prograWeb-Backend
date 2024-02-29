from django.urls import path

from .views import *


urlpatterns = [
    path('users', usuariosEndpoint),
    path('createuser', createUsersEndpoint),
    path('ver-peliculas',verPeliculasEndpoint),
    path('ver-pelicula',verPeliculaEndpoint),
    path('ver-funciones-pelicula',verFuncionesxPeliculaEndpoint),
    path('ver-funciones-sala',verFuncionesxSalaEndpoint),
    path('ver-salas', verSalasEndpoint)
    
    
]