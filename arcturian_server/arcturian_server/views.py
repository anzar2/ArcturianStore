from django.shortcuts import render,redirect
from arcturian_app.forms import (RegistroForm,LoginForm)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import arcturian_app.models as arcturian_app
from django.contrib.auth.models import User
def m_index(request):
    return render(request, 'index.html')

def m_cartas(request):
    return render(request,'productos/listado_cartas.html')



def m_creacion_cuenta(request):
    if request.method=='GET':
        context={
            'formulario':RegistroForm(),
        }
        return render(request, 'usuario/usuario_creacion.html',context)
    if request.method=='POST':

        datos_usuario=RegistroForm(data=request.POST)
        es_valido=datos_usuario.is_valid()

        if es_valido:
            datos_usuario.save()
            return redirect('index')
    
        context={
            'formulario':RegistroForm()
        }
        return render(request, 'usuario/usuario_creacion.html',context)

def m_login(request):

    context = {
    'formulario': LoginForm()
    }
    if request.method=='POST':
        datos_post=LoginForm(data=request.POST)
        if datos_post.is_valid():
            usuario = datos_post.cleaned_data['username']
            contraseña = datos_post.cleaned_data['password']
            usuario=authenticate(username=usuario,password=contraseña)
            login(request,usuario)
            print(f"Ingreso el usuario: {usuario}")
            return redirect('index')
        else:
            print(datos_post.errors)
    return render(request, 'usuario/usuario_ingreso.html', context)


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        print("Se ha salido de la sesión")
    return redirect ('index')

@login_required
def m_mazo(request):
    mazos_all = arcturian_app.Mazo.objects.all()
    contexto={
        'mazos':mazos_all
    }
    return render(request, 'mazos.html',contexto)



def m_añadir_mazo(request):
    fk_usuario_id = User.objects.get(id=request.user.id)
    nombre_mazo = 'Nuevo Mazo'
    total_mazos=arcturian_app.Mazo.objects.filter(fk_id_usuario=request.user.id)
    print(total_mazos)
    
    new_mazo = arcturian_app.Mazo(
        nombre_mazo=nombre_mazo,
        fk_id_usuario = fk_usuario_id
    )
    
    print(total_mazos.count())
    if total_mazos.count()>=5:
        print("No se permiten mas mazos")
    else:
        print("Mazo añadido")
        new_mazo.save()
    return redirect('mazo')
    
    
def m_eliminar_mazo(request,id_mazo):
    mazo_escogido=arcturian_app.Mazo.objects.get(id=id_mazo)
    mazo_escogido.delete()
    print('se borro el mazo:', mazo_escogido)
    return redirect('mazo')
