from django.db import models

# Create your models here.

class Paises(models.Model):
    nombre = models.CharField(max_length=45)