from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from .models import *
from django.db import IntegrityError

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
    

def verReservasEndpoint(request):
    if request.method == "GET":
        codigo = request.GET.get("codigo")

        if not codigo:
            return JsonResponse({"msg": "Se requiere el código para buscar las reservas."}, status=400)

        reservas = Reserva.objects.filter(r_codigo=codigo)

        dataResponse = []
        for reserva in reservas:
            dataResponse.append({
                "id": reserva.pk,
                "nombre": reserva.r_name,
                "apellido": reserva.r_apellido,
                "codigo": reserva.r_codigo,
                "cantidad": reserva.r_cantidad,
                "pelicula": reserva.r_pelicula,
                "horario": reserva.r_horario
            })

        return JsonResponse(dataResponse, safe=False)

    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)

    
@csrf_exempt
def importar_salas(request):
    try:
        with open('static/data/salas.json', 'r') as file:
            data = json.load(file)

            for sala_data in data:
                sala = Sala.objects.create(
                    siglas=sala_data['siglas'],
                    nombre=sala_data['name'],
                    direccion=sala_data['address'],
                    imagen=sala_data['img'],
                    path=sala_data['path']
                )

        return JsonResponse({'message': 'Datos de salas importados correctamente.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)