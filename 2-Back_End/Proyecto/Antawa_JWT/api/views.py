from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

from .models import *
from .serializers import *

from rest_framework import status, permissions

class IndexView(APIView):
  permission_classes = (IsAuthenticated,)
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

class MakeView(APIView):
  def get(self,request):
    dataBrand = Make.objects.all()
    serBrand = MakeSerializer(dataBrand,many=True)
    context = {
      'ok':True,
      'content':serBrand.data
    }

    return Response(context)

class MakeModelView(APIView):
  def get(self,request,brand_id):
    dataBrand = Make.objects.get(pk=brand_id)
    serBrand = MakeModelSerializer(dataBrand)
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

class RegionView(APIView):
  def get(self,request):
    dataRegion = Region.objects.all()
    serRegion = RegionSerializer(dataRegion,many=True)
    context = {
      'ok':True,
      'content':serRegion.data
    }
    return Response(context)

class SalePostView(APIView):
  def get(self,request):
    dataSale = SalePost.objects.all()
    serSale = SalePostSerializer(dataSale,many=True)
    context = {
      'ok':True,
      'content':serSale.data
    }
    return Response(context)


class UserCreateView(APIView):
  permission_classes = (permissions.AllowAny,)

  def post(self,request):
    serUser = UserSerializer(data=request.data)
    if serUser.is_valid():
      password = serUser.validated_data.get('password')
      serUser.validated_data['password'] = make_password(password)
      new_user = serUser.save()
      if new_user:
        context = {
          'ok':True,
          'content': serUser.data
        }
        return Response(context)
      return Response(serUser.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
  permission_classes = (IsAuthenticated,)
  def get(self,request,user_id):
    dataUserDetail = User.objects.get(pk=user_id)
    serUserDetail = UserSerializer(dataUserDetail)
    context = {
      'ok':True,
      'content':serUserDetail.data
    }

    return Response(context)

  def put(self,request,user_id):
    dataUserDetail = User.objects.get(pk=user_id)
    serUserDetail = UserSerializer(dataUserDetail, data=request.data)
    context = {
      'ok':True,
      'content':serUserDetail.data
    }
    return Response(context)

  def delete(self,request,user_id):
    dataUserDetail = User.objects.delete(pk=user_id)
    serUserDetail = UserSerializer(dataUserDetail)
    context = {
      'ok':True,
      'content': serUserDetail.data
    }
    return Response(context)

class ExtentUserView(APIView):
  def get(self,request):
    dataUserMoreData = ExtentUser.objects.all()
    serUserMoreData = ExtentUserSerializer(dataUserMoreData,many=True)
    context = {
      'ok':True,
      'content':serUserMoreData.data
    }
    return Response(context)

  def post(self,request):
    serUserMoreData = ExtentUserSerializer(data=request.data)
    serUserMoreData.is_valid()
    serUserMoreData.save()
    context = {
      'ok':True,
      'content':serUserMoreData.data
    }
    return Response(context)