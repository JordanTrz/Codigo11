Se instala el virtual box

una vez instalado se descargar la versiṕon de ubuntu pero tipo server

se abre virtual box y se agrega el iso de ubuntu. Se configura para que el tipo de conexión de red esté en bridge/puente. Y el iso que cargue como modo cd room

Una vez iniciado el virtual, se pone "hecho a todo" pero en la parte de red se debe de configurar ya que se debe de especificar la dirección ip, esta tiene que ponerse en modo manual. Para poder configurar la ip tenemos que saber a qué dirección ip estamos conectados. para eso se tiene que poner el comando

`ifconfig`

en una terminal. Ahí se va a visualizar, en este caso nuestro ip config es 192.168.0.110.

El gateway tiene que ir: 192.168.0.0/24
Y se coloca la dirección ip de forma manual: 192.168.0.100
las máscaras tienen que estar configuradas con 8.8.8.8,8.8.4.4 que son las ip's de los servidores de google para poder comunicarnos hacia el exterior mediante internet

se pone ok y se sigue poniendo ok hasta que figure una opción de cargar
`openssh`. Esto es importante ya que mediante el ssh vamos a poner conectarnos con el servidor

Luego se coloca los nombres del servidor, el usuario y la contraseña, esto se tiene que guardar ya que con esto se ingresa al servidor.

se reinicia el virtual box y luego nos conectamos con el login.

Una vez se encuentra corriendo el servidor se conecta mediante ssh.

Se abre terminal y se coloca:

`ssh codigo@192.168.0.100` y luego se tiene que colocar la contraseña y listo, se habrá conectado.

- instalación de python

Primero se revisa qué versión se tiene de python. Luego se tiene que instalar el venv y el pip

`sudo apt install python3.8-venv`
`sudo apt install python3-pip`

se ingresa al
`activate source/bin/activate`
`pip3 install django`

Se tiene que crear un projecto

django-admin startproject "nombre"

se ingresa al settings y se edita con vim

`vim settings.py`

y se pone para que sea allowed para todos

se vuelve a correr todo:

`python3 manage.py runserver 0.0.0.0:8000`

para cerrar el servidor se colocar en el terminal:

`sudo init 0`