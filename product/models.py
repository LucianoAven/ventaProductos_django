from django.contrib import admin
from django.contrib.auth.models import User

# Método para convertir variables en columnas y agregarles especificaciones de una.
from django.db import models

# Creo las tablas de bases de datos y establezco las columnas que contendrán.
class Category(models.Model):
    # Crea la columna name de la tabla se establece que el contenido no puede tener más
    # de 200 caracteres.
    name = models.CharField(max_length=200)

    # Retorna la columna en formato string para que pueda ser visible en la página.    
    def __str__(self):
        return  self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    # Especifica que la columna puede ser nula.
    description = models.TextField(
        null=True,
        blank=True,
    )
    # Se declara que la columna es de caracter numérico.
    price = models.DecimalField(
        # Especifica que el número no puede tener más de diez dígitos.
        max_digits=10,
        decimal_places=2,
    )

    # Se vincula la columna con la tabla de Categorías. 
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products',
        # Habilita que la columna pueda ser nula.
        null=True,
    )

    # Establece que el stock sea 0 si no se especifica a la hora de enlistar un producto nuevo.
    stock = models.IntegerField(default=0)

    # Retorna el nombre del producto para hacerlo visible en la página principal.
    def __str__(self):
        return  self.name

    # Muestra un mensaje que tan valioso puede llegar a ser un producto por su precio.
    @admin.display(description="Rango de Precio")
    def rango_precios(self):
        if self.price > 1000000:
            return "ALTO"
        if 500000< self.price < 1000000:
            return "MEDIO"
        return "BAJO"


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f'Review by {self.author.username} for {self.product.name}'
    

class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='price_history'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.price} on {self.date}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    # image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.product.name}'

