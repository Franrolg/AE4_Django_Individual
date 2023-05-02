from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro-usuario/', views.formulario_usuario, name='registro usuarios'),
    path('lista-usuarios/', views.lista_usuarios , name='lista usuarios'),
]