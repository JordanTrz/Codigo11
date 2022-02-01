from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Empleado,Equipos

from .serializers import EmpleadoSerializer,EquipoSerializer

# Create your views here.

@api_view(['GET'])
def index(response):
      data = {'mensaje':'Bienvenidos al proyecto con django REST_FRAMEWORK'}
      return Response(data)


@api_view(['GET','POST'])
def showEmpleados(request):
  if request.method == 'GET':
    listaEmpleados = Empleado.objects.all()
    serEmpleados = EmpleadoSerializer(listaEmpleados,many=True)
    return Response(serEmpleados.data)

  elif request.method == 'POST':
    serEmpleados = EmpleadoSerializer(data=request.data)
    if serEmpleados.is_valid():
      serEmpleados.save()
      return Response(serEmpleados.data)
    else:
      return Response(serEmpleados.errors)

@api_view(['GET','POST'])
def showEquipos(request):
  if request.method == 'GET':
    listaEquipos = Equipos.objects.all()
    serListaEquipos = EquipoSerializer(listaEquipos,many=True)
    return Response(serListaEquipos.data)
  elif request.method == 'POST':
    serEquipos = EquipoSerializer(data=request.data)
    if serEquipos.is_valid():
      serEquipos.save()
      return Response(serEquipos.data)
    else:
      return Response(serEquipos.errors)