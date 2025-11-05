from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Categoria, Producto
from .forms import *

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
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'ver_productos.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto registrado exitosamente.")
            return redirect('ver_productos')
        else:
            messages.error(request, "Error al registrar el producto. Por favor, verifica los datos ingresados.")
    else:
        form = FormProducto()
    return render(request, 'registrar_producto.html', {'form': form})

def editar_producto(request, id_producto):
    """
    select  from Producto where id=id_producto
    """
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = FormProducto(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id_producto):
    """
    select * from Producto where id=id_producto
    """
    if request.method == 'POST':
        producto = Producto.objects.get(id=id_producto)
        producto.delete()
        return redirect('ver_productos')
    else:
        producto = Producto.objects.get(id=id_producto)
        return render(request, 'eliminar_producto.html', {'producto': producto})
    
def filtrar_productos(request, id_categoria):
    """
    select * from Producto where categoria_id=id_categoria
    """
    productos = Producto.objects.filter(categoria_id=id_categoria)
    print(productos)
    return render(request, 'ver_productos.html', {'productos': productos})

def catalogo(request):
    productos = Producto.objects.all().order_by('-id')
    cart = request.session.get('cart', {})# Obtener el carrito de la sesión
    total_productos = sum(item.get('cantidad', 0) for item in cart.values())  # Sumar las cantidades de productos en el carrito
    return render(request, 'catalogo.html', {'productos': productos, 'total_productos': total_productos})

def agregar_al_carrito(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Producto.objects.get(id=product_id)

        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            cart[str(product_id)]['cantidad'] += 1
        else:
            cart[str(product_id)] = {
                'nombre': product.nombre,
                'precio': float(product.precio),
                'cantidad': 1,
                'imagen': product.imagen.url if product.imagen else '',
            }
        print(cart)
        request.session['cart'] = cart
        request.session.modified = True

        total_items = sum(item['cantidad'] for item in cart.values())
        message = f"✅ Producto '{product.nombre}' agregado al carrito."
        return JsonResponse({'success': True, 'total_items': total_items, 'message': message})

    return JsonResponse({'success': False}, status=400)
        