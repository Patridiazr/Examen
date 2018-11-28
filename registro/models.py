from django.db import models

# Create your models here.

class Usuario():
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Producto():
    nombre = models.CharField(max_length = 100)
    costoP = models.IntegerField()
    costoR = models.IntegerField()
    tienda = models.CharField(max_length = 100)
    notas = models.CharField(max_length = 200)


