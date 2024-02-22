from django.contrib import admin
from .models import Pelicula, Actor, Genre

#Se crean clases para que se vean bien en el admin
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height', 'path']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'pelicula']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'pelicula']


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)