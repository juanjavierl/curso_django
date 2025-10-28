from django.contrib import admin
from .models import * # Importa todos los modelos del archivo models.py
admin.site.register(Categoria)
admin.site.register(Producto)