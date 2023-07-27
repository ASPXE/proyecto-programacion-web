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
    numInt = models.CharField(max_length=5)
    codigoPostal = models.ForeignKey(CodigoPostal, on_delete=models.PROTECT)
    colonia = models.ForeignKey(Colonias, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT)

    def __str__(self):
        return f'ID Centro: {self.id}, Calle: {self.calle}, numExt: {self.numExt}, numInt: {self.numInt}' \
               f'Codigo Postal: {self.codigoPostal}, Colonia: {self.colonia}, Estado: {self.estado}' \
               f'Municipio: {self.municipio}'


