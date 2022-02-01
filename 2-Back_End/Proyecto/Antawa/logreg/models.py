from django.db import models

# Create your models here.

class LogReg(models.Model):
      nombre = models.CharField(max_length=200)
      apellido = models.CharField(max_length=200)
      email = models.EmailField()
      contrasena = models.CharField(max_length=200)
      dni = models.IntegerField()
      celular = models.IntegerField()

      def __str__(self):
        return self.email