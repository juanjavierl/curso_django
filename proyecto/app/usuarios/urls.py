
from django.urls import path

from app.usuarios import views

urlpatterns = [
    path('', views.home, name='home')
]