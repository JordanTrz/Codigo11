# Se crea dos carpetas, uno backend y otro front end

## En el backend se crea un entorno virtual

Se tiene que instalar primero la librería para poder tener el virtual environment.

` pip3 install virtualenv `

luego se tiene que instalar el venv

`virtualenv -p venv venv`

o se puede realizar

`python3 -m venv venv`

Para poder ingresar al virtual environment se tien que ingresar el código:

`source venv/bin/activate`

y para poder salir o desactivar se utiliza:

`deactivate`

# Instalando extensiones para trabajar back

Una vez en el venv, se tiene que instalar:

`pip3 install flask Flask-PyMongo flask-cors`

# Mongo DB

Para poder ver si mongodb se está ejecutando se tiene que poner el siguiente código:

`service mongod status`

Para poder detener mongodb es:

`service mongod stop`

Para poder arrancar mongodb es:

`service mongod start`

sudo service mongod restart
sudo service mongod stop
sudo service mongod start

sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock
sudo service mongod restart

## SQLALCHEMY and FLASK-SQLALCHEMY ORM/ODM

el sqlalchemy hace que se puedea ingresar y modificar/alterar una base de datos que en este caso sería en estructura SQL, a través de python y con sintaxis de python. Te peprmite convertir datos de tus objetos en un formato correcto para poder guardarlos en una base de datos (mapeo), donde los datos que se encuentran en nuestra aplicacións, sean vinculados a la base de datos. Esto con el fin de proteger nuestra base datos y poder trabajar todo el backend desde un archivo.

## Marshmallow

Sirve para serializar y deserializar objetos