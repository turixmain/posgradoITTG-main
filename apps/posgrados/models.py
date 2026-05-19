from django.db import models

# Create your models here.

# Utils
import os
import uuid
import hashlib

from django.utils import timezone

from apps.utils.models import BaseModel

def laboratorio(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance.imagen)+str(now)).encode()).hexdigest()
    return f'images/laboratorios/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class Posgrados(BaseModel):
    nombre           = models.CharField('Nombre del posgrado', max_length=200, blank=True, null=True)
    descripcion      = models.TextField('Descripción del posgrado', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Laboratorios(BaseModel):
    nombre              = models.CharField('Nombre del laboratorio', max_length=100, blank=True, null=True)
    imagen              = models.FileField(upload_to=laboratorio, blank=True, null=True)
    imagen_2            = models.FileField(upload_to=laboratorio, blank=True, null=True)
    imagen_3            = models.FileField(upload_to=laboratorio, blank=True, null=True)
    imagen_descripcion  = models.FileField(upload_to=laboratorio, blank=True, null=True)
    descripcion_breve   = models.TextField('Descripción corta',blank=True, null=True)
    descripcion_1       = models.TextField('Descripción parte 1', blank=True, null=True)
    descripcion_2       = models.TextField('Descripción parte 2', blank=True, null=True)
    posgrado            = models.ForeignKey(Posgrados, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre