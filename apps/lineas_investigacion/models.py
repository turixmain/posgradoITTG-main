from django.db import models

# Create your models here.

from apps.utils.models import BaseModel
from apps.investigadores.models import Docentes
from apps.posgrados.models import Posgrados

# Utils
import os
import uuid
import hashlib

from django.utils import timezone

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/linea-investigacion/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class LineasInvestigacion(BaseModel):
    nombre      = models.CharField('Nombre linea de investigación', max_length=150, blank=True, null=True)
    descripcion = models.TextField('Descripción linea de investigación', blank=True, null=True)
    imagen_lin  = models.FileField(upload_to=upload_to)
    posgrado    = models.ForeignKey(Posgrados, on_delete=models.CASCADE)
    docentes    = models.ManyToManyField(Docentes)

    def __str__(self):
        return self.nombre + ' - ' + str(self.posgrado)