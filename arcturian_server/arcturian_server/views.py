from django.shortcuts import render

def m_index(request):
    return render(request, 'index.html')