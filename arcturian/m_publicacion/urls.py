from django.contrib import admin
from django.urls import path, include
from .views import mostrar_publiaciones, mostrar_publicar
urlpatterns = [
    path('crear/', mostrar_publicar, name='publicar'),
    path('', mostrar_publiaciones, name='publicaciones'),
]