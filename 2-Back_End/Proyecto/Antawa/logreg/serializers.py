from rest_framework import serializers

from .models import *

class LogRegSerializer(serializers.ModelSerializer):
  class Meta:
    model = LogReg
    fields = '__all__'