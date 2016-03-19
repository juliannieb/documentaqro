from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    """ Index de la pagina
    """
    context = {'arreglo': ['hola', 'adios', 'bye']}
    return render(request, 'index.html', context)

def patrocinadores(request):
	"""Patrocinadores generales de DocumentaQro
	"""
	context = {}
	return render(request, 'patrocinadores.html', context)

def nosotros(request):
	"""Equipo y staff
	"""
	context = {}
	equipo = MiembroEquipo.objects.all()
	staff = MiembroStaff.objects.all()
	context['equipo'] = equipo
	context['staff'] = staff
	return render(request, 'nosotros.html', context)