
from django.urls import include, path

from app.usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registroUser, name='registroUser'),
    path('salir/', views.salir, name='salir'),
]