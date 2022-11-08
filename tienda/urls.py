from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin', views.listado, name='listado'),
    path('tienda/editar', views.editar, name='editar'),
    path('tienda/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('tienda/add', views.add, name='add'),
    path('tienda/editar/<int:id>', views.editar, name='editar'),
]
