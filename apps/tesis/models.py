from django.db import models

# Create your models here.
from apps.utils.models import BaseModel

# Utils
import os
import uuid
import hashlib

from django.utils import timezone


def upload_to_tesis(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/tesis/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class Tesis(BaseModel):
    nombre      = models.CharField('Nombre de la tesis', max_length=300, blank=True, null=True)
    lugar       = models.CharField('Nombre de la institución', max_length=300, blank=True, null=True)
    responsable = models.TextField('Responsable', blank=True, null=True)
    email       = models.EmailField('Correo de contacto', blank=True, null=True)
    descripcion = models.TextField('Resumen de la tesis', blank=True, null=True)
    abstract    = models.TextField('Abstract de la tesis', blank=True, null=True)
    imagen      = models.FileField(upload_to=upload_to_tesis, blank=True, null=True)
    documento   = models.FileField(upload_to='documents/pdf/', blank=True, null=True)
    link_tesis  = models.URLField('Url en donde se encuentra la tesis', blank=True, null=True)
    asignada    = models.BooleanField('Asignación tesis', default=False)

    def __str__(self):
        return '{}'.format(self.nombre)