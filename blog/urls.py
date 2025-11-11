
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('autor/<int:autor_pk>', views.autor_post, name='autor_post'),
    path('autores', views.autores, name='autores'),
]
