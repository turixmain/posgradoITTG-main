from django.shortcuts import render

from apps.tesis.models import Tesis
from apps.posgrados.models import Laboratorios
from apps.lineas_investigacion.models import LineasInvestigacion

# Create your views here.
# from django.contrib import messages

# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')

def tesis_disponibles(request):
    tesis        = Tesis.objects.all().filter(asignada=False)
    laboratorios = Laboratorios.objects.all()
    lineas       = LineasInvestigacion.objects.all().filter(posgrado=1)
    context      = { 'tesis': tesis, 'laboratorios': laboratorios, 'lineas': lineas }
    return render(request=request, template_name='components/doctorado/tesis.html', context=context)