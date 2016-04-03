from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime, timedelta

from .models import *
from .forms import ContactoForm

# Create your views here.

def index(request):
	""" Index de la pagina
	"""
	context = {}
	highlights = Highlights.objects.all()
	festivales = Festival.objects.all()
	blog = BlogPost.objects.all()
	context['highlights'] = highlights
	context['festivales'] = festivales
	context['blog'] = blog[:3]
	return render(request, 'index.html', context)

def patrocinadores(request):
	"""Patrocinadores generales de DocumentaQro
	"""
	context = {}
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	return render(request, 'patrocinadores.html', context)

def nosotros(request):
	"""Equipo y staff
	"""
	context = {}
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			contacto = form.save(commit=False)
			contacto.fecha_y_hora = timezone.now()
			contacto.save()
			return redirect('contacto')
	else:
		form = ContactoForm()
	context['form'] = form
	equipo = MiembroEquipo.objects.all()
	staff = MiembroStaff.objects.all()
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['equipo'] = equipo
	context['staff'] = staff
	return render(request, 'nosotros.html', context)

def blog(request):
	"""Blog
	"""
	context = {}
	blog = BlogPost.objects.all()
	paginator = Paginator(blog, 24)
	page = request.GET.get('page')
	try:
		blog = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		blog = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		blog = paginator.page(paginator.num_pages)
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['blog'] = blog
	return render(request, 'blog.html', context)

def blog_post(request, post_id):
	"""Post de un Blog
	"""
	post = BlogPost.objects.get(pk=post_id)
	context = {}
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['post'] = post
	return render(request, 'blog_post.html', context)

def search_blog_posts(request):
	"""Busqueda de un post
	"""
	search_string = request.GET.get('search_string', '')
	print(search_string)
	context = {}
	blog = BlogPost.objects.filter(titulo__icontains=search_string)
	paginator = Paginator(blog, 24)
	page = request.GET.get('page')
	try:
		blog = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		blog = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		blog = paginator.page(paginator.num_pages)
	context['blog'] = blog
	return render(request, 'search_blog_posts.html', context)

def contacto(request):
	"""Mensaje de contacto
	"""
	context = {}
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			contacto = form.save(commit=False)
			contacto.fecha_y_hora = timezone.now()
			contacto.save()
			return redirect('contacto')
	else:
		form = ContactoForm()
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['form'] = form
	return render(request, 'contacto.html', context)

def evento(request, festival_id):
	"""Vista de un evento
	"""
	context = {}
	#festival = Festival.objects.get(pk=festival_id)
	today = timezone.now()
	eventos_proximos = Evento.objects.filter(festival=festival_id, fecha_fin__gt=today)
	if eventos_proximos:
		evento = eventos_proximos[0]
		seleccion_oficial = Pelicula.objects.filter(evento=evento.pk, es_seleccion_oficial=True)
		proyecciones = Proyeccion.objects.filter(evento=evento.pk)
		conferencias = Conferencia.objects.filter(evento=evento.pk)
		talleres = Taller.objects.filter(evento=evento.pk)
		jurado = Jurado.objects.filter(evento=evento.pk)
		context['evento'] = evento
		context['seleccion_oficial'] = seleccion_oficial
		context['proyecciones'] = proyecciones
		context['conferencias'] = conferencias
		context['talleres'] = talleres
		context['jurado'] = jurado
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	return render(request, 'evento.html', context)

def seleccion_oficial(request, evento_id):
	"""Seleccion oficial
	"""
	context = {}
	evento = get_object_or_404(Evento, pk=evento_id)
	seleccion_oficial = Pelicula.objects.filter(evento=evento.pk, es_seleccion_oficial=True, nacional=True)
	paginator = Paginator(seleccion_oficial, 24)
	page = request.GET.get('page')
	try:
		seleccion_oficial = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		seleccion_oficial = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		seleccion_oficial = paginator.page(paginator.num_pages)
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['evento'] = evento
	context['seleccion_oficial'] = seleccion_oficial
	return render(request, 'seleccion_oficial.html', context)

def seleccion_oficial_filtro(request, evento_id, tipo_seleccion):
	"""Seleccion oficial
	"""
	context = {}
	evento = get_object_or_404(Evento, pk=evento_id)
	if (tipo_seleccion == 'nacional'):
		seleccion_oficial = Pelicula.objects.filter(evento=evento.pk, es_seleccion_oficial=True, nacional=True)
	else:
		seleccion_oficial = Pelicula.objects.filter(evento=evento.pk, es_seleccion_oficial=True, nacional=False)
	paginator = Paginator(seleccion_oficial, 24)
	page = request.GET.get('page')
	try:
		seleccion_oficial = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		seleccion_oficial = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		seleccion_oficial = paginator.page(paginator.num_pages)
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	context['evento'] = evento
	context['seleccion_oficial'] = seleccion_oficial
	context['origen_seleccion_oficial'] = tipo_seleccion
	return render(request, 'seleccion_oficial_filtro.html', context)


def pelicula(request, pelicula_id):
	"""Patrocinadores generales de DocumentaQro
	"""
	context = {}
	pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
	festivales = Festival.objects.all()
	context['festivales'] = festivales
	return render(request, 'pelicula.html', context)