from django.shortcuts import redirect, render
from .models import Categoria, Producto
from .forms import FormCategoria, FormProducto
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

def ver_productos(request):
    """
    Select * from Producto;
    """
    productos = Producto.objects.all()
    return render(request, 'ver_productos.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = FormProducto()
    return render(request, 'registrar_producto.html', {'form': form})

def editar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)#select * from Producto where id=id_producto;
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = FormProducto(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)#select * from Producto where id=id_producto;
    producto.delete()#delete from Producto where id=id_producto;
    return redirect('ver_productos')
