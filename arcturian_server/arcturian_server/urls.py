"""
URL configuration for arcturian_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    m_index,
    m_creacion_cuenta,
    m_cartas,
    m_login,
    cerrar_sesion,
    m_mazo,
    m_añadir_mazo,
    m_eliminar_mazo
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', m_index, name='index'),
    path('login/',m_login,name='login'),
    path('crear_cuenta/',m_creacion_cuenta,name='crear_cuenta'),
    path('cartas/',m_cartas,name='cartas'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('mazo/',m_mazo,name='mazo'),
    path('mazo/agregar',m_añadir_mazo,name='agregar_mazo'),
    path('mazo/eliminar/<int:id_mazo>/',m_eliminar_mazo,name='eliminar_mazo'),
]
