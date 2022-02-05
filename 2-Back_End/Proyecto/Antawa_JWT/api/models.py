from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Tablas para Carro
class Brand(models.Model):
  brand_id = models.AutoField(primary_key=True)
  brand_type = models.CharField(max_length=200,verbose_name='Marca')

  def __str__(self):
    return self.brand_type

class Model(models.Model):
  model_id = models.AutoField(primary_key=True)
  model_type = models.CharField(max_length=200,verbose_name='Modelo')
  brand_id = models.ForeignKey(Brand,related_name='Models',to_field='brand_id',on_delete=models.RESTRICT,db_column='brand_id',verbose_name='Marca')

  def __str__(self):
    return self.model_type

class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_type = models.CharField(max_length=200,verbose_name='Categoria')

  def __str__(self):
    return self.category_type

class Fuel(models.Model):
  fuel_id = models.AutoField(primary_key=True)
  fuel_type = models.CharField(max_length=200,verbose_name='combustible')

  def __str__(self):
    return self.fuel_type

class Transmission(models.Model):
  transmission_id = models.AutoField(primary_key=True)
  transmission_type = models.CharField(max_length=200,verbose_name='Transmisión')

  def __str__(self):
    return self.transmission_type

class Car(models.Model):
  car_id = models.AutoField(primary_key=True)
  car_year = models.DateField(verbose_name='Año modelo')
  car_kilometer = models.IntegerField(verbose_name='Kilometraje')
  car_color = models.CharField(max_length=200,verbose_name='Color')
  car_cylinder = models.CharField(max_length=200,verbose_name='Motor')
  car_photo = CloudinaryField('image',default='')
  brand_id = models.ForeignKey(Brand,to_field='brand_id',db_column='brand_id',on_delete=models.RESTRICT,verbose_name='Marca')
  model_id = models.ForeignKey(Model,to_field='model_id',db_column='model_id',on_delete=models.RESTRICT,verbose_name='Model')
  category_id = models.ForeignKey(Category,to_field='category_id',db_column='category_id',on_delete=models.RESTRICT,verbose_name='Categoria')
  fuel_id = models.ForeignKey(Fuel,to_field='fuel_id',db_column='fuel_id',on_delete=models.RESTRICT,verbose_name='Combustible')
  tranmission_id = models.ForeignKey(Transmission,to_field='transmission_id',db_column='transmission_id',on_delete=models.RESTRICT,verbose_name='Transmisión')

# Region
class Region(models.Model):
  region_id = models.AutoField(primary_key=True)
  region_type = models.CharField(max_length=200,verbose_name='Region')

  def __str__(self):
    return self.region_type

# Venta del carro
class Sale(models.Model):
  sale_id = models.AutoField(primary_key=True)
  sale_price = models.IntegerField(verbose_name='Precio')
  sale_date = models.DateTimeField(null=True,verbose_name='Fecha')
  sale_newused = models.BooleanField()
  car_id = models.ForeignKey(Car,to_field='car_id',db_column='car_id',on_delete=models.RESTRICT,verbose_name='Carro')
  usu_id = models.ForeignKey(User,to_field='id',db_column='usu_id',on_delete=models.RESTRICT,verbose_name='Usuario')
  region_id = models.ForeignKey(Region,to_field='region_id',db_column='region_id', on_delete=models.RESTRICT,verbose_name='Region')
