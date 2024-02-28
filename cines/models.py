from django.db import models



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
        return self.username

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