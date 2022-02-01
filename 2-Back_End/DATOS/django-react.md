En django se tiene que devolver un json para que lo pueda consumir el front.

- Se deben crear los modelos para que estos sean registrados en la base de datos.

- Se debe de crear los views para mostrar los valores de la base de datos.

- Se debe crear un archivo con nombre `serializer` con el fin de poder enviar los datos a la base de datos, este archivo importa los models y tmb serializers del rest_framework

`from rest_framework import serializers
from .models import Room`

`class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip')`

El view tmb importa el rest_framework para crear createapiview

----------------------------

Se debe crear otro app para el frontend

python3 manage.py createapp frontend

una vez dentro se tiene que crear las carpetas:

- static --> css / frontend / images
- templates
- src --> components

luego dentro de la carpeta frontend de app, se debe instalar npm con la línea de comando:

`npm init -y`

luego tmb se pone:
`npm i webpack webpack-cli --save-dev`

Luego se tiene que instalar babel, esto es para que el código pueda funcionar en versiones antiguas de exploradores:
`npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`

`npm install @babel/plugin-proposal-class-properties`

Luego se instala react:
`npm i react react-dom --save-dev`
`npm install react-router-dom`


luego se puede instalar material UI:
`npm install @material-ui/core`
`npm install @material-ui/icons`
