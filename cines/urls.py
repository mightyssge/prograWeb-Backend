from django.urls import path

from .views import *


urlpatterns = [
    path('users', usuariosEndpoint),
    path('createuser', createUsersEndpoint),
    path('createreserva', createReservasEndpoint),
    path('ver-peliculas',verPeliculasEndpoint),
    path('ver-pelicula',verPeliculaEndpoint),
    path('ver-funciones-pelicula',verFuncionesxPeliculaEndpoint),
    path('ver-funciones-sala',verFuncionesxSalaEndpoint),
    path('ver-usuarioid', verUsuarioID),
    path('ver-ventanaid', verVentanaID),
    path('ver-salas', verSalasEndpoint)
    
    
]
