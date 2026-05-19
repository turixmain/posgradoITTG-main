from django.shortcuts import render, get_object_or_404

# Create your views here.

from apps.slides.models import Slides
from apps.lineas_investigacion.models import LineasInvestigacion
from apps.investigadores.models import TiempoParcial, TiempoCompleto
from apps.posgrados.models import Posgrados
from apps.posgrados.models import Laboratorios

def index_doctorado(request):
    carrousel = Slides.objects.all().filter(posgrado=1)
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    posgrados = Posgrados.objects.all()
    return render(request, 'components/doctorado/index.html', {'carrousels': carrousel, 'posgrados': posgrados, 'lineas': lineas_investigacion, 'laboratorios': laboratorios})

def navbar_doctorado(request):
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    return render(request, 'components/doctorado/navbar.html', {'lineas': lineas_investigacion, 'laboratorios': laboratorios})

def linea_investigacion(request, pk=None):
    linea = get_object_or_404(LineasInvestigacion, pk=pk)
    docentes_tiempo_parcial = TiempoParcial.objects.all().filter(posgrado=1)
    docentes_tiempo_completo = TiempoCompleto.objects.all().filter(posgrado=1)
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=1)
    laboratorios = Laboratorios.objects.all()
    context = {'linea': linea, 'maestros': docentes_tiempo_parcial, 'docentes': docentes_tiempo_completo, 'lineas': lineas_investigacion, 'laboratorios': laboratorios }
    return render(request, 'components/doctorado/linea_investigacion.html', context=context)

def index(request):
    return render(request, 'components/index.html')

def index_maestria(request):
    carrousel = Slides.objects.all().filter(posgrado=2)
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    posgrados = Posgrados.objects.all()
    return render(request, 'components/maestria/index.html', {'carrousels': carrousel, 'posgrados': posgrados, 'lineas': lineas_investigacion, 'laboratorios': laboratorios})

def navbar_doctorado(request):
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    return render(request, 'components/maestria/navbar.html', {'lineas': lineas_investigacion, 'laboratorios': laboratorios})

def linea_investigacion_maestria(request, pk=None):
    linea = get_object_or_404(LineasInvestigacion, pk=pk)
    docentes_tiempo_parcial = TiempoParcial.objects.all().filter(posgrado=2)
    docentes_tiempo_completo = TiempoCompleto.objects.all().filter(posgrado=2)
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    context = {'linea': linea, 'maestros': docentes_tiempo_parcial, 'docentes': docentes_tiempo_completo, 'lineas': lineas_investigacion, 'laboratorios': laboratorios }
    return render(request=request, template_name='components/maestria/linea_investigacion.html', context=context)

def ligas_interes_maestria(request):
    lineas_investigacion = LineasInvestigacion.objects.all().filter(posgrado=2)
    laboratorios = Laboratorios.objects.all()
    context = { 'lineas': lineas_investigacion, 'laboratorios': laboratorios }
    return render(request=request, template_name='components/maestria/ligas_interes.html', context=context)