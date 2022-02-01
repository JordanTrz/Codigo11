from rest_framework import serializers
from .models import Empleado,Equipos

class EmpleadoSerializer(serializers.ModelSerializer):
      class Meta:
            model = Empleado
            fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Equipos
    fields = '__all__'