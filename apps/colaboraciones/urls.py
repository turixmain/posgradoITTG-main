from django.urls import path

# Views from colaboraciones
from apps.colaboraciones.views import colaboraciones_academicas, mision_vision, vinculacion, procedimientos, galeria_doctorado
from apps.colaboraciones.views import colaboraciones_academicas_maestria, mision_vision_maestria, vinculacion_maestria, procedimientos_maestria, galeria_maestria

urlpatterns = [
    path('doctorado/colaboraciones-academicas/', colaboraciones_academicas, name='colaboraciones-academicas'),
    path('doctorado/mision-vision/', mision_vision, name='mision-vision'),
    path('doctorado/vinculacion/', vinculacion, name='vinculacion'),
    path('doctorado/procedimientos/', procedimientos, name='procedimientos'),
    path('doctorado/galeria/', galeria_doctorado, name='galeria-doctorado'),
    path('maestria/colaboraciones-academicas/', colaboraciones_academicas_maestria, name='colaboraciones-academicas-maestria'),
    path('maestria/mision-vision/', mision_vision_maestria, name='mision-vision-maestria'),
    path('maestria/vinculacion/', vinculacion_maestria, name='vinculacion-maestria'),
    path('maestria/procedimientos/', procedimientos_maestria, name='procedimientos-maestria'),
    path('maestria/galeria/', galeria_maestria, name='galeria-maestria'),
]