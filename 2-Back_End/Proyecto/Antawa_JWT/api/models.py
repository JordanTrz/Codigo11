from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Datos adicionales en otra tabla
class ExtentUser(models.Model):
  user_id = models.AutoField(primary_key=True)
  usu_id = models.ForeignKey(User,to_field='id',db_column='usu_id',on_delete=models.RESTRICT,verbose_name='Usuario')
  user_dni = models.IntegerField(null=True,blank=True)
  user_cellphone = models.IntegerField(null=True,blank=True)
  cellphone_str = str(user_cellphone)
  def __str__(self):
    return self.cellphone_str

# Tablas para Carro
class Make(models.Model):
  make_id = models.AutoField(primary_key=True)
  make_type = models.CharField(max_length=200,verbose_name='Marca')

  def __str__(self):
    return self.make_type

class Model(models.Model):
  model_id = models.AutoField(primary_key=True)
  model_type = models.CharField(max_length=200,verbose_name='Modelo')
  make_id = models.ForeignKey(Make,related_name='Models',to_field='make_id',on_delete=models.RESTRICT,db_column='make_id',verbose_name='Marca')

  def __str__(self):
    return self.model_type

class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_type = models.CharField(max_length=200,verbose_name='Categoria')

  def __str__(self):
    return self.category_type

class Transmission(models.Model):
  transmission_id = models.AutoField(primary_key=True)
  transmission_type = models.CharField(max_length=200,verbose_name='Transmisión')

  def __str__(self):
    return self.transmission_type

class Fuel(models.Model):
  fuel_id = models.AutoField(primary_key=True)
  fuel_type = models.CharField(max_length=200,verbose_name='combustible')

  def __str__(self):
    return self.fuel_type

# Region
class Region(models.Model):
  region_id = models.AutoField(primary_key=True)
  region_type = models.CharField(max_length=200,verbose_name='Region')

  def __str__(self):
    return self.region_type

# Publicación
class SalePost(models.Model):
  salePost_id = models.AutoField(primary_key=True)
  salePost_description = models.CharField(max_length=200,verbose_name='Descripción')
  salePost_yearModel = models.DateField(verbose_name='Año modelo')
  salePost_kilometer = models.IntegerField(verbose_name='Kilometraje')
  salePost_cylinder = models.CharField(max_length=200,verbose_name='Cilindrada')
  salePost_door = models.IntegerField(verbose_name='Número de puertas')
  salePost_color = models.CharField(max_length=200,verbose_name='Color')
  salePost_price = models.IntegerField(verbose_name='Precio dólares')
  salePost_newCar = models.BooleanField(verbose_name='Auto nuevo')
  salePost_photo = CloudinaryField('image',default='')
  salePost_datePost = models.DateTimeField(null=True,verbose_name='Fecha de publicación')
  usu_id = models.ForeignKey(User,to_field='id',db_column='usu_id',on_delete=models.RESTRICT,verbose_name='Usuario')
  model_id = models.ForeignKey(Model,to_field='model_id',db_column='model_id',on_delete=models.RESTRICT,verbose_name='Modelo')
  category_id = models.ForeignKey(Category,to_field='category_id',db_column='category_id',on_delete=models.RESTRICT,verbose_name='Categoria')
  tranmission_id = models.ForeignKey(Transmission,to_field='transmission_id',db_column='transmission_id',on_delete=models.RESTRICT,verbose_name='Transmisión')
  fuel_id = models.ForeignKey(Fuel,to_field='fuel_id',db_column='fuel_id',on_delete=models.RESTRICT,verbose_name='Combustible')
  region_id = models.ForeignKey(Region,to_field='region_id',db_column='region_id', on_delete=models.RESTRICT,verbose_name='Region')