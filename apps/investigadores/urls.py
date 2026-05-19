from django.urls import path

from apps.investigadores.views import docentes_doctorado, docente_profile, tutorias_list
from apps.investigadores.views import estudiantes_doctorado, estudiante_profile
from apps.investigadores.views import docentes_maestria, estudiante_profile_maestria
from apps.investigadores.views import docente_profile_maestria, estudiantes_maestria # , tutorias_list_maestria

urlpatterns = [
    path('doctorado/docentes/', docentes_doctorado, name='docentes-doctorado'),
    path('doctorado/docentes/<int:pk>', docente_profile, name='docente-profile'),
    path('doctorado/estudiantes/', estudiantes_doctorado, name='estudiantes-doctorado'),
    path('doctorado/estudiantes/<int:pk>', estudiante_profile, name='estudiante-profile'),
    path('doctorado/tutorias/', tutorias_list, name='tutorias'),
    path('maestria/docentes/', docentes_maestria, name='docentes-maestria'),
    path('maestria/docentes/<int:pk>', docente_profile_maestria, name='docente-profile-maestria'),
    path('maestria/estudiantes/', estudiantes_maestria, name='estudiantes-maestria'),
    path('maestria/estudiantes/<int:pk>', estudiante_profile_maestria, name='estudiante-profile-maestria'),
    # path('maestria/tutorias/', tutorias_list_maestria, name='tutorias-maestria'),
]