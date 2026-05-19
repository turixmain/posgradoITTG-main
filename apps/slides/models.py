from django.db import models

# Create your models here.

# Utils
import os
import uuid
import hashlib

from django.utils import timezone

# Models
from apps.utils.models import BaseModel
from apps.posgrados.models import Posgrados

def upload_to_slides(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/slides/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class Slides(BaseModel):
    nombre      = models.CharField('Nombre de la imagen que tendrá en el carrousel',max_length=150, blank=True, null=True)
    imagen      = models.FileField(upload_to=upload_to_slides)
    descripcion = models.TextField(blank=True, null=True)
    url         = models.URLField(blank=True, null=True)
    posgrado    = models.ForeignKey(Posgrados, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre