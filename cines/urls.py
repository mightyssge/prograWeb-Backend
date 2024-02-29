from django.urls import path

from .views import *


urlpatterns = [    

    path('importar_salas/', importar_salas, name='importar_salas'),
    path('guardar_reserva/', guardar_reserva, name='guardar_reserva'),
    #path('ver_reservas/', views.verReservasEndpoint, name='ver_reservas'),
    #path('ver_salas/', views.ver_salas, name='ver_salas'),
    path('ver-salas',verSalasEndpoint),

]