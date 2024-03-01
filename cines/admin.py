from django.contrib import admin
from .models import Usuario, Pelicula, ActorPelicula, GeneroPelicula , Sala, FormatoSala, Ventana , Reserva, Funcion 

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "correo", "password"]

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height', 'path']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'pelicula']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'pelicula']

class SalaAdmin(admin.ModelAdmin):
    list_display = ['siglas', 'nombre', 'direccion', 'imagen', 'path', 'city']

class FormatoSalaAdmin(admin.ModelAdmin):
    list_display = ['form_name', 'sala']

class VentanaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'hora' , 'funcion_id']

class FuncionAdmin(admin.ModelAdmin):
    list_display = ['pelicula_id', 'sala_id']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['ventana', 'usuario']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(ActorPelicula, ActorAdmin)  
admin.site.register(GeneroPelicula, GeneroAdmin)  
admin.site.register(Sala, SalaAdmin)
admin.site.register(FormatoSala, FormatoSalaAdmin)
admin.site.register(Ventana, VentanaAdmin)
admin.site.register(Funcion, FuncionAdmin)
admin.site.register(Reserva, ReservaAdmin)


