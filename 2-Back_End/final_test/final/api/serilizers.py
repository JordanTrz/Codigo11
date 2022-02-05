from rest_framework import serializers
from .models import *


class favoritoSerializer(serializers.ModelSerializer):
  class Meta:
        model = Favorito
        fields = '__all__'
