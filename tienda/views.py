from django.shortcuts import render
from .models import *

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    all_objects = Producto.objects.all().values('nombre')
    context = {'all_objects': all_objects}
    return render(request, 'tienda/listado.html', context)