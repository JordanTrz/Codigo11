# Se tiene que instalar con el pip

`pip3 install djangorestframework-simplejwt`

la documentación se encuentra en la pag: https://jwt.io/

luego se tiene que colocar en el settings en el installed apps, restframework
se tiene que poner los paths en la urls. Todo esto según la página

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

Para cambiar el tiempo de duración del token
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

Se corre el servidor y se ingresa al path del jwt

http://localhost:8000/api/token

se selecciona rawdata y se ingresa admin admin y te va a arrojar un token,
el token access dura 30 segundos y el otro token dura 10 minutos, esto se puede cambiar

ahora con el token se ingresa al thunderclient o al postman y se manda en la opción auth/bearer, si sale 200 es que se logueó correctamente.

tarea:
investigar cómo enviar el token desde React

____________________________________________________

para poder importar y tener las views de una base ya creada y con datos:

python manage.py inspectdb

python manage.py inspectdb > base/models.py