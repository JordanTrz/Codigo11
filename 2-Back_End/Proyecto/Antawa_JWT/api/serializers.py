from rest_framework import serializers

from .models import *

class ModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Model
    fields = '__all__'

  # def to_representation(self,instance):
  #       representation = super().to_representation(instance)
  #       # representation['plato_img'] = instance.plato_img.url
  #       return representation

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'

class BrandModelSerializer(serializers.ModelSerializer):
  Models = ModelSerializer(many=True,read_only=True)
  class Meta:
    model = Brand
    fields = ['brand_id','brand_type','Models']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class FuelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fuel
    fields = '__all__'

class TransmissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transmission
    fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = '__all__'