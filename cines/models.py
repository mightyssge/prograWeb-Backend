from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)  # Cambiado de "apellido" a "apellidos"
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    class Meta:
        app_label='cines'


class Pelicula(models.Model):
    title = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    year = models.IntegerField()
    href = models.CharField(max_length=200)
    extract = models.TextField()
    thumbnail = models.URLField()
    thumbnail_width = models.FloatField()
    thumbnail_height = models.FloatField()
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ActorPelicula(models.Model):  # Cambiado el nombre de la clase
    name = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GeneroPelicula(models.Model):  # Cambiado el nombre de la clase
    genre_name = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre_name


class Sala(models.Model):
    siglas = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    imagen = models.URLField()
    path = models.TextField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class FormatoSala(models.Model):
    form_name = models.CharField(max_length=50)
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.form_name

class Ventana(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    funcion_id = models.ForeignKey('Funcion', on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return f'{str(self.fecha)} | {str(self.hora)}'


class Funcion(models.Model):
    pelicula_id = models.ForeignKey(Pelicula, on_delete=models.SET_NULL, null=True)
    sala_id = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.pk)

class Reserva(models.Model):
    ventana = models.ForeignKey (Ventana, on_delete=models.SET_NULL, null=True) #falta actualizar cambios
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    def __str__(self):
        return str(self.pk)

