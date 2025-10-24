from django.urls import include, path
from app.ecomerce import views

urlpatterns = [
    path('ver_categorias/', views.ver_categorias, name='ver_categorias'),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
]