# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de Productos y Categorías.
from product.models import Category, Product


#logger = logging.getLogger(__name__)

# Funciones para las distintas acciones de la página.
class ProductRepository:

    # Visualizar todos los productos almacenados.
    def get_all(self) -> List[Product]:
        return Product.objects.all()

    # Buscar un producto por su id.
    def filter_by_id(self, id: int) -> Optional[Product]:
        # Retorna el producto con la id espicificada en la función.
        return Product.objects.filter(id=id).first()

    # Muestra el producto con la id especificada.    
    def get_by_id(self, id: int) -> Optional[Product]:
        # Envía un componente vacío en caso de no haber un producto con la id ingresada.
        try:
            product = Product.objects.get(id=id)
        except:
            product = None
        return product

    # Filtra todos los productos cuyo valor se encuentre entre los precios especificados.
    def get_product_on_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Product]:
        #products = Product.objects.filter(
        #    price__gt=min_price,
        #    price__lt=max_price,
        #)
        products = Product.objects.filter(
            price__range=(min_price, max_price)
        )

        return products

    # Crea un nuevo producto y especifica sus características.
    def create(
        self,
        nombre: str,
        precio: float,
        descripcion: Optional[str] = None,
        cantidades: Optional[int] = 0,
        categoria: Optional[Category] = None,
    ):
        return Product.objects.create(
            # Agrego los datos ingresados del nuevo producto en las columnas de la tabla.
            name=nombre,
            price=precio,
            description=descripcion,
            stock=cantidades,
            category=categoria,
        )

    # Filtrar los productos que posean la misma categoría especificada.
    def filter_by_category(
        self, 
        categoria: Category,
        
    ) -> List[Product]:
        return Product.objects.filter(category=categoria)

    def filter_by_category_name(
        self, 
        nombre_categoria: str,
    
    ) -> List[Product]:
        return Product.objects.filter(
            category__name=nombre_categoria
        )

    # Elimiar un producto específico de la lista.
    def delete(self, producto: Product):
        return producto.delete()

    def get_product_gte_stock():
        ...

    def get_product_lte_stock():
        ...

    # Modifico un producto de la lista.
    def update(
        self,
        producto: Product,
        nombre: str,
        precio: float,
        cantidad: int,
        categoria: Category,
        descripcion: str,

    ) -> Product:

        # Asegurar que no haya números negativos en las cantidades de productos.
        if int(cantidad) < 0:
            raise ValueError("No se puede tener menos de cero unidades en el inventario.")

        # Reemplazo las caracteristicas anteriores del producto por las nuevas realizadas.
        producto.name = nombre
        producto.price = precio
        producto.stock = cantidad
        producto.category = categoria
        producto.description = descripcion

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        producto.save()


