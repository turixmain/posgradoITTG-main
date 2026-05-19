from django.contrib import admin

# Register your models here.

from apps.slides.models import Slides

admin.site.register(Slides)