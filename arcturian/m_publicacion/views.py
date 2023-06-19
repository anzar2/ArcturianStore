from django.shortcuts import render

def mostrar_publiaciones(request):
    return render(request, 'publicaciones.html')
def mostrar_publicar(request):
    return render(request, 'publicar.html')
