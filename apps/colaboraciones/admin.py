from django.contrib import admin

# Register your models here.

from apps.colaboraciones.models import Colaboraciones, Galeria

admin.site.register(Colaboraciones)
admin.site.register(Galeria)