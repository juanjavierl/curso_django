from .models import Categoria, Producto
from django import forms

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio no puede ser negativo o cero.")
        return precio