from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class IndexView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request):
    context = {
      'ok':True,
      'message':'El servidor está activo!'
    }
    return Response(context)

class ModelView(APIView):
  def get(self,request):
    dataModel = Model.objects.all()
    serCategoria = ModelSerializer(dataModel,many=True)
    context = {
      'ok':True,
      'content':serCategoria.data
    }
    return Response(context)

class BrandView(APIView):
  def get(self,request):
    dataBrand = Brand.objects.all()
    serBrand = BrandSerializer(dataBrand,many=True)
    context = {
      'ok':True,
      'content':serBrand.data
    }

    return Response(context)

class BrandModelView(APIView):
  def get(self,request,brand_id):
    dataBrand = Brand.objects.get(pk=brand_id)
    serBrand = BrandModelSerializer(dataBrand)
    context = {
      'ok':True,
      'content':serBrand.data
    }

    return Response(context)

class CategoryView(APIView):
  def get(self,request):
    dataCategory = Category.objects.all()
    serCategory = CategorySerializer(dataCategory,many=True)
    context={
      'ok':True,
      'content':serCategory.data
    }
    return Response(context)

class FuelView(APIView):
  def get(self,request):
    dataFuel = Fuel.objects.all()
    serFuel = FuelSerializer(dataFuel,many = True)
    context = {
      'ok':True,
      'content':serFuel.data
    }
    return Response(context)

class TransmissionView(APIView):
  def get(self,request):
    dataTransmission = Transmission.objects.all()
    serTransmission = TransmissionSerializer(dataTransmission,many=True)
    context = {
      'ok':True,
      'content':serTransmission.data
    }
    return Response(context)

class CarView(APIView):
  def get(self,request):
    dataCar = Car.objects.all()
    serCar = CarSerializer(dataCar,many=True)
    context = {
      'ok':True,
      'content':serCar.data
    }
    return Response(context)

class RegionView(APIView):
  def get(self,request):
    dataRegion = Region.objects.all()
    serRegion = RegionSerializer(dataRegion,many=True)
    context = {
      'ok':True,
      'content':serRegion.data
    }
    return Response(context)

class SaleView(APIView):
  def get(self,request):
    dataSale = Sale.objects.all()
    serSale = SaleSerializer(dataSale,many=True)
    context = {
      'ok':True,
      'content':serSale.data
    }
    return Response(context)