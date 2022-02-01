from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializers import *

class Index(APIView):
  def get(self,request):
    context = {
      'mensaje':'Servidor Activo'
    }
    return Response(context)

class LogRegView(APIView):
  def get(self,request):
    dataLogReg = LogReg.objects.all()
    serLogReg = LogRegSerializer(dataLogReg,many=True)
    context = {
      'ok':True,
      'content':serLogReg.data
    }
    return Response(context)

  def post(self,request):
    serLogReg = LogRegSerializer(data=request.data)
    serLogReg.is_valid(raise_exception=True)
    serLogReg.save()
    context = {
      'ok':True,
      'content':serLogReg.data
    }
    return Response(context)

class LogRegDetailView(APIView):
  def get(self,request,usuario_id):
    dataLogReg = LogReg.objects.get(pk=usuario_id)
    serLogReg = LogRegSerializer(dataLogReg)
    context = {
      'ok':True,
      'content':serLogReg.data
    }
    return Response(context)

  def put(self,request,usuario_id):
    dataLogReg = LogReg.objects.get(pk=usuario_id)
    serLogReg = LogRegSerializer(dataLogReg,data=request.data)
    serLogReg.is_valid(raise_exception=True)
    serLogReg.save()
    context = {
      'ok':True,
      'content':serLogReg.data
    }
    return Response(context)

  def delete(self,request,usuario_id):
    dataLogReg = LogReg.objects.get(pk=usuario_id)
    serLogReg = LogRegSerializer(dataLogReg)
    dataLogReg.delete()
    context = {
      'ok':True,
      'content':serLogReg.data
    }
    return Response(context)