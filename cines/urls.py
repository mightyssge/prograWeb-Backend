from django.urls import path
from . import views

urlpatterns = [    
    path('guardar_reserva/', views.guardar_reserva, name='guardar_reserva'),
    path('ver_reservas/', views.verReservasEndpoint, name='ver_reservas'),
    path('importar-salas/', views.importar_salas, name='importar_salas'),

]
