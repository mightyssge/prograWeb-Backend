from django.contrib import admin
from .models import Usuario, Pelicula, ActorPelicula, GeneroPelicula

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "correo", "password"]

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height', 'path']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'pelicula']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'pelicula']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(ActorPelicula, ActorAdmin)  
admin.site.register(GeneroPelicula, GeneroAdmin)  
