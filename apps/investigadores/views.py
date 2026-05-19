from django.shortcuts import render, get_object_or_404

from apps.investigadores.models import Docentes, Estudiantes, Tutorias, Generacion
from apps.investigadores.models import TiempoParcial, TiempoCompleto
from apps.lineas_investigacion.models import LineasInvestigacion
from apps.posgrados.models import Laboratorios

def docentes_doctorado(request):
    docentes_tiempo_parcial = TiempoParcial.objects.all().filter(posgrado=1)
    docentes_tiempo_completo = TiempoCompleto.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'maestros': docentes_tiempo_parcial, 'docentes': docentes_tiempo_completo, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/docentes.html', context=context)

def docente_profile(request, pk=None):
    docente_profile = get_object_or_404(Docentes, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'docente': docente_profile, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/profile.html', context=context)

def estudiantes_doctorado(request):
    generacion  = Generacion.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'generacion': generacion, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/estudiantes.html', context=context)

def estudiante_profile(request, pk=None):
    estudiante_profile = get_object_or_404(Estudiantes, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'estudiante': estudiante_profile, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/estudiantes_profile.html', context=context)

def tutorias_list(request):
    tutorias = Tutorias.objects.all().order_by('generacion')
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=1)
    context = {'tutorias': tutorias, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/tutorias.html', context=context)

def docentes_maestria(request):
    docentes_tiempo_parcial = TiempoParcial.objects.all().filter(posgrado=2)
    docentes_tiempo_completo = TiempoCompleto.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'maestros': docentes_tiempo_parcial, 'docentes': docentes_tiempo_completo, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/docentes.html', context=context)

def docente_profile_maestria(request, pk=None):
    docente_profile = get_object_or_404(Docentes, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'docente': docente_profile, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/profile.html', context=context)

def estudiantes_maestria(request):
    generacion  = Generacion.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'generacion': generacion, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/estudiantes.html', context=context)

def estudiante_profile_maestria(request, pk=None):
    estudiante_profile = get_object_or_404(Estudiantes, pk=pk)
    laboratorios = Laboratorios.objects.all()
    lineas = LineasInvestigacion.objects.all().filter(posgrado=2)
    context = {'estudiante': estudiante_profile, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/maestria/estudiantes_profile.html', context=context)