from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rutas para llamar a las funciones de las vistas.
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
]