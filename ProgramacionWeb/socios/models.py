from django.db import models

from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from municipios.models import Municipios


# Create your models here.

class Socios(models.Model):
    nombres = models.CharField(max_length=40)
    apellidoP = models.CharField(max_length=40)
    apellidoM = models.CharField(max_length=40)
    calle = models.CharField(max_length=60)
    numExt = models.CharField(max_length=5)
    numInt = models.CharField(max_length=5)
    colonia = models.ForeignKey(Colonias, on_delete=models.PROTECT)
    cp = models.ForeignKey(CodigoPostal, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)
    mensualidad = models.FloatField()
