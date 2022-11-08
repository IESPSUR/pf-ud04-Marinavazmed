from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    all_objects = Producto.objects.all().values()
    listaquery = list(all_objects)
    return render(request, 'tienda/listado.html', {'listaquery' : listaquery})

def editar(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    return render(request, 'tienda/editar.html', {})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
    return redirect('listado')