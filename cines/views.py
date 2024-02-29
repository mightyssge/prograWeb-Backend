from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from .models import *
from django.db import IntegrityError

# Create your views here.

@csrf_exempt
def usuariosEndpoint(request):
    if request.method == 'POST':
        data = request.body
        user_data = json.loads(data)
        correo = user_data['correo']
        password = user_data['password']

        usuario_login = get_object_or_404(Usuario, correo=correo)
        
        if usuario_login.password != password:
            errorMsg = {"msg": "Contraseña incorrecta"}
            return HttpResponse(json.dumps(errorMsg), status=400)

        dataResponse = {
            "nombre": usuario_login.nombre,
            "apellidos": usuario_login.apellido,
            "correo": usuario_login.correo
        }
        return HttpResponse(json.dumps(dataResponse), status=200)

@csrf_exempt
def createUsersEndpoint(request):
    if request.method == 'POST':
        data = request.body
        user_data = json.loads(data)
        nombre = user_data['nombre']
        apellido = user_data['apellidos'] 
        correo = user_data['correo']
        password = user_data['password']

        try:
            new_user = Usuario(nombre=nombre, apellido=apellido, correo=correo, password=password)
            new_user.save()
        except IntegrityError:
            errorMsg = {
                "msg": "Correo ya registrado. Ingrese un correo diferente"
            }
            return HttpResponse(json.dumps(errorMsg), status=400)

        dataResponse = {
            "nombre": new_user.nombre,
            "apellidos": new_user.apellido,
            "correo": new_user.correo
        }
        return HttpResponse(json.dumps(dataResponse), status=200)

@csrf_exempt
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
            listaActoresQuerySet = ActorPelicula.objects.filter(pelicula_id = pelicula.pk)
            listaActores = [actor.name for actor in listaActoresQuerySet]

            listaGenerosQuerySet = GeneroPelicula.objects.filter(pelicula_id = pelicula.pk)
            listaGeneros = [genero.genre_name for genero in listaGenerosQuerySet]

            dataResponse.append({
                "id" : pelicula.pk,
                "title" : pelicula.title,
                "year" : pelicula.year,
                "extract" : pelicula.extract,
                "thumbnail" : pelicula.thumbnail,
                "path" : pelicula.path,
                "genres" : listaGeneros,
                "cast" : listaActores
            })

        return HttpResponse(json.dumps(dataResponse))

@csrf_exempt
def importar_peliculas(request):
    try:
        with open('static/data/peliculas.json', 'r') as file:
            data = json.load(file)
            
            for pelicula_data in data:
                # Crear la película
                pelicula = Pelicula.objects.create(
                    title=pelicula_data['title'],
                    year=pelicula_data['year'],
                    href=pelicula_data['href'],
                    extract=pelicula_data['extract'],
                    thumbnail=pelicula_data['thumbnail'],
                    thumbnail_width=pelicula_data['thumbnail_width'],
                    thumbnail_height=pelicula_data['thumbnail_height'],
                    path=pelicula_data['path']
                )
                
                # Crear los géneros de la película
                for genero in pelicula_data['genres']:
                    GeneroPelicula.objects.create(
                        pelicula=pelicula,
                        genero=genero
                    )
                
                # Crear los actores de la película
                for actor in pelicula_data['cast']:
                    ActorPelicula.objects.create(
                        pelicula=pelicula,
                        name=actor
                    )
                
        return JsonResponse({'message': 'Datos de películas importados correctamente.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

        

 







