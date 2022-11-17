from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ##ESTE ARCHIVO SOBREESCRIBE EL FORMULARIO DE USUARIO POR DEFECTO DE DJANGO (USERCREATIONFORM) Y NOS AYUDA A ENTENDER:
#
# class FormularioUsuario(UserCreationForm):
#     nombre = forms.TextInput(required = True)
#     contras = forms.TextInput(required = True)
#
#     class Meta:
#         model = User
#         fields = ("nombre", "email")
#
#     def save(self, commit=True):
#         user=super(FormularioUsuario,self).save(commit = False)
#         user.nombre = self.cleaned_data['nombre']
#         user.contras = self.cleaned_data['contras']
#         if commit:
#             user.save()
#         return user

class FormularioCompra(forms.Form):
    cantidad = forms.IntegerField(required=True, min_value=1)

class FormularioBusqueda(forms.Form):
    nombre = forms.CharField(required=True, max_length=30)
