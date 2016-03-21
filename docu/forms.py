from django import forms

from .models import Contacto

class ContactoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre", error_messages = {'required': "Este campo es requerido"})
	correo = forms.EmailField(label="Correo", error_messages = {'required': "Este campo es requerido"})
	mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class':'materialize-textarea'}),
		error_messages = {'required': "Este campo es requerido"})

	class Meta:
		model = Contacto
		fields = ('nombre', 'correo', 'mensaje')