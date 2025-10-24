from .models import Categoria
from django import forms

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']