from django.urls import path

from individual4.views import *

urlpatterns = [
    path('', index, name='index'),
    path('usuario/', formulario_usuario, name='usuario')
]