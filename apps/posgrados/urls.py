from django.urls import path

from apps.posgrados.views import informacion_doctorado, laboratorios, laboratorio
from apps.posgrados.views import informacion_maestria, laboratorio_maestria, laboratorios_maestria

urlpatterns = [
    path('doctorado/informacion-doctorado/', informacion_doctorado, name='informacion-doctorado'),
    path('doctorado/laboratorios/', laboratorios, name='laboratorios'),
    path('doctorado/laboratorios/<int:pk>/', laboratorio, name='laboratorio'),
    path('maestria/informacion-maestria/', informacion_maestria, name='informacion-maestria'),
    path('maestria/laboratorios/', laboratorios_maestria, name='laboratorios-maestria'),
    path('maestria/laboratorios/<int:pk>/', laboratorio_maestria, name='laboratorio-maestria'),
]