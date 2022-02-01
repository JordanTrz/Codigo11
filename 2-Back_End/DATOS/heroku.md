Heroku:

PAra instalar se debe loguear primero en la página


cloudinary es para poder alojar las imágenes. Se coloca en el settings en el installed_apps

whitenoise es para poder trabajar con archivos staticos, se debe agregar en el middleware

whitenoise.middleware.WhiteNoiseMiddleware

De igual manera, se trabaja con herokupostgres, para poder trabajar con esta bd se tiene que cambiar el settings en databases liean 83-85

En el static URL linea 128-130, se debe agregar el static root:

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR,'statis')
)


____________

Una vez se tiene desplegado el proyecto en heroku, se puede realizar el migrate y makemigrations dando el comando:

heroku run python manage.py makemigrations

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

