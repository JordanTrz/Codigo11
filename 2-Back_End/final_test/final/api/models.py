from django.db import models

# Create your models here.
class Favorito(models.Model):
  titulo = models.CharField(max_length=200,verbose_name='Titulo')
  url = models.CharField(max_length=200,verbose_name='URL')
  fecha_registro = models.DateTimeField(null=True,verbose_name='Fecha de Registro')

  def __str__(self):
    return self.titulo