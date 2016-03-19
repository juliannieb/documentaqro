from django.shortcuts import render

# Create your views here.

def index(request):
    """ Index de la pagina
    """
    context = {'arreglo': ['hola', 'adios', 'bye']}
    return render(request, 'index.html', context)