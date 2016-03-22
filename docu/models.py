from django.db import models
from django.utils import timezone

class Festival(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Sede(models.Model):
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='sedes', default='static/default.jpg')
	latitud = models.FloatField()
	longitud = models.FloatField()

	def __str__(self):
		return self.nombre

class Evento(models.Model):
	festival = models.ForeignKey('Festival')

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(default="")
	imagen_principal = models.ImageField(upload_to='eventos', default='static/default.jpg')
	logo = models.ImageField(upload_to='eventos', default='static/default.jpg')
	patrocinadores = models.ImageField(upload_to='eventos', default='static/default.jpg')
	color = models.CharField(max_length=7)
	fecha_inicio = models.DateTimeField('Fecha inicio')
	fecha_fin = models.DateTimeField('Fecha fin')

	def __str__(self):
		return self.nombre

class Proyeccion(models.Model):
	evento = models.ForeignKey('Evento')
	sede = models.ForeignKey('Sede')

	nombre = models.CharField(max_length=100)
	fecha_y_hora = models.DateTimeField('Fecha y hora')
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre + " - " + self.fecha_y_hora

class Pelicula(models.Model):
	proyeccion = models.ForeignKey('Proyeccion')

	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='peliculas', default='static/default.jpg')
	sinopsis = models.CharField(max_length=500)
	trailer = models.CharField(max_length=1000)

	def __str__(self):
		return self.nombre

class Jurado(models.Model):
	evento = models.ForeignKey('Evento')

	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='jurado', default='static/default.jpg')

	def __str__(self):
		return self.nombre


class Subscriptor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre + " " + self.apellido

class Area(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

class MiembroEquipo(models.Model):
	area = models.ForeignKey('Area')

	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='equipo', default='static/default.jpg')

	def __str__(self):
		return self.nombre

class MiembroStaff(models.Model):
	area = models.ForeignKey('Area')
	
	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='staff', default='static/default.jpg')

	def __str__(self):
		return self.nombre

class BlogPost(models.Model):
	titulo = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='posts', default='static/default.jpg')
	contenido = models.TextField(default="")
	video = models.CharField(max_length=1000)

	def __str__(self):
		return self.titulo

class Contacto(models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)
	mensaje = models.CharField(max_length=2000)
	fecha_y_hora = models.DateTimeField('Fecha y hora')

	def __str__(self):
		return self.nombre + " - " + self.fecha_y_hora.strftime('%d-%B-%Y %H:%M') + " - " + self.correo + " - " + self.mensaje