from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	context['blog'] = blog
	return render(request, 'blog.html', context)

def blog_post(request, post_id):
	"""Post de un Blog
	"""
	post = BlogPost.objects.get(pk=post_id)
	context = {}
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