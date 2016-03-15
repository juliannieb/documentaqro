from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TipoEnvento)
admin.site.register(Evento)
admin.site.register(Proyecciones)
admin.site.register(Jurado)
admin.site.register(Subscriptores)
admin.site.register(MiembroEquipo)
admin.site.register(MiembroStaff)
admin.site.register(BlogPost)
admin.site.register(Contacto)