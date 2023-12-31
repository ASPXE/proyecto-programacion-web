from django.db import models

from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from municipios.models import Municipios


# Create your models here.

class Centros(models.Model):
    nombre = models.CharField(max_length=45)
    calle = models.CharField(max_length=60)
    numExt = models.CharField(max_length=5)
    numInt = models.CharField(max_length=5, null=True)
    codigoPostal = models.ForeignKey(CodigoPostal, on_delete=models.SET_NULL, null=True)
    colonia = models.ForeignKey(Colonias, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipios, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'


