from django.db import models
from django.forms import ModelForm, forms
from django.core.validators import MinValueValidator
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=30, default='Sin Marca asignada', primary_key=True, unique=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    modelo = models.CharField(max_length=30)
    unidades = models.PositiveIntegerField(default=1)
    precio = models.FloatField(validators=[MinValueValidator(0.0)])
    detalles = models.CharField(max_length=30, blank=True, default="Sin detalles")
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre



class Compra(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT, to_field='username', default=False)
    fecha = models.DateTimeField()
    unidades = models.IntegerField(validators=[MinValueValidator(0.0)])
    importe = models.FloatField(validators=[MinValueValidator(0.0)])
    nombre = models.CharField(max_length=30)
#    nombre = models.ForeignKey('Producto', to_field='nombre', related_name='Nombre', on_delete=models.RESTRICT) #Para restricciones de borrado de informe

class FormularioProductos(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
