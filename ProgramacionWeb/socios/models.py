from django.db import models

from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from municipios.models import Municipios


# Create your models here.

class Socios(models.Model):
    nombres = models.CharField(max_length=40)
    apellidoP = models.CharField(max_length=40)
    apellidoM = models.CharField(max_length=40, null=True)
    calle = models.CharField(max_length=60)
    numExt = models.CharField(max_length=5)
    numInt = models.CharField(max_length=5, null=True)
    colonia = models.ForeignKey(Colonias, on_delete=models.SET_NULL, null=True)
    cp = models.ForeignKey(CodigoPostal, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipios, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    mensualidad = models.FloatField()

    def __str__(self):
        return f'ID Socio: {self.id}, Nombres: {self.nombres}, Apellido Paterno: {self.apellidoP}, Apellido Materno: {self.apellidoM},' \
               f'Calle: {self.calle}, numExt: {self.numExt}, numInt: {self.numInt}, Colonia: {self.colonia}, Codigo Postal: {self.cp},' \
               f'Municipio: {self.municipio}, Estado: {self.estado}, Mensualidad: {self.mensualidad}'
