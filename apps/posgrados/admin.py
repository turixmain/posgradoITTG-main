from django.contrib import admin

# Register your models here.
from apps.posgrados.models import Posgrados, Laboratorios

admin.site.register(Posgrados)
admin.site.register(Laboratorios)