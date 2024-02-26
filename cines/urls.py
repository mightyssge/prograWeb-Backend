from django.urls import path
from . import views

urlpatterns = [    
    path('guardar_reserva/', views.guardar_reserva, name='guardar_reserva'),
]
