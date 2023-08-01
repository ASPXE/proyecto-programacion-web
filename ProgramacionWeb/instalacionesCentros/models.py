from django.db import models

from centros.models import Centros
from instalaciones.models import Instalaciones


# Create your models here.

class InstalacionesCentros(models.Model):
    instalacion = models.ForeignKey(Instalaciones, on_delete=models.SET_NULL, null=True)
    centro = models.ForeignKey(Centros, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'ID IC: {self.id}, Instalacion: {self.instalacion}, Centro: {self.centro}'
