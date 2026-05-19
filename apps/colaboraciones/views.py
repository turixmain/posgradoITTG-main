from django.shortcuts import render

from django.shortcuts import get_object_or_404

# Models
from apps.colaboraciones.models import Colaboraciones, Galeria
from apps.lineas_investigacion.models import LineasInvestigacion
from apps.posgrados.models import Laboratorios

def colaboraciones_academicas(request):
    colaboraciones = Colaboraciones.objects.all().filter(posgrado=1).order_by('-id')
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    contex = {'colaboraciones': colaboraciones, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/colaboraciones.html', context=contex)

def mision_vision(request):
    return render(request=request, template_name='components/doctorado/mision-vision.html')

def vinculacion(request):
    return render(request=request, template_name='components/doctorado/vinculacion.html')

def procedimientos(request):
    return render(request=request, template_name='components/doctorado/procedimientos.html')

def galeria_doctorado(request):
    galerias = Galeria.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context  = {'imagenes': galerias, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/galeria.html', context=context)

def colaboraciones_academicas_maestria(request):
    colaboraciones = Colaboraciones.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    contex = {'colaboraciones': colaboraciones, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/colaboraciones.html', context=contex)

def mision_vision_maestria(request):
    return render(request=request, template_name='components/maestria/mision-vision.html')

def vinculacion_maestria(request):
    return render(request=request, template_name='components/maestria/vinculacion.html')

def procedimientos_maestria(request):
    return render(request=request, template_name='components/maestria/procedimientos.html')

def galeria_maestria(request):
    galerias = Galeria.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context  = {'imagenes': galerias, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/galeria.html', context=context)