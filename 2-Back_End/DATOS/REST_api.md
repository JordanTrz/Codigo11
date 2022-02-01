# Es parecido a django/flask

- Es un framework de trabajo para crear API

- Se crea un entorno virtual:

python3 -m venv venv

- luego se ingresar al entorno virtual:

source venv/bin/activate

- se debe de instalar o crear un requirements.txt:

Django
djangorestframework

- Luego se crea un nuevo app en django:

python3 manage.py createapp "nombre_de_app"

- Se crea el models que se va a utilizar, se ingresa al models del app creado:

`class Empleado(models.Model):
  nombre = models.CharField(max_length=200,default='')
  email = models.EmailField()
  def __str__(self):
    return self.nombre`

- se ingresa al app creado y se crea los views importando los models creados:

`from .models import Empleado
@api_view(['GET'])
def empleados(request):
  listaEmpleados = Empleado.objects.all()
  print(listaEmpleados)
  dataEmpleados = []
  for d in listaEmpleados:
        dataEmpleados.append({
          'nombre':d.nombre,
          'email':d.email
        })
  return Response({'status':'OK','data':dataEmpleados})`

- Se crea un file urls en el cual se llama al view creado

`from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='index'),
  path('empleados/',views.empleados,name='empleados')
]`

- Este urls que es del app, tiene que ser llamado del url principal del programa

`from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('', include('equipos.urls')),
    path('admin/',admin.site.urls),
]`

- Se ingresa al admin.py del app creado y se importa el models creado:
`admin.site.register(Empleado)`

- En los settings.py del proyecto principal se debe agregar al installed_app el app que se crea y el rest_framework:

`'equipos',
'rest_framework'`

- Se realiza los migrations de la tabla:
- El makemigrations hace que se migue todas los models que se tiene del app creado
`python3 manage.py makemigrations`

- El migrate hace que todos los modelos migren a la base de datos y se creen las tablas
`python3 manage.py migrate`

- Se crea un superuser de la base de datos para poder ingresar en modo admin:
`python3 manage.py createsuperuser`

- Luego se corre el programa:
`python3 manage.py runserver`

- Nos dirijimos a la página con el "/admin", nos logueamos con el superuser y le damos add a la tabla creada (models)

- Luego se puede agregar métodos post al views y mandar por Thunderbolt o Postman