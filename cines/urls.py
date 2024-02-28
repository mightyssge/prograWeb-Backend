from django.urls import path

from .views import *
from .views import createUsersEndpoint


urlpatterns = [
    path('users', usuariosEndpoint),
    path('createuser', createUsersEndpoint),
    path('importar-peliculas/', importar_peliculas, name='importar_peliculas'),
    path('ver-peliculas/',verPeliculasEndpoint)
    
    
]
