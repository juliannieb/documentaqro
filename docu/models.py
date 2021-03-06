from django.db import models
from django.utils import timezone

class Highlights(models.Model):
	titulo = models.CharField(max_length=100, default="", blank=True)
	frase = models.CharField(max_length=100, default="", blank=True)
	imagen = models.ImageField(upload_to='highlights', default='static/default.jpg')

	type_choices = ((0, 'Centro'), (1, 'Izquierda'),(2, 'Derecha'),)
	posicion = models.IntegerField(choices=type_choices, default=0)

	def __str__(self):
		return str(self.pk) + " - " + self.titulo

	def __unicode__(self):
		return str(self.pk) + " - " + self.titulo

class Festival(models.Model):
	nombre = models.CharField(max_length=100)
	nombre_corto = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Sede(models.Model):
	type_choices = ((0, 'Sede Oficial'), (1, 'Hoteles'),(2, 'Otros'),)
	tipo = models.IntegerField(choices=type_choices, default=0)
	nombre = models.CharField(max_length=100)
	direccion = models.TextField()
	imagen = models.ImageField(upload_to='sedes', default='static/default.jpg')
	latitud = models.FloatField()
	longitud = models.FloatField()

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	festival = models.ForeignKey('Festival')

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(default="")
	imagen_principal = models.ImageField(upload_to='eventos', default='static/default.jpg')
	logo = models.ImageField(upload_to='eventos', default='static/default.jpg')
	
	texto_introductorio_jurado = models.TextField(null=True, blank=True)
	texto_introductorio_invitados_especiales = models.TextField(null=True, blank=True)
	texto_introductorio_talleristas = models.TextField(null=True, blank=True)
	texto_introductorio_seleccion_oficial_nacional = models.TextField(null=True, blank=True)
	texto_introductorio_seleccion_oficial_internacional = models.TextField(null=True, blank=True)
	texto_introductorio_sedes = models.TextField(null=True, blank=True)
	
	header_seleccion_oficial = models.ImageField(upload_to='eventos', null=True, blank=True)
	header_proyecciones = models.ImageField(upload_to='eventos', null=True, blank=True)
	header_actividades = models.ImageField(upload_to='eventos', null=True, blank=True)

	btn_seleccion_oficial = models.ImageField(upload_to='eventos', null=True, blank=True)
	btn_proyecciones = models.ImageField(upload_to='eventos', null=True, blank=True)
	btn_actividades = models.ImageField(upload_to='eventos', null=True, blank=True)
	
	patrocinadores = models.ImageField(upload_to='eventos', null=True, blank=True)
	arte = models.ImageField(upload_to='eventos', null=True, blank=True)
	color = models.CharField(max_length=7)
	color_texto_nav = models.CharField(max_length=7)
	fecha_inicio = models.DateTimeField('Fecha inicio')
	fecha_fin = models.DateTimeField('Fecha fin')
	link_acreditaciones = models.CharField(max_length=2000, null=True, blank=True)

	texto_introductorio_premios = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Proyeccion(models.Model):
	evento = models.ForeignKey('Evento')
	sede = models.ForeignKey('Sede', null=True, blank=True)

	nombre = models.CharField(max_length=100)
	fecha_y_hora = models.DateTimeField('Fecha y hora')
	descripcion = models.CharField(max_length=500)
	es_seleccion_oficial = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre + " - " + self.fecha_y_hora.strftime('%d-%B-%Y %H:%M')

	def __unicode__(self):
		return self.nombre + " - " + self.fecha_y_hora.strftime('%d-%B-%Y %H:%M')

