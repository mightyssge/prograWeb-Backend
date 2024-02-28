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

    def __str__(self):
        return self.nombre



