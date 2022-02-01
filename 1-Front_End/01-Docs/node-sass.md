#Installar node sass

Es para poder compilar el código de Sass

## node js

Primero se tiene que instalar el node js

En este caso, al ser ubuntu, se realiza con el nvm

se insala/actualiza:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

Código para que el sistema reconozca los cambios:

source ~/.bashrc

Una vez instalado/actualizado el nvm, se pasa a colocar el código

nvm ls-remote

de esa lista se tiene que elegir qué versión del node js se quiere instalar, y se utiliza el comando:

nvm install [version.number

## INSTALAR COMPILADOR

Luego de tener el node

npm i node-sass

ó se puede usar el:

npm i -g sass

## NODE-SASS

para utilizar se usa:

npx node-sass ./"lugar donde se encuentra el sass" ./"lugar donde se quiere guardar .css"