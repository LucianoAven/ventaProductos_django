# Filtrar los elementos de la tabla Categoría como una lista.
from typing import List, Optional, NoReturn

# Importo el modelo de las columnas de la tabla que almacena las categorias de los productos.
from product.models import Category

class CategoryRepository:

    # Muestra todas las categorías establecidas en la tabla.
    def get_all(self) -> List[Category]:
        return Category.objects.all()

    # Seleccionar una categoría en específico por su id.
    def get_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.get(pk=id)

    # Eliminar una categoría
    def delete(self, categoria: Category):
        return categoria.delete()

    # Modifico una categoría de la lista.
    def update(
        self,
        categoria: Category,
        nombre: str,

    ):

        # Reemplazo las caracteristicas anteriores de la categoría por las nuevas realizadas.
        categoria.name = nombre

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        categoria.save()

    # Crea una nueva categoría.
    def create(
        self, 
        nombre: str

    ) -> Category:    
        category = Category.objects.filter(name=nombre)

        if category:
            return "Nombre en uso"

        return Category.objects.create(
            name=nombre,
        )
