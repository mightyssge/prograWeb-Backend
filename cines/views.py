from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Pelicula, Actor, Genre


#PATH : /cines/verPeliculas

def verPeliculasEndpoint(request):
    if request.method == "GET":
        # Es una peticion de tipo GET
        titleFilter = request.GET.get("title") # Obtenemos query parameter nombre

        if titleFilter == "" :
            # No hay que filtrar nada
            listaPeliculaFiltrada = Pelicula.objects.all()
        else:
            # Si ha enviado filtro
            listaPeliculaFiltrada = Pelicula.objects.filter(title__contains=titleFilter)

        dataResponse = []
        for pelicula in listaPeliculaFiltrada:

            #dos relaciones one to many para genero y actor
            listaActoresQuerySet = Actor.objects.filter(pelicula_id = pelicula.pk)
            listaActores = list(listaActoresQuerySet.values())

            listaGenerosQuerySet = Genre.objects.filter(pelicula_id = pelicula.pk)
            listaGeneros = list(listaGenerosQuerySet.values())

            dataResponse.append({
                "id" : pelicula.pk,
                "title" : pelicula.title,
                "year" : pelicula.year,
                "cast" : listaActores,
                "genres" : listaGeneros,
                "extract" : pelicula.extract,
                "thumbnail" : pelicula.thumbnail,
                "path" : pelicula.path
            })

        return HttpResponse(json.dumps(dataResponse))
