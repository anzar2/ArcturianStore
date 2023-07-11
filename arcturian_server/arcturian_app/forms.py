from django.forms import(
    ModelForm,
    PasswordInput,
    CharField,
    EmailField,
    EmailInput,
    TextInput,
    ChoiceField,
    Select,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from .data import COMUNA_DATA, REGION_DATA
#Formulario de creacion de cuenta, Login y autenticación

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['username'].widget = TextInput(attrs = { 'class': 'form-control mb-5', 'placeholder': 'Nombre Usuario'})
        self.fields['password'].widget = PasswordInput (attrs= { 'class': 'form-control mb-5', 'placeholder': 'Contraseña'})

class RegistroForm(UserCreationForm):
    def __init__(self, *args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'] = CharField(help_text="La contraseña debe tener minimo 8 caracteres, y debe incluir mayuscula")
        self.fields['password2']= CharField(help_text="Su contraseña no puede ser completamente numerica, ni asemejarse a su informacion personal")
        self.fields['password1'].widget = PasswordInput(attrs = { 'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs = { 'class': 'form-control'})

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name', 
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username' : TextInput( attrs = { 'class':'form-control' }),
            'first_name' : TextInput( attrs = { 'class':'form-control' }),
            'last_name' : TextInput( attrs = { 'class':'form-control' }),
            'email' : EmailInput( attrs = { 'class':'form-control' }),
            'password1' : PasswordInput( attrs = { 'class':'form-control' }),
            'password2' : PasswordInput( attrs = { 'class':'form-control' })
        }

    address = CharField(
        required=True,
        widget= TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    comuna = ChoiceField(
        required=True,
        choices=COMUNA_DATA,
        widget= Select(
            attrs={
                'class': 'form-select'
            }
        )
    )
    region = ChoiceField(
        required=True,
        choices=REGION_DATA,
        widget= Select(
            attrs={
                'class': 'form-select'
            }
        )
    )
