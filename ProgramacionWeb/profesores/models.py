from django.db import models

from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from municipios.models import Municipios
from gradoEstudios.models import gradoEstudios


# Create your models here.

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellidoP = models.CharField(max_length=40)
    apellidoM = models.CharField(max_length=40)
    calle = models.CharField(max_length=60)
    numExt = models.CharField(max_length=5)
    numInt = models.CharField(max_length=5)
    colonia = models.ForeignKey(Colonias, on_delete=models.PROTECT)
    cp = models.ForeignKey(CodigoPostal, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)
    gradoEstudios = models.ForeignKey(gradoEstudios, on_delete=models.PROTECT)

    def __str__(self):
        return f'ID Profesor: {self.id}, Nombre: {self.nombre}, Apellido Paterno: {self.apellidoP},' \
               f'Apellido Materno: {self.apellidoM}, Calle: {self.calle}, numExt: {self.numExt},' \
               f'numInt: {self.numInt}, Colonia: {self.colonia}, Codigo Postal:{self.cp},' \
               f'Municipio: {self.municipio}, Estado: {self.estado}, Grado Estudio: {self.gradoEstudios}'
