from django.contrib import admin
from .models import *

#Se crean clases para que se vean bien en el admin
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height', 'path']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'pelicula']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'pelicula']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "correo", "password"]
    
class SalaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion"]
    
class FuncionAdmin(admin.ModelAdmin):
    list_display = ["pelicula_id", "sala_id", "ventana_id"]

class ReservaAdmin(admin.ModelAdmin):
    list_display = ["usuario_id", "funcion_id", "cantidad"]
    
class ReservaAdmin2(admin.ModelAdmin):
    list_display = ['r_name', 'r_apellido', 'r_codigo', 'r_cantidad', 'r_pelicula', 'r_horario']
    

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(ActorPelicula, ActorAdmin)
admin.site.register(GeneroPelicula, GeneroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Funcion, FuncionAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Reserva2, ReservaAdmin2)