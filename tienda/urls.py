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
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usr, name='login_usr'),
    path('logout/', views.logout_usr, name='logout_usr'),
    path('listadocompra/', views.listadocompra, name='listadocompra'),
    path('compraid/<int:id>', views.compraid, name='compraid'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('informe/', views.informe, name='informe'),
    path('listado_marcas/<str:nombre>', views.listado_marcas, name='listado_marcas'),
    path('listado_usuario/<str:nombre>', views.listado_usuario, name='listado_usuario'),
]
