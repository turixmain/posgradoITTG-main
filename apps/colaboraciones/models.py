from django.db import models

from apps.utils.models import BaseModel
from apps.posgrados.models import Posgrados
# Create your models here.

# Utils
import os
import uuid
import hashlib

from django.utils import timezone

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance.imagen_institucion)+str(now)).encode()).hexdigest()
    return f'images/colaboraciones/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

def galeria(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance.imagen)+str(now)).encode()).hexdigest()
    return f'images/galeria/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class Colaboraciones(BaseModel):
    nombre_institucion = models.CharField('Nombre del la institución', max_length=100, blank=True, null=True)
    imagen_institucion = models.FileField(upload_to=upload_to, blank=True, null=True)
    descripcion        = models.TextField(blank=True, null=True)
    posgrado           = models.ForeignKey(Posgrados, on_delete=models.CASCADE ,blank=True, null=True)

    def __str__(self):
        return self.nombre_institucion

class Galeria(BaseModel):
    nombre   = models.CharField('Nombre del imagen', max_length=100, blank=True, null=True)
    imagen   = models.FileField(upload_to=galeria, blank=True, null=True)
    posgrado = models.ForeignKey(Posgrados, on_delete=models.CASCADE ,blank=True, null=True)

    def __str__(self):
        return self.nombre