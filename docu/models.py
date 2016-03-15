from django.db import models

class TipoEnvento(models.Model):
    nombre = models.CharField(max_length=100)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    #patrocinadores = models.ImageField(upload_to='cars')
    color = models.CharField(max_length=7)
    fecha_inicio = models.DateTimeField('Fecha inicio')
    fecha_fin = models.DateTimeField('Fecha fin')

    def __str__(self):
    	return self.nombre

class Proyecciones(models.Model):
	nombre = models.CharField(max_length=100)
	fecha_y_hora = models.DateTimeField('Fecha y hora')
	#imagen
	sinopsis = models.CharField(max_length=500)
	#trailer

	def __str__(self):
		return self.nombre

class Jurado(models.Model):
	nombre = models.CharField(max_length=50)
	#foto

	def __str__(self):
		return self.nombre


class Subscriptores(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre + " " + self.apellido

class MiembroEquipo(models.Model):
	nombre = models.CharField(max_length=50)
	#foto

	def __str__(self):
		return self.nombre

class MiembroStaff(models.Model):
	nombre = models.CharField(max_length=50)
	#foto

	def __str__(self):
		return self.nombre

class BlogPost(models.Model):
	titulo = models.CharField(max_length=100)
	#imagen
	link = models.CharField(max_length=1000)
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.titulo

class Contacto(models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=30)
	mensaje = models.CharField(max_length=2000)

	def __str__(self):
		return self.nombre + " - " + self.correo + " - " + self.mensaje