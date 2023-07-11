from django.shortcuts import render,redirect
from .forms import FormularioRegistro
def m_index(request):
    return render(request, 'index.html')
def m_cartas(request):
    
    return render(request,'productos/listado_cartas.html')

def m_creacion_cuenta(request):
    if request.method=='GET':
        context={
            'formulario':FormularioRegistro(),
        }
        return render(request, 'usuario/usuario_creacion.html',context)
    if request.method=='POST':

        datos_usuario=FormularioRegistro(data=request.POST)
        es_valido=datos_usuario.is_valid()

        if es_valido:
            datos_usuario.save()
            return redirect('index')
    
        context={
            'formulario':FormularioRegistro()
        }
        return render(request, 'usuario/usuario_creacion.html',context)