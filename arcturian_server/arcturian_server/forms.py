from typing import Any
from django.forms import(
    ModelForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm)

#Formulario de creacion de cuenta, Login y autenticación

class FormularioRegistro(UserCreationForm):
    pass

