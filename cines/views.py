from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from .models import *
from django.db import IntegrityError

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
def verVentanaID(request):
    if request.method == "GET":
        fecha = request.GET.get("nombre")
        hora = request.GET.get("apellido")

        if not fecha or not hora:
            errorDict = {
                "msg": "mala hora"
            }
            return JsonResponse(errorDict, status=400)

        try:
            ventana = Ventana.objects.get(fecha=fecha, hora=hora)
        except Usuario.DoesNotExist:
            errorDict = {
                "msg": "no existe"
            }
            return JsonResponse(errorDict, status=404)

        respDict = {
            "id": ventana.id
        }
        return JsonResponse(respDict)

@csrf_exempt
def createReservasEndpoint(request):
    if request.method == 'POST':
        data = request.body
        user_data = json.loads(data)
        
        try:
            ventana = Ventana.objects.get(pk=user_data['ventana'])
            usuario = Usuario.objects.get(pk=user_data['usuario'])
            cantidad = user_data['cantidad']
            
            new_reserva = Reserva(ventana=ventana, usuario=usuario, cantidad=cantidad)
            new_reserva.save()
            
            dataResponse = {
                "ventana": new_reserva.ventana.id,
                "usuario": new_reserva.usuario.id,
                "cantidad": new_reserva.cantidad
            }
            return HttpResponse(json.dumps(dataResponse), status=200)
        except ObjectDoesNotExist:
            errorMsg = {
                "msg": "Ventana o Usuario no encontrado"
            }
            return HttpResponse(json.dumps(errorMsg), status=404)
        except IntegrityError:
            errorMsg = {
                "msg": "Error de integridad al guardar la reserva"
            }
            return HttpResponse(json.dumps(errorMsg), status=400)
        
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
            listaPeliculaFiltrada = Pelicula.objects.filter(title__icontains=titleFilter)

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

def verPeliculaEndpoint(request):
    if request.method == "GET":
        peliculapath = request.GET.get("path")

        if peliculapath is None:
            errorDict = {
                "msg": "Debe proporcionar un path de película"
            }
            return JsonResponse(errorDict, status=400)

        try:
            pelicula = Pelicula.objects.get(path=peliculapath)
        except Pelicula.DoesNotExist:
            errorDict = {
                "msg": "La película con el path proporcionado no existe"
            }
            return JsonResponse(errorDict, status=404)

        # Obtener los géneros asociados a la película
        generos_pelicula = GeneroPelicula.objects.filter(pelicula=pelicula)
        actores = ActorPelicula.objects.filter(pelicula=pelicula)

        # Obtener los nombres de los géneros
        nombres_generos = [genero.genre_name for genero in generos_pelicula]
        lista_actores = [actor.name for actor in actores]

       

        respDict = {
            "id": pelicula.pk,
            "nombre": pelicula.title,
            "anho": pelicula.year,
            "thumbnail": pelicula.thumbnail,
            "extract": pelicula.extract,
            "path": pelicula.path,
            "generos": nombres_generos,  # Añadir los nombres de los géneros a la respuesta
            "actores": lista_actores,
        }
        return JsonResponse(respDict)
@csrf_exempt 
def verUsuarioID(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")

        if not nombre or not apellido:
            errorDict = {
                "msg": "Debe proporcionar un nombre y un apellido"
            }
            return JsonResponse(errorDict, status=400)

        try:
            usuario = Usuario.objects.get(nombre=nombre, apellido=apellido)
        except Usuario.DoesNotExist:
            errorDict = {
                "msg": "El usuario con el nombre y apellido proporcionados no existe"
            }
            return JsonResponse(errorDict, status=404)

        respDict = {
            "id": usuario.id
        }
        return JsonResponse(respDict)
@csrf_exempt
def verSalasEndpoint(request):
    if request.method == "GET":
        pathFilter = request.GET.get("path")
        
        if pathFilter == "":
            listaSalaFiltrada = Sala.objects.all()
        else:
            listaSalaFiltrada = Sala.objects.filter(path__icontains = pathFilter)
        
        dataResponse = []
        for sala in listaSalaFiltrada:
            listaFormatosQuerySet = FormatoSala.objects.filter(sala_id = sala.pk)
            listaFormatos = [formato.form_name for  formato in listaFormatosQuerySet]
            
            dataResponse.append({
                "id" :  sala.pk,
                "nombre" : sala.nombre,
                "siglas" : sala.siglas,
                "direccion" : sala.direccion,
                "imagen" : sala.imagen,
                "path" : sala.path,
                "city" : sala.city,
                "formato" : listaFormatos
            })
        return HttpResponse(json.dumps(dataResponse))

def verFuncionesxPeliculaEndpoint (request):
    if request.method == "GET":
        id_pelicula = request.GET.get("idpelicula")

        if id_pelicula == "":
            errorDict = {
                "msg": "Debe proporcionar un id de película"
            }
            return JsonResponse(errorDict, status=400)
        else:
            # Si ha enviado filtro
            listaFunciones = Funcion.objects.filter(pelicula_id=id_pelicula)


        dataResponse = []
        for funcion in listaFunciones:
            
            #obtener los datos de la ventana
            listaventanas = Ventana.objects.filter(funcion_id=funcion.pk)
            ventanas = [f'{str(ventana.fecha)} | {str(ventana.hora)}' for ventana in listaventanas]

            dataResponse.append({
                "id" : funcion.pk,  
                "sala" : funcion.sala_id.pk, #necesito el nombre de la sala , sus siglas , su address 
                "salasiglas" : funcion.sala_id.siglas,
                "salanombre" : funcion.sala_id.nombre,
                "salaadress" : funcion.sala_id.direccion,
                "ventanas" : ventanas
            })

        return HttpResponse(json.dumps(dataResponse))
        
    

def verFuncionesxSalaEndpoint (request):
    if request.method == "GET":
        id_sala = request.GET.get("idsala")


        if id_sala == "" :
            errorDict = {
                "msg": "Debe proporcionar un id de sala"
            }
            return JsonResponse(errorDict, status=400)
        else:
            # Si ha enviado filtro
            listaFunciones = Funcion.objects.filter(sala_id=id_sala)

        dataResponse = []
        

        for funcion in listaFunciones:
            listaventanas = Ventana.objects.filter(funcion_id=funcion.pk)
            ventanas = [f'{str(ventana.fecha)} | {str(ventana.hora)}' for ventana in listaventanas]
            dataResponse.append({
                "id" : funcion.pk,  
                "pelicula" : funcion.pelicula_id.pk, #necesito el nombre de la sala , sus siglas , su address 
                "peliculasiglas" : funcion.pelicula_id.siglas,
                "peliculanombre" : funcion.pelicula_id.title,
                "peliculaextract" : funcion.pelicula_id.extract,
                "ventanas" : ventanas
            })

        return HttpResponse(json.dumps(dataResponse))
    

 