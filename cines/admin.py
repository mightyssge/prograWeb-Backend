from django.contrib import admin
from .models import Pelicula, Actor, Genre, Reserva

#Se crean clases para que se vean bien en el admin
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height', 'path']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'pelicula']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'pelicula']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['r_name', 'r_apellido', 'r_codigo', 'r_cantidad', 'r_pelicula', 'r_horario']
