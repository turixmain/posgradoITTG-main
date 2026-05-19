from django.db import models

# Create your models here.

from apps.utils.models import BaseModel
from apps.tesis.models import Tesis
from apps.posgrados.models import Posgrados

# Utils
import os
import uuid
import hashlib

from django.utils import timezone

def upload_to_estudiantes(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/estudiantes/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

def upload_to_docentes(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/docentes/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

def upload_to_cohorte(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename)
    hash_file = hashlib.sha256(str(str(instance)+str(now)).encode()).hexdigest()
    return f'images/cohorte/{now:%Y}/{now:%m}/{now:%d}/{hash_file}{extension}'

class Docentes(BaseModel):

    SNI_CHOICES = (
        ('C', 'Candidato'),
        ('I', 'Nivel I'),
        ('II', 'Nivel II'),
        ('III', 'Nivel III'),
    )

    GRADO_CHOICES = (
        ('Dr', 'Doctor'),
        ('Dra', 'Doctora'),
        ('MC', 'Maestro en Ciencias')
    )

    grado                 = models.CharField('Grado', max_length=5, choices=GRADO_CHOICES, blank=True, null=True)
    nombre                = models.CharField('Nombre del investigador', max_length=150, blank=True, null=True)
    apellidos             = models.CharField('Apellidos del investigador', max_length=150, blank=True, null=True)
    formacion_profesional = models.CharField('Formación profesional', max_length=200, blank=True, null=True)
    expertise             = models.CharField('Expertise', max_length=200, blank=True, null=True)
    sni                   = models.CharField('SNI', max_length=5, choices=SNI_CHOICES, blank=True, null=True)
    email                 = models.EmailField('Correo del investigador', blank=True, null=True)
    perfil_researchgate   = models.URLField('Perfil Researchgate', blank=True, null=True)
    scholar_google        = models.URLField('Perfil Scholar Google', blank=True, null=True)
    personal_page         = models.URLField('Pagina Personal', blank=True, null=True)
    fotografia            = models.FileField(upload_to=upload_to_docentes, blank=True, null=True)
    descripcion           = models.TextField(blank=True, null=True)
    posgrado              = models.ManyToManyField(Posgrados, blank=True)

    def __str__(self):
        return self.grado + '. ' + self.nombre + ' ' + self.apellidos

class Estudiantes(BaseModel):
    nombre                = models.CharField('Nombre del estudiante', max_length=150, blank=True, null=True)
    apellidos             = models.CharField('Apellidos del estudiante', max_length=150, blank=True, null=True)
    tesis_estudiante      = models.OneToOneField(Tesis, on_delete=models.CASCADE, blank=True, null=True)
    email                 = models.CharField('Correo del estudiante', max_length=200, blank=True, null=True)
    posgrado              = models.ForeignKey(Posgrados, on_delete=models.CASCADE)
    director_tesis        = models.ForeignKey(Docentes, related_name='director_tesis', on_delete=models.CASCADE, blank=True, null=True)
    codirector_tesis      = models.ForeignKey(Docentes, related_name='codirector_tesis', on_delete=models.CASCADE, blank=True, null=True)
    revisores_tesis       = models.ManyToManyField(Docentes, blank=True)
    revisor_externo       = models.CharField('Revisor externo de tesis', max_length=150, blank=True, null=True)
    perfil_researchgate   = models.URLField('Perfil Researchgate', blank=True, null=True)
    scholar_google        = models.URLField('Perfil Scholar Google', blank=True, null=True)
    fotografia            = models.FileField(upload_to=upload_to_estudiantes, blank=True, null=True)
    descripcion           = models.TextField(blank=True, null=True)
    fecha_examen_grado    = models.DateField('Fecha de examen de grado', blank=True, null=True)
    actividad             = models.CharField('Actividad del estudiante', max_length=200, blank=True, null=True)
    actividad_actual      = models.CharField('Actividad actual del estudiante', max_length=200, blank=True, null=True)
    nombre_institucion    = models.CharField('Nombre de la institución donde labora', max_length=200, blank=True, null=True)
    numero_acta           = models.CharField('Numero de acta', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Generacion(BaseModel):
    nombre   = models.CharField('Nombre de la generación', max_length=150, blank=True, null=True)
    mes      = models.CharField('Mes de inicio de la generación', max_length=150, blank=True, null=True)
    ano      = models.CharField('Año de la generación', max_length=150, blank=True, null=True)
    cohorte  = models.FileField(upload_to=upload_to_cohorte, verbose_name='Imagen de Cohorte', blank=True, null=True )
    alumnos  = models.ManyToManyField(Estudiantes, blank=True)
    posgrado = models.ForeignKey(Posgrados, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre + '-' + str(self.posgrado)

class Tutorias(BaseModel):
    estudiante  = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    docente     = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    generacion  = models.ForeignKey(Generacion, on_delete=models.CASCADE)

    def __str__(self): 
        return str(self.generacion) + ' - ' + str(self.estudiante.posgrado)

class TutoriasManytoMany(BaseModel):
    from apps.investigadores.models import Docentes
    from apps.investigadores.models import Estudiantes

    generacion  = models.ForeignKey(Generacion, on_delete=models.CASCADE, blank=True, null=True)
    docente     = models.ManyToManyField(Docentes, blank=True)
    estudiante  = models.ManyToManyField(Estudiantes, blank=True)

    def __str__(self):
        return self.generacion.nombre + '- ' + self.generacion.ano
    

class TiempoParcial(BaseModel):
    from apps.lineas_investigacion.models import LineasInvestigacion

    nombre   = models.CharField(max_length=100, default='Tiempo Parcial', blank=True, null=True) 
    docentes = models.ManyToManyField(Docentes, blank=True)
    posgrado = models.ForeignKey(Posgrados, blank=True, null=True, on_delete=models.CASCADE)
    linea    = models.ForeignKey(LineasInvestigacion, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - ' + str(self.posgrado)

class TiempoCompleto(BaseModel):
    from apps.lineas_investigacion.models import LineasInvestigacion
    
    nombre   = models.CharField(max_length=100, default='Tiempo Completo') 
    docentes = models.ManyToManyField(Docentes, blank=True)
    posgrado = models.ForeignKey(Posgrados, blank=True, null=True, on_delete=models.CASCADE)
    linea    = models.ForeignKey(LineasInvestigacion, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - ' + str(self.posgrado)