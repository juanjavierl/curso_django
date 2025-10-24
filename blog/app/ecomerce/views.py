from django.shortcuts import redirect, render
from .models import Categoria
from .forms import FormCategoria
# Create your views here.
def ver_categorias(request):
    """
    Select * from Categoria;
    """
    categorias = Categoria.objects.all()
    print(categorias)
    return render(request, 'ver_categorias.html', {'categorias': categorias})

def nueva_categoria(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_categorias')
    else:
        form =FormCategoria()
    return render(request, 'nueva_categoria.html', {'form': form})