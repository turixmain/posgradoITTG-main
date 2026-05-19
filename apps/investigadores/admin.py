from django.contrib import admin

# Register your models here.
from apps.investigadores.models import Docentes, Estudiantes, Generacion, Tutorias
from apps.investigadores.models import TiempoCompleto, TiempoParcial

admin.site.register(Docentes)
admin.site.register(Estudiantes)
admin.site.register(Generacion)
admin.site.register(Tutorias)
admin.site.register(TiempoCompleto)
admin.site.register(TiempoParcial)