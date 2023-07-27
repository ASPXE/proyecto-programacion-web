from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=45)
    costo = models.FloatField()

    def __str__(self):
        return f'ID Servicio: {self.id}, Nombre: {self.nombre}, Costo: {self.costo}'