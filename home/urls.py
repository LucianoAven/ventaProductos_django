from django.urls import path

from home.views import (
    index_view,
    LoginView,
    LogoutView,
)

urlpatterns = [
    # Vincula las vistas de home con una ruta url.
    path(route='', view=index_view, name='index'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
]