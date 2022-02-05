from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serilizers import *

# Create your views here.

class indexView(APIView):
  def get(self,request):
    context={
      'mensaje':'Servidor Conectado'
    }
    return Response(context)

class favoritoView(APIView):
  def get(self,request):
    dataFavorito = Favorito.objects.all()
    serFavorito = favoritoSerializer(dataFavorito,many=True)
    context = {
      'ok':True,
      'content':serFavorito.data
    }
    return Response(context)

  def post(self,request):
    serFavorito = favoritoSerializer(data=request.data)
    serFavorito.is_valid(raise_exception=True)
    serFavorito.save()
    # context = {
    #   'ok':True,
    #   'content':serFavorito
    # }
    # return Response(context)
    return Response(serFavorito.data)

class favoritoNewView(APIView):
  def get(self,request,id):
    dataFavoritoNew = Favorito.objects.get(pk=id)
    serDataFavoritoNew = favoritoSerializer(dataFavoritoNew)
    # context={
    #   'ok':True,
    #   'content':serDataFavoritoNew.data
    # }
    # return Response(context)
    return Response(serDataFavoritoNew.data)

  def put(self,request,id):
    dataFavoritoNew = Favorito.objects.get(pk=id)
    serDataFavoritoNew = favoritoSerializer(dataFavoritoNew,data=request.data)
    serDataFavoritoNew.is_valid(raise_exception=True)
    serDataFavoritoNew.save()
    # context = {
    #   'ok':True,
    #   'content':serDataFavoritoNew.data
    # }
    # return Response(context)
    return Response(serDataFavoritoNew.data)

  def delete(self,request,id):
    dataFavoritoNew = Favorito.objects.get(pk=id)
    serDataFavoritoNew = favoritoSerializer(dataFavoritoNew)
    dataFavoritoNew.delete()
    # context = {
    #   'ok':True,
    #   'content':serDataFavoritoNew.data
    # }
    # return Response(context)
    return Response(serDataFavoritoNew.data)