from django.urls import path
from .views import(
    crear_usuario,
    ingreso_usuario,
)


urlpatterns=[
    path('',crear_usuario,name="crear_usuario"),
    path('ingreso/',ingreso_usuario,name="ingreso_usuario"),
]