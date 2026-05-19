from django.urls import path

from apps.slides.views import index_doctorado, linea_investigacion, index
from apps.slides.views import index_maestria, linea_investigacion_maestria, ligas_interes_maestria

urlpatterns = [
    path('', index, name='index'),
    path('doctorado/', index_doctorado, name='index-doctorado'),
    path('doctorado/linea-investigacion/<int:pk>', linea_investigacion, name='linea-investigacion'),
    path('maestria/', index_maestria, name='index-maestria'),
    path('maestria/linea-investigacion/<int:pk>', linea_investigacion_maestria, name='linea-investigacion-maestria'),
    path('maestria/ligas-interes/', ligas_interes_maestria, name='ligas-interes'),
]