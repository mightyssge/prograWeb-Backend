from django.db import models

# Create your models here.

class Pelicula(models.Model):
    #relaciones de uno a muchos en la pelicula
        #para el cast , una pelicula tiene varios actores
        #para los generos, una pelicula tiene varios generos
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

class Actor(models.Model):
    name = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre_name


class Reserva(models.Model):
    r_name = models.CharField(max_length=100)
    r_apellido = models.CharField(max_length=100)
    r_codigo = models.CharField(max_length=100)
    r_cantidad = models.IntegerField()  
    r_pelicula = models.CharField(max_length=100)
    r_horario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.r_name
    
class Sala(models.Model):
    siglas = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    imagen = models.TextField()
    path = models.TextField()

    def __str__(self):
        return self.nombre
    