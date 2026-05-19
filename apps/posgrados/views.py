from django.shortcuts import render
from django.shortcuts import get_object_or_404

from apps.posgrados.models import Laboratorios
from apps.lineas_investigacion.models import LineasInvestigacion

def informacion_doctorado(request):
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/informacion_posgrado.html', context=context)

def laboratorios(request):
    laboratorios = Laboratorios.objects.all()
    context = {'laboratorios': laboratorios }
    return render(request=request, template_name='components/doctorado/laboratorios.html', context=context)

def laboratorio(request, pk=None):
    laboratorio = get_object_or_404(Laboratorios, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'laboratorio': laboratorio, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/laboratorio-profile.html', context=context)

def informacion_maestria(request):
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/informacion_posgrado.html', context=context)

def laboratorios_maestria(request):
    laboratorios = Laboratorios.objects.all()
    context = {'laboratorios': laboratorios }
    return render(request=request, template_name='components/maestria/laboratorios.html', context=context)

def laboratorio_maestria(request, pk=None):
    laboratorio = get_object_or_404(Laboratorios, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'laboratorio': laboratorio, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/laboratorio-profile.html', context=context)