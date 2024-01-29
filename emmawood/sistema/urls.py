from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('productos', views.productos, name="productos"),
    path('productos/crear', views.crear, name="crear"),
    path('productos/editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('editar/<int:id>', views.editar, name='editar'),
]