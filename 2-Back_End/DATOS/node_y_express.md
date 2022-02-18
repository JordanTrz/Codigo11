- Express con Node

se crea una carpeta del proyecto

se pone:
`npm init`

Tammbién se puede correr el comando:
`npm init -y`
esto da yes a todo

Se completa todo los campos:

1. package name: se deja el mismo noambre de la carpeta
2. description: se pone una descripción del proyecto
3. entry point: enter
4. test comand: enter
5. git repository: enter, en realidad se pone el link
6. keywords: enter
7. author: "tu propio nombre"
8. license: Se deja ISC por defecto
9. Te muestra el package-json final

Se da enter y ya se tiene el package-json

Luego se tiene que instalar el framework Express:

`npm install express`

Este comando te instala las dependencias y te coloca en el package json la versión que se va a utilizar

Creación de .gitignore, dentro se tiene que poner el:
`node_modules/`

-- Instalación de nodemon:

`npm install --save-dev nodemon`

-- configuración de scripts

1. Se ingresa al package json
2. se agrega un "start" en scripts:

`"scripts": {"start":"node index.js",}`

con esto se puede correr el programa utilizando el código:

`npm start / npm run start`

Se debe poner modo global para utilizar nodemon. en el package json se agrega en scripts:

`"dev":"nodemon index.js"`

para correr se coloca en el terminal:

`npm run dev`

-- URL

para pasar parámetro en los get se pone `:` y el nombre del parámetro:

`app.get('/saludar/:nombre',(req,res)=>{`

  `res.send('Hola ' + req.params.nombre)`

`})`

-- Trabajar con base de datos

Se instala:

`npm install mysql`

se crea otro archivo con nombre `database.js`

Se importa la libreria en la cabecera:
const mysql = require('mysql');