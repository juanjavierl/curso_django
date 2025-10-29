from django.urls import include, path
from app.ecomerce import views

urlpatterns = [
    path('ver_categorias/', views.ver_categorias, name='ver_categorias'),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('filtrar_productos/<int:id_categoria>/', views.filtrar_productos, name='filtrar_productos'),
]