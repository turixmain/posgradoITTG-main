from django.db import models

class BaseModel(models.Model):
    active     = models.BooleanField(default=True)
    created_at = models.DateTimeField('Date and time of object created', auto_now_add=True)
    updated_at = models.DateTimeField('Date and time of object updated', auto_now=True)

    class Meta:
        abstract = True