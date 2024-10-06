from django.db import models

# Create your models here.

class Disco(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    imagen = models.ImageField(upload_to='discos/')


    def __Str__(self):
        return self.titulo
    

class Merch(models.Model):
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='merch/')

    def __str__(self):
        return self.nombre