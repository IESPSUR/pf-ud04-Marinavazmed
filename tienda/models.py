from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    modelo = models.CharField(max_length=30, primary_key=True)
    unidades = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    detalles = models.CharField(max_length=30, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)


class Compra(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    importe = models.FloatField()

