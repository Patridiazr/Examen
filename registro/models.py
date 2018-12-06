from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)


class Tienda(models.Model):
    nombre = models.CharField(max_length = 100)
    sucursal = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    ciudad = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    aprobado = models.BooleanField(default=False)

class Lista(models.Model):
    nombre = models.CharField(max_length = 100)
    total_A = models.IntegerField(blank=True,null=True)
    total_C = models.IntegerField(blank=True,null=True)
    costo_P = models.IntegerField(blank=True,null=True)
    costo_R = models.IntegerField(blank=True,null=True)
    username = models.CharField(max_length = 100)

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    costoP = models.IntegerField(blank=True)
    costoR = models.IntegerField(blank=True)
    tienda = models.CharField(max_length = 100,blank=True)
    notas = models.CharField(max_length = 200,blank=True)
    nlista = models.CharField(max_length = 100)




