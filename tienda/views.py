from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UserCreationForm, FormularioCompra, FormularioBusqueda
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.db.models import Sum
from django.db import transaction
from django.forms import ModelForm

# Create your views here.
#INDEX
def welcome(request):
    return render(request, 'tienda/index.html', {})



#LISTADO:
def listado(request):
    """
    Vista de listado de productos. Muestra CRUD si auth
    """
    all_objects = Producto.objects.all().values()
    listaquery = list(all_objects)
    return render(request, 'tienda/listado.html', {'listaquery' : listaquery})
#---------END LISTADO




#PROCESO (VISTA Y DETALLE) DE COMPRA:
def listadocompra(request):
    """
    Vista de listado de COMPRA de productos.
    """
    listaquery = list(Producto.objects.all().values())
    return render(request, 'tienda/listadocompra.html', {'listaquery' : listaquery})

@transaction.atomic
def compraid(request, id=id):
    """
    Vista de DETALLE de compra de producto.
    """
    producto = get_object_or_404(Producto, id=id)
    form = FormularioCompra(request.POST)

    if request.method == "POST":
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            if(producto.unidades > cantidad):
                producto.unidades = producto.unidades - cantidad
                producto.save()
                #Registramos la compra en la bbdd:
                if request.user.is_authenticated:
                    username = request.user.username
                else:
                    username = None
                compra = Compra(usuario=username, fecha=datetime.now().date() ,unidades=cantidad, importe=(cantidad*producto.precio), nombre=producto)
                compra.save()
                return redirect('listadocompra')
            else:
                raise forms.ValidationError('Has introducido demasiadas unidades')

    return render(request, 'tienda/compraitem.html', {'producto': producto, 'unidades':producto.unidades, 'form':form, 'id':id})
#----------FIN VISTA DETALLE Y COMPRA




#SECCIÓN INFORME PRODUCTOS
def informe(request):
    all_marcas = list(Marca.objects.all().values())
    all_compras = list(Compra.objects.all().values('usuario').distinct())

    top_ten = Compra.objects.values('nombre').annotate(total_ventas=Sum('unidades')).order_by('-total_ventas')[:10]
    top_ten_usuario = Compra.objects.values('usuario').annotate(total_compra_usuario=Sum('importe')).order_by('-total_compra_usuario')[:10]

    return render(request, 'tienda/informe.html', {'listamarcas':all_marcas, 'listacompras' : all_compras, 'top_ten':top_ten, 'top_ten_usuario':top_ten_usuario})

def listado_marcas(request, nombre):
    listaproductos = Producto.objects.filter(marca=nombre).values()
    return render(request, 'tienda/listado.html', {'listaquery': listaproductos})

def listado_usuario(request, nombre):
    listacompras = Compra.objects.filter(usuario=nombre).values()
    return render(request, 'tienda/listado.html', {'listaquery' : listacompras})

#--------FIN SECCIÓN INFORME




#CRUD
def add(request):
    """
    CRUD añadir producto nuevo
    """
    form = FormularioProductos(request.POST)

    if form.is_valid():
        producto = Producto(nombre= form.cleaned_data['nombre'],
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
    """CRUD eliminar producto. Descomentar las líneas comentadas para eliminar la proteccion de fk"""
    producto = get_object_or_404(Producto, id=id)
#    compra = get_object_or_404(Compra, nombre=producto)
    if request.method == 'POST':
#        compra.delete()
        producto.delete()
        return redirect('listado')

def editar(request, id):
    """CRUD editar producto"""
    producto = get_object_or_404(Producto, id=id)
    form = FormularioProductos(request.POST, instance=producto)
    #Es necesario el parámetro instance cuando creamos un formulario SOBRE un producto ya existente
    #Así rellenará automáticamente sus campos con los datos ya preestablecidos
    if form.is_valid():
#            producto.id = id
            producto.nombre = form.cleaned_data['nombre']
            producto.modelo = form.cleaned_data['modelo']
            producto.unidades = form.cleaned_data['unidades']
            producto.precio = form.cleaned_data['precio']
            producto.detalles = form.cleaned_data['detalles']
            producto.marca = form.cleaned_data['marca']
            producto.save()
            return redirect('listado')
    else:
        return render(request, 'tienda/editar.html', {'form' : form})
#-------------FIN CRUD



#AUTH
def registro(request):
    """Registro de usuario nuevo"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listado')
        else:
            messages.error(request, "Formulario no válido")
    form = UserCreationForm()
    return render(request, "tienda/registro.html", {"register_form":form})

def login_usr(request):
    """Logeo de usuario ya creado"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("listado")
            else:
                messages.error(request, "Error en el inicio de sesión")
        else:
            messages.error(request, "Fallo en el inicio de sesión")
    form = AuthenticationForm()
    return render(request, "tienda/login.html", {'login_form':form})

def logout_usr(request):
    """Cierre de sesión de usuario"""
    logout(request)
    return redirect("listado")
#------------FIN AUTH



#FORMULARIO DE BÚSQUEDA
def busqueda(request):
    form = FormularioBusqueda(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                nombreprod = form.cleaned_data['nombre']
                productos = Producto.objects.filter(nombre__contains=nombreprod).values()
                listaquery = list(productos)
                return render(request, 'tienda/listadocompra.html', {'listaquery': listaquery})
            except Producto.DoesNotExist:
                return HttpResponse("Producto no encontrado")
    return render(request, 'tienda/busqueda.html', {'form':form})
#----------------FIN BUSQUEDA



