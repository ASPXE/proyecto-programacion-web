from django.db import models

from estados.models import Estados


# Create your models here.

class Municipios(models.Model):
    nombre = models.CharField(max_length=40)
    estado = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'
