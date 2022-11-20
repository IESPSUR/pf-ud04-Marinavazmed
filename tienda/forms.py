from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioCompra(forms.Form):
    """Formulario para la compra del objeto"""
    cantidad = forms.IntegerField(required=True, min_value=1)

class FormularioBusqueda(forms.Form):
    """Formulario para aplicar el filtro de búsqueda objetos"""
    nombre = forms.CharField(required=True, max_length=30)


class UserCreateForm(UserCreationForm):
    """Crea un formulario basado en el UserCreationForm de Django. Se usa para customizar el formulario por defecto.
    En este caso, para que los mensajes de help_text no aparezcan en los campos indicados al llamar al constructor __init__"""
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
