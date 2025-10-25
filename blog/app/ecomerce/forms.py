from .models import *
from django import forms

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'#muestra todos los campos del modelo