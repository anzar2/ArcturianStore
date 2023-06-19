from typing import Any
from django.forms import (
    ModelForm,
    EmailInput,
    PasswordInput,
    TextInput,
    Form
    )
from .models import Usuario
from django.contrib.auth.forms import (
    AuthenticationForm
)


class FormularioUsuarioRegistro(Form):
    class Meta:
        model = Usuario
        fields =[
            'rut',
            'nombre_usuario',
            'pnombre',
            'snombre',
            'appaterno',
            'apmaterno',
            'correo',
            'contrasena',
            'telefono',
            'foto_perfil'
        ]
        widgets = {
            'rut' : TextInput( attrs = { 'class':'form-control' }),
            'nombre_usuario' : TextInput( attrs = { 'class':'form-control' }),
            'pnombre' : TextInput( attrs = { 'class':'form-control' }),
            'snombre' : TextInput( attrs = { 'class':'form-control' }),
            'appaterno' : TextInput( attrs = { 'class':'form-control' }),
            'apmaterno' : TextInput( attrs = { 'class':'form-control' }),
            'correo' : EmailInput( attrs = { 'class':'form-control' }),
            'contrasena' : PasswordInput( attrs = { 'class':'form-control' }),
            'telefono' : TextInput( attrs = { 'class':'form-control' }),
            'foto_perfil' : TextInput( attrs = { 'class':'form-control' }),
        }
        #widgets = {}

class FormularioUsuarioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
