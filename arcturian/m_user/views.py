from django.shortcuts import render
from .forms import (
    FormularioUsuarioRegistro,
    FormularioUsuarioLogin,
)
# Create your views here.


def crear_usuario(request):
    if request.method=='GET':
        contexto={
            'formularioCreacion':FormularioUsuarioRegistro()
        }
    if request.method=='POST':
        pass
    return render(request,'registrar.html')


def ingreso_usuario(request):
    if request.method=='GET':
        contexto={
            'formularioCreacion':FormularioUsuarioLogin()
        }

    return render(request,'login.html')