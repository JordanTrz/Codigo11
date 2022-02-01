Proyecto

pasos:
- Se crea react: npm install -g create-react-app
- se crea react-router-dom@5.3.0: npm i react-router-dom@5.3.0
- se instala antdesign
- Se instala tailwind css
- Se instala icons de tailwind css
- axios para servidor

instalación de json-server
npm i json-server
json-server --watch db.json // npm run fake-api

redux
npm install redux
npm install react-redux

se va a utilizar:

los hooks:

useSelector from 'react-redux' -->
Esto se pone en el componente o página en donde se quiere escuchar el cambio de estado


npx node-sass --watch ./src/sass/App.scss ./src/sass/App.css

npm install redux-persist

npm install react-slick --save

npm install --save styled-components

para crear/autocompletar se pone dentro del .js

rfce

significa reactfunctional export component

npx create-react-app "nombre"

se ingresa a la carpeta creada

npm start

para installar sass

- npm install node-sass

para correr el comando para sass:
- npx node-sass ./"documento scss a compilar" ./".css" --watch


___________________________________________________________________

scrapping

pip install request
pip install beautifulsoup4

aplicación de scrappear y obtener el tipo de cambio del día para el programa

tarea para 2 semanas:
realizar el cliend server

hacer aplicación en python para poder registrar computadoras

hacer aplicación para generar reportes: mostrar

la aplicación es de ingreso/registro de ingreso. hora, día

cómo capturar hora de la computadora

fecha límite: 3 de enero

figma:
https://www.figma.com/file/W7SByZ2A1HbN2nwRSnjFG0/Untitled?node-id=0%3A1

key:
300790-ee89e16d-f476-4765-bfb5-22dcc0496518

Semana 02 dia 01
Como crear entorno virtual. Se tien que hacer en la carpeta:

sudo apt install python3-venv
python3 -m venv venv

como activar el venv
- source venv/bin/activate

cuando se pone el pip freeze, el entorno virtual se encuentra vacío. ahí recién se instala flask:

- pip install flask

export FLASK_APP=main
export FLASK_ENV=environment

export FLASK_DEBUG=1

luego para correr Flask se coloca:

- flask run --> Este comando lo que hace es correr Flask con los parámetros por defecto, pero si se quiere correr con los parámetros seteados en código se tiene que correr flask con:

- python3 main.py

Jinja es un template.

Semana 02 dia 01:

se trabaja con firebase, se loguea con cuenta de google.

Se tiene que instalar el firebase para que reconozca la importación:

pip install firebase_admin

Desplegar heroku.
https://www.heroku.com/pricing

Se tiene que instalar:

heroku git:clone -a jterrazos

pip install gunicorn
pip install python-decouple
pip install WhiteNoise

pip freeze > requirements.txt --> Esto es para guardar todos las librerías que se están utilizando

en el .gitignore se debe de poner que no se cargue el venv/ , pero sí tiene que cargar el firebase token

pip install -r requirements.txt

esto instala los comandos que se encuentran dentro del txt. Solo se tiene que poner en el txt lo necesario. no actualizar en cada momento con el:

pip freeze > requirements.txt

clever cloud es base de datos

Para poder utilizar el api se utiliza el thunder Client:

- Se pone New request
- se pone si se quiere un método post o get o delete o put
- se coloca http://localhost:5000/<el enlace que tiene el método>
- Se entra a headers y se coloca: "Content-Type" y "Application/json"
- Luego se va al body (si es un método post) y se ocloca el json con los datos que se quier enviar