- Ingreso a aws

Se debe registrar con una tarjeta y cuenta personal

se debe ingresar a aplicaciónes e ingresar a la opción EC2

Una vez dentro se da click a lanzar instancia

una vez lanzado la instacia se tiene que seleccionar todo lo que es de la capa gratuita

1. AMI --> Se selecciona la opción de ubuntu server
2. Elegir tipo de instancia --> La capa gratuita
3. Configurar la instancia --> No se selecciona nada
4. Adición de almacenamiento --> No se selecciona nada
5. Agregar Etiquetas --> No se selecciona nada
6. Configure security group --> Se añade una regla:
   1. SSH
   2. HTTP
   3. Regla TCP personalizada -- Puerto
Se da click en lanzar
luego aparecerá una ventana final que indica que se debe poner par de claves
Se pone crear, se coloca un nombre y se descarga

Se conecta al servidor con los siguientes pasos:

Abra un cliente SSH.
Localice el archivo de clave privada. La clave utilizada para lanzar esta instancia es codigo.pem
Ejecute este comando, si es necesario, para garantizar que la clave no se pueda ver públicamente.
 chmod 400 codigo.pem
Conéctese a la instancia mediante su DNS público:
 ec2-184-72-103-101.compute-1.amazonaws.com
Ejemplo:
 `ssh -i "codigo.pem" ubuntu@ec2-184-72-103-101.compute-1.amazonaws.com`

Luego se sigue los siguientes pasos del link:

https://www.digitalocean.com/community/tutorials/como-configurar-django-con-postgres-nginx-y-gunicorn-en-ubuntu-18-04-es

En resumen sería:
- sudo apt update
- sudo apt upgrade
- sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

Luego se ingresa a postgres:
- sudo -u postgres psql

Dentro de postgres:
CREATE DATABASE shop;
CREATE DATABASE pos_backend;
CREATE DATABASE pos;

Se crea usuario
- CREATE USER codigo WITH PASSWORD 'codigo2022';

- ALTER ROLE codigo SET client_encoding TO 'utf8';
- ALTER ROLE codigo SET default_transaction_isolation TO 'read committed';
- ALTER ROLE codigo SET timezone TO 'UTC';

- GRANT ALL PRIVILEGES ON DATABASE shop TO codigo;

- \q

Luego se tiene que instalar el entorno virtual y el pip3

`sudo apt install python3.8-venv`
`sudo apt install python3-pip`

python3 -m venv venv
sourve venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

-- Despliegue con gunicorn y nginx

Se debe de copiar 3 archivos que se tiene en awsconfig. Para esto se copia del repo:

`https://github.com/cesarmayta/CODIGO-2021-G11/tree/semana07/semana07/dia2/awsconf`

o se puede copiar en local, hacer un push y desde el servidor hacer un pull o clone del proyecto.

Luego se tiene que copiar los archivos dentro del servidor, en la carpeta /etc/

`sudo cp gunicorn.socket /etc/systemd/system/gunicorn.socket`

`sudo cp gunicorn.service /etc/systemd/system/gunicorn.service`

`sudo cp shop /etc/nginx/sites-available/shop`
`sudo cp pos_backend /etc/nginx/sites-available/pos_backend`


Luego en la carpeta shop se debe desplegar el gunicorn, esto se puede hacer con el comando:

`gunicorn --bind 0.0.0.0:8000 pos_backend.wsgi`

Luego se tiene que poner otro comando más

`python3 manage.py collectstatic`

Activamos los sockets:

`sudo systemctl start gunicorn.socket`
`sudo systemctl enable gunicorn.socket`

Para verificar que está funcionando correctamente se corre el comando:

`sudo systemctl status gunicorn.socket`

`file /run/gunicorn.sock`

`sudo systemctl status gunicorn`

`curl --unix-socket /run/gunicorn.sock localhost`

`sudo systemctl status gunicorn`

<!-- ERror -->
Paste that into the path section of the ‘ExecStart’ value inside the ’/etc/systemd/system/gunicorn.service’ file, and run the 'sudo systemctl daemon-reload’ and 'sudo systemctl restart gunicorn’ commands to restart your daemon and try curling again with curl --unix-socket /run/gunicorn.sock localhost

<!-- fin error -->

Ahora se debe configurar nginx

`sudo ln -s /etc/nginx/sites-available/pos_backend /etc/nginx/sites-enabled`
sudo ln -s /etc/nginx/sites-available/pos_backend /etc/nginx/sites-enabled

`sudo nginx -t`

`sudo systemctl restart nginx`