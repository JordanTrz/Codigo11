from django.db import models

# Create your models here.
class Empleado(models.Model):
  nombre = models.CharField(max_length=200)
  email = models.EmailField()

  def __str__(self):
    return self.nombre

class Equipos(models.Model):
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  procesador = models.CharField(max_length=200)
  ram = models.CharField(max_length=200)
  disco = models.CharField(max_length=200)
  video = models.CharField(max_length=200)

  def __str__(self):
    return self.modelo