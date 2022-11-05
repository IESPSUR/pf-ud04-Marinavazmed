from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=30, unique=True, default='Sin Marca asignada')

class Producto(models.Model):
    nombre = models.CharField(max_length=30, null=True, unique=True)
    modelo = models.CharField(max_length=30, primary_key=True, unique=True)
    unidades = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    detalles = models.CharField(max_length=30, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT, verbose_name="Marca", null=True, default=0)


class Compra(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    importe = models.FloatField()
    nombre = models.ForeignKey('Producto', to_field='nombre', related_name='Nombre', on_delete=models.RESTRICT)

