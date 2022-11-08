from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    all_objects = Producto.objects.all().values()
    listaquery = list(all_objects)
    return render(request, 'tienda/listado.html', {'listaquery' : listaquery})

def add(request):
    form = FormularioProductos(request.POST)

    if form.is_valid():
        producto=Producto(id= form.cleaned_data['id'],
                          nombre= form.cleaned_data['nombre'],
                          modelo= form.cleaned_data['modelo'],
                          unidades= form.cleaned_data['unidades'],
                          precio = form.cleaned_data['precio'],
                          detalles = form.cleaned_data['detalles'],
                          marca = form.cleaned_data['marca'])

        producto.save()
        return render(request, 'tienda/confirmacion.html', {'producto' : producto})
    else:
        return render(request, 'tienda/add.html', {'form' : form})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listado')

#TODO
def editar(request):
    all_objects = Producto.objects.all().values()
    listaquery = list(all_objects)
    return render(request, 'tienda/listado.html', {'listaquery' : listaquery})