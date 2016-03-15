from django.shortcuts import render

# Create your views here.

def index(request):
    """ Index de la pagina
    """
    context = {}
    return render(request, 'base.html', context)