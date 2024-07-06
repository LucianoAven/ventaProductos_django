from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository
from product.repositories.product import ProductRepository

# Visualiza todas las categorías en la página.
def category_list(request):
    category_repository = CategoryRepository()
    categorias = category_repository.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

# Muestra los detalles de una categoría en específico
def category_detail(request, id:int):

    category_repository = CategoryRepository()
    product_repository = ProductRepository()

    categoria = category_repository.get_by_id(id)
    productos = product_repository.filter_by_category(categoria)

    return render(
        request,
        'categories/detail.html',
        dict (
            category = categoria,
            products = productos,
        )
    )

# Permite crear una nueva categoría
def category_create(request):

    category_repository = CategoryRepository()

    if request.method == "POST":

        # Habilito al usuario agregar una nueva categoría desde la parte externa del sitio web.
        nombre = request.POST.get('name')

        # Creo la nueva categoría con su respectiva función del repositorio de categorías.
        category_repository.create(
            nombre = nombre,
        )

        # Redirecciona a la función de detalles para ver el resultado de la nueva categoría.
        return redirect('category_list')

    # Vinculo la función con el archivo que permite añadir categorías desde el sitio web html.
    return render(
        request,
        'categories/create.html',
    )

# Actualiza el nombre de una categoría.
def category_update(request, id:int):

    category_repository = CategoryRepository()

    # Almacena la categoría que quiero modificar
    category = category_repository.get_by_id(id)

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')

        # Utilizo la función para actualizar del model para reemplazar las anteriores columnas
        # por las nuevas.
        category_repository.update(
            categoria = category,
            nombre = name,
        )

        # Redirijo el resultado a la función de ver detalles para revisar las modificaciones
        return redirect('category_detail', category.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'categories/update.html',
        dict(
            category=category,
        )
    )
