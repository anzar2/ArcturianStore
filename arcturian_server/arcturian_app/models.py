from django.db.models import (
    Model,
    CharField,
    ImageField,
    BooleanField,
    ForeignKey,
    PositiveSmallIntegerField,
    CASCADE,
)
from django.contrib.auth.models import User
# Create your models here.

class Carta(Model):
    nombre_carta = CharField(max_length=70,blank=False,null=False)
    imagen= ImageField(upload_to='foto_carta/')
    carta_reeditada=BooleanField(default=True)
     
class Region(Model):
    nombre_region = CharField(max_length=60,null=False, blank=False)
       
class InfoUsuario(Model):
    apmaterno = CharField(max_length=15, null=False, blank=False)
    telefono = PositiveSmallIntegerField(null=False,blank=False)
    foto_usuario =ImageField(upload_to='foto_usuario/')
    fk_id_usuario = ForeignKey(User, on_delete=CASCADE)
    fk_id_region=ForeignKey(Region,on_delete=CASCADE)

class Comuna(Model):
    nombre_comuna=CharField(max_length=50,blank=False,null=False)
    fk_id_region = ForeignKey(Region,on_delete=CASCADE)

class Mazo(Model):
    nombre_mazo = CharField(max_length=10)
    fk_id_usuario = ForeignKey(User, on_delete=CASCADE)
    
class DetalleMazo(Model):
    fk_mazo = ForeignKey(Mazo, on_delete=CASCADE)
    fk_id_carta=ForeignKey(Carta,on_delete=CASCADE)
    fk_id_usuario = ForeignKey(User, on_delete=CASCADE)
