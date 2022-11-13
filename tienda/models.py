from django.db import models
from django.forms import ModelForm, forms


# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=30, default='Sin Marca asignada', primary_key=True, unique=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
#    id = models.CharField(max_length=30, primary_key=True, unique=True)
    nombre = models.CharField('Nombre', max_length=30, null=True, unique=True)
    modelo = models.CharField('Modelo', max_length=30)
    unidades = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    detalles = models.CharField(max_length=30, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT, verbose_name="Marca", null=True, default=0)

    def __str__(self):
        return self.nombre



class Compra(models.Model):
    usuario = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    unidades = models.IntegerField()
    importe = models.FloatField()
    nombre = models.ForeignKey('Producto', to_field='nombre', related_name='Nombre', on_delete=models.RESTRICT)

class FormularioProductos(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


