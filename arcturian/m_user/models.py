from django.db.models import(
    Model,
    CharField,
    EmailField,
    ImageField,
    IntegerField,
    
)

# Create your models here.
class Usuario(Model):
    rut = CharField(max_length=10, blank=False, null= False)
    nombre_usuario = CharField(unique=True,max_length=15,null=False,blank=False)
    pnombre = CharField(max_length=15, blank=False, null= False)
    snombre= CharField(max_length=15, blank=False, null= False)
    appaterno= CharField(max_length=15, blank=False, null= False)
    apmaterno= CharField(max_length=15, blank=False, null= False)
    correo =EmailField(max_length=30)
    contrasena= CharField(max_length=15, blank=False, null= False)
    telefono= IntegerField()
    foto_perfil= ImageField(null=True,blank=True)