class Taller(models.Model):
	evento = models.ForeignKey('Evento')
	sede = models.ForeignKey('Sede')

	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=2000)
	nombre_tallerista = models.CharField(max_length=200)
	fecha_y_hora = models.DateTimeField('Fecha y hora')
	fecha_y_hora_final = models.DateTimeField('Fecha y hora final')
	imagen = models.ImageField(upload_to='talleres', default='static/default.jpg')
	costo = models.CharField(max_length=150)
	link_inscripcion = models.CharField(max_length=2000)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Conferencia(models.Model):
	evento = models.ForeignKey('Evento')
	sede = models.ForeignKey('Sede')

	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=2000)
	nombre_conferencista = models.CharField(max_length=200)
	fecha_y_hora = models.DateTimeField('Fecha y hora')
	fecha_y_hora_final = models.DateTimeField('Fecha y hora final')
	imagen = models.ImageField(upload_to='Conferencia', default='static/default.jpg')
	costo = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre


class Pelicula(models.Model):
	evento = models.ForeignKey('Evento', blank=True, null=True)
	proyeccion = models.ForeignKey('Proyeccion', blank=True, null=True)
	proyeccion_2 = models.ForeignKey('Proyeccion', blank=True, null=True, related_name='peliculas_2')

	es_seleccion_oficial = models.BooleanField(default=False)
	nacional = models.BooleanField(default=False)
	nombre = models.CharField(max_length=100)
	poster = models.ImageField(upload_to='peliculas', default='static/default.jpg')
	still = models.ImageField(upload_to='peliculas', default='static/default.jpg')
	sinopsis = models.CharField(max_length=1000)
	duracion = models.CharField(max_length=30)
	director = models.CharField(max_length=1000)
	year = models.IntegerField()
	origen = models.CharField(max_length=100)
	trailer = models.CharField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Jurado(models.Model):
	evento = models.ForeignKey('Evento')

	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=500)
	foto = models.ImageField(upload_to='jurado', default='static/default.jpg')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre


class Subscriptor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre + " " + self.apellido

	def __unicode__(self):
		return self.nombre + " " + self.apellido

class Area(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class MiembroEquipo(models.Model):
	area = models.ForeignKey('Area')

	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='equipo', default='static/default.jpg')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class MiembroStaff(models.Model):
	area = models.ForeignKey('Area')
	
	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='staff', default='static/default.jpg')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class BlogPost(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.CharField(max_length=500)
	fecha = models.DateField('Fecha')
	imagen = models.ImageField(upload_to='posts', default='static/default.jpg')
	contenido = models.TextField(default="")
	video = models.CharField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.titulo

	def __unicode__(self):
		return self.titulo

class Contacto(models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)
	mensaje = models.CharField(max_length=2000)
	fecha_y_hora = models.DateTimeField('Fecha y hora')

	def __str__(self):
		return self.nombre + " - " + self.fecha_y_hora.strftime('%d-%B-%Y %H:%M') + " - " + self.correo + " - " + self.mensaje

	def __unicode__(self):
		return self.nombre + " - " + self.fecha_y_hora.strftime('%d-%B-%Y %H:%M') + " - " + self.correo + " - " + self.mensaje

class RedesSociales(models.Model):
	facebook = models.CharField(max_length=2000)
	twitter = models.CharField(max_length=2000)
	instagram = models.CharField(max_length=2000)
	mailchimp = models.CharField(max_length=2000)
	correo_principal = models.CharField(max_length=100)

	def __str__(self):
		return "Redes sociales"

	def __unicode__(self):
		return "Redes sociales"

class Index(models.Model):
	descripcion_inicial = models.TextField()
	imagen_parallax_inicial = models.ImageField(upload_to='index', default='static/default.jpg')

	def __str__(self):
		return "Index"

	def __unicode__(self):
		return "Index"

class Tallerista(models.Model):
	evento = models.ForeignKey('Evento')

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='jurado', default='static/default.jpg')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class InvitadoEspecial(models.Model):
	evento = models.ForeignKey('Evento')

	nombre = models.CharField(max_length=100)
	titulo_participacion = models.CharField(max_length=100)
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='jurado', default='static/default.jpg')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre