from django.db import models

# Create your models here.

class Instalaciones(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}'
