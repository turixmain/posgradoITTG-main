from django.urls import path

from apps.tesis.views import tesis_disponibles

urlpatterns = [
    path('doctorado/tesis-disponibles/', tesis_disponibles, name='tesis-disponibles'),
]