from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Importa el modelo de la tabla Categoría.
from product.models import Category
from product.forms import ProductForm
from product.repositories.product import ProductRepository

# Almaceno en una variable la clase de Product que contiene todas las funciones para filtrar
# los productos y categorías.
repo = ProductRepository()

# Permite visualizar y enlistar todos los poductos.
def product_list(request):
    productos = repo.get_all()
    # Vínculo la función para ver todos los productos con el archivo html que posee 
    # el diseño de la página principal.
    return render(
        request,
        'products/list.html',
        # Cambio la variable que recorrerá el for por la variable que posee la tabla de productos, 
        dict(
            products=productos
        )
    )

# Muestra los detalles del producto seleccionado.
def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    # Vincula la funcíon para ver los detalles de un producto con el html que permite
    # visualizarlos mejor.
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

# Crear un nuevo producto.
def product_create(request):
    form = ProductForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            # Creo la nueva tabla con la función del repositorio de productos.
            producto_nuevo = repo.create(
                nombre = form.cleaned_data['name'],
                descripcion = form.cleaned_data['description'],
                precio = form.cleaned_data['price'],
                cantidades = form.cleaned_data['stock'],
                categoria = form.cleaned_data['category'],
            )
            return redirect('product_detail', producto_nuevo.id)

    # Variable almacenando repositorio de categorias.
    categorias = Category.objects.all()
    return render (
        request, 
        'products/create.html',
        {'form':form}
    )

@login_required(login_url='login')
def product_update(request, id):
    # Almaceno el producto que quiero modificar
    product = repo.get_by_id(id=id)

    # form = ProductForm(request.POST)


    # Almaceno todas las categorías de la tabla.
    categorias = Category.objects.all()

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')

        if id_category:
            category = Category.objects.get(id=id_category)
        else:
            category = None

        # Utilizo la función para actualizar del model para reemplazar las anteriores columnas
        # por las nuevas.
        repo.update(
            producto = product,
            nombre = name,
            precio = price,
            descripcion = description,
            cantidad = stock,
            categoria = category,
        )

        # Redirijo el resultado a la función de ver detalles para revisar las modificaciones
        return redirect('product_detail', product.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'products/update.html',
        dict(
            categories=categorias,
            product=product,
        )
    )

# Elimino un producto y vuelvo a rehacer toda la lista redirrigiendo la función a product_detail.
def product_delete(request, id):
    product = repo.get_by_id(id=id)
    repo.delete(producto=product)
    # Nombre del listado de productos en la url.
    return redirect('product_list')

def index_view(request):
    return render(
        request,
        'index/index.html',
    )