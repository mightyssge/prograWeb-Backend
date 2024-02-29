from django.urls import path

from .views import *
from .views import createUsersEndpoint
from .views import verPeliculasEndpoint
from .views import verPeliculaEndpoint
from .views import verFuncionesxPeliculaEndpoint


urlpatterns = [
    path('users', usuariosEndpoint),
    path('createuser', createUsersEndpoint),
    path('ver-peliculas',verPeliculasEndpoint),
    path('ver-pelicula',verPeliculaEndpoint),
    path('ver-funciones-pelicula',verFuncionesxPeliculaEndpoint)
    
    
]
