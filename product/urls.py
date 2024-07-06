from django.urls import path

# Importo las funciones creadas en la vista de productos para vincularlas
# con los archivos html.
from product.views.product_view import (
    product_list,
    product_create,
    product_detail,
    product_update,
    product_delete,
)

# Importo las funciones creadas en la vista de categorias para también vincularlas
# con los archivos html.
from product.views.category_view import (
    category_list,
    category_create,
    category_detail,
    category_update,
)

from product.views.product_review_view import (
    ProductReviewCreateView,
    ProductReviewDetailView,
    ProductReviewUpdateView,
    ProductReviewView,
)

urlpatterns = [
    # Especifico las rutas donde se visualizaran los archivos html con sus funciones.
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),

    # Rutas de las categorías.
    path(route='category/', view=category_list, name='category_list'),
    path(route='category/create/', view=category_create, name='category_create'),
    path(route='category/<int:id>/', view=category_detail, name='category_detail'),
    path(route='category/<int:id>/update/', view=category_update, name='category_update'),

    path(route='product_reviews/', view=ProductReviewView.as_view(), name='product_reviews'),
    path(route='product_reviews/create/', view=ProductReviewCreateView.as_view(), name='product_reviews_create'),
    path(route='product_reviews/<int:id>/', view=ProductReviewDetailView.as_view(), name='product_reviews_detail'),
    path(route='product_reviews/<int:id>/update/', view=ProductReviewUpdateView.as_view(), name='product_reviews_update'),
]