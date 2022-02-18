Django

- Se tiene que crear primero un entorno virtual

python3 -m venv venv

- Se tiene que instalar django:

pip3 install django

- Luego se crea un proyecto

django-admin startproject "nombre de proyecto"

- Se ingresa a la carpeta y se lanza el programa:

python3 manage.py runserver

- Se crea aplicación del proyecto:

python3 manage.py startapp "nombre de app"

Modelo vista template, es lo que se encuentra dentro del app del proyecto de django

Se tiene una estructura:

View: Es la ruta en django
Template: Es el HTML
Model:

python3 manage.py migrate --> para que se migren las classes a las tablas de la base de datos.

python3 manage.py createsuperuser --> Es para poder crear usuario de la base de datos

python3 manage.py makemigrations app --> Es para poder migrar los datos de la aplicación app

Luego se pone de nuevo la migración con todos los campos migrados:
python3 manage.py migrate

Se puede realizar una migración única:
python3 manage.py sqlmigrate 0001_... o 0002_...

------

# Migrar/conectar django con base de datos MySQL:

Se ingresa al archivo settigns.py, se busca la línea 75 y se cambia la configuración según el link que te indica. y se cambia "engine" por mysql

luego en la base de datos, se crea la tabla de datos con el mismo nombre para que se pueda realizar el migrate

python3 manage.py migrate

-------

Se ingresa al shell para poder interactuar con python

python3 manage.py shell

Se tiene que importar de la base de datos las clases:

from app.models import Autor,Receta,Comentario

Se instancia de la clase y se le coloca los argumentos

a = Autor(nombre="jordan terrazos", email="jt@gmail.com")

luego se coloca:
"instancia".save()
a.save()

Se puede instanciar objectos según la clase:
primer = Autor.objects.get(pk=1)
primer.nombre

Para visualizar todos los datos creados:
"nombre de clase".objects.all()

Para poder hacer un "select" como en mysql:
primer = Autor.objects.get(pk=1)

Para poder instanciar y crear datos ejemplo:
r1 = Receta.objects.create(titulo="asdfasf",preparacion="adsfasf",autor="si es foreign key se llama a otra instacia que ya se haya creado")

Receta.objects.exclude(ingredientes_startswith="A")
Receta.objects.filter(pk=1).update(titulo="Huevos revueltos")
Receta.objects.all().count()

----

Se tiene que crear un archivo urls.py dentro de la carpeta app, ahí llamo al template html que se va a mapear. Por lo que se crea una carpeta dentro de app que obligatorio debe tener el nombre de "templates". dentro de template se crea un index.html. Luego, al urls principal(el de la carpeta que se creó)


En el formulario se debe colocar un código:
{% csrf_token %}

------

Para poder agregar imagen se tiene que utilizar/importar en models el "IMAGEFIELD"

Luego en el admin se carga, según las tablas creadas, las imágenes que se desee.

Para que se pueda observar en la página se debe de agregar ciertas cosas:

- En "settings" se agrega:
MEDIA_URL = '/media/'

- En URLS del proyecto se importa:
from django.conf import settings
from django.conf.urls.static import static

y se agrega:

urlpatterns = [
    path('', include('tienda.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)







