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

class MakeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Make
    fields = '__all__'

class MakeModelSerializer(serializers.ModelSerializer):
  Models = ModelSerializer(many=True,read_only=True)
  class Meta:
    model = Make
    fields = ['make_id','make_type','Models']

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

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'

class SalePostSerializer(serializers.ModelSerializer):
  class Meta:
    model = SalePost
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','first_name','last_name','email','username','password']
    # fields = '__all__'

  #   extra_kwargs = {'password':{'write_only':True}}

  # def create(self,validated_data):
  #   password = validated_data.pop('password',None)
  #   instance = self.Meta.model(**validated_data)
  #   if password is not None:
  #     instance.set_password(password)
  #   instance.save()
  #   return instance

class ExtentUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = ExtentUser
    fields = '__all__'
