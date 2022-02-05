Heroku:

Para instalar se debe loguear primero en la página
Se crea un nuevo app en heroku
se ingresa a la carpeta de Heroku que se tiene fuera de todo el github
se pone:

`heroku git:clone -a "nombre del proyecto"`

una vez hecho eso se ingresa a la pagina y se agregar un add on, que va a ser posgres heroku y se da submit form

en los requirements del poryecto se tiene que agregar librerías para los archivos static

cloudinary es para poder alojar las imágenes. Se coloca en el settings en el installed_apps

whitenoise es para poder trabajar con archivos staticos, se debe agregar en el middleware

whitenoise.middleware.WhiteNoiseMiddleware


el requirements es:

django==3.2
djangorestframework
djangorestframework-simplejwt
cloudinary
python-decouple
django-cors-headers
psycopg2
dj-database-url
gunicorn
whitenoise


De igual manera, se trabaja con herokupostgres, para poder trabajar con esta bd se tiene que cambiar el settings en databases liean 83-85

En el static URL linea 128-130, se debe agregar el static root:

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR,'statis')
)


____________

Una vez se tiene desplegado el proyecto en heroku, se puede realizar el migrate y makemigrations dando el comando:

`heroku run python manage.py makemigrations`

`heroku run python manage.py migrate`

`heroku run python manage.py createsuperuser`


Esto es el gitignore
https://www.toptal.com/developers/gitignore/api/django

_________________________________

Se puede trabajar con dos entornos de desarrollo, uno para desplegar en heroku y otro para trabajar localmente

El settings del proyecto se copia y se pega en la misma carpeta, se cambia de nombre a: settings-dev

Dentro del settings-dev se tiene que eliminar todo lo referente a whitenoise, poner el debug a True y quitar el '*' a allowed users

El comando para que se pueda correr desde otro settings:

`python3 manage.py runserver --settings=shop.settings-dev`