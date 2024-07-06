# Miniblog Django.

Este es un proyecto de prueba para un sitio web donde los usuarios puedan ver y comprar productos en venta
presentados en la ventana principal. Además de poder ver los detalles de cada producto (cantidad, precio, tipo
de producto, etc)

## Características

- Inicio de sesion.
- Lista de productos.
- Caracteristicas de cada producto (precio, cantidad, categoría, descripción, etc).
- Lista de reseñas de cada producto y opción para publicar una reseña.
- Opciones para filtrar los productos por categorías

## Requisitos

- Python 3.x
- Django 5.x

## Instalación

1. Hacer un clon del repositorio de github:

    ```sh
    git clone: git@github.com:LucianoAven/ventaProductos_django.git
    ```

2. Crear un entorno virtual:

    ```sh
    python -m venv env
    ```

3. Crear un entorno virtual:

    ```sh
    source env/bin/activate
    ```

4. Instalar las dependencias necesarias para su funcionamiento:

    ```sh
    pip install -r requirements.txt
    ```

5. Generar las migraciones:

    ```sh
    python manage.py migrate
    ```

6. Ejecuta el sitio web de prueba:

    ```sh
    python manage.py runserver
    ```

7. Acceder a la pagina escribiendo el siguiente enlace en la barra de navegacion:

    ```
    http://127.0.0.1:8000/
     ```

## Contribuir

1. Hacer un fork del repositorio
2. Crear una nueva rama. Ejemplo: git checkout -b nueva-rama.
3. Genera un commit una vez realizada todas las modificaciones. Ejemplo: git commit -m 'Aniade descripcion a nueva rama'.
4.  Enviar la rama al repositorio en github. Ejemplo: git push origin nueva-rama.
5. Crea un nuevo Pull Request

## Hecho por:

-`Luciano Ciro Avendano.`