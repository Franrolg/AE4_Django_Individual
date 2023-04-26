from django.urls import path

from individual4.views import index

urlpatterns = [
    path('', index, name='index'),
]