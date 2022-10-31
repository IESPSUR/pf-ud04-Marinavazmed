from django.contrib import admin
from django.db import models
# Register your models here.
from .models import *

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
