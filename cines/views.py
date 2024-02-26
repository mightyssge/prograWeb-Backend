import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Actor, Genre, Pelicula, Reserva

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




    
    
@csrf_exempt
def guardar_reserva(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        reservaDict = json.loads(data)

        if '' in (reservaDict["nombre"], reservaDict["apellido"], reservaDict["codigo"], reservaDict["cantidad"], reservaDict["pelicula"], reservaDict["horario"]):
            errorDict = {
                "msg": "Debe ingresar todos los datos."
            }
            return HttpResponse(json.dumps(errorDict))
        
        reserva = Reserva(
            r_name=reservaDict["nombre"],
            r_apellido=reservaDict["apellido"],
            r_codigo=reservaDict["codigo"],
            r_cantidad=reservaDict["cantidad"],
            r_pelicula=reservaDict["pelicula"],
            r_horario=reservaDict["horario"]
        )
        reserva.save()
        
        respDict = {
            "msg": "Reserva guardada exitosamente."
        }
        
        return HttpResponse(json.dumps(respDict))