# para crear database

## use "nombre database"
ejemplo:

use codigog11;
show dbs;

show collections;

# trabajar con colecciones

## Leer datos

show dbs;

db.alumnos.find();

db.alumnos.find().pretty();

db.alumnos.find({nota:{$gte:11}});

## Crear datos

db.alumnos.insertOne({nombre:"Jordan Terrazos",email:"jordan@gmail.com"});

db.alumnos.insertOne();

db.alumnos.insertMany();

## Actualizar datos

db.alumnos.updateOne({email:"cesarmayta@gmail.com"},{$set :{nombre:"Cesar Avalos",nota:12}});

db.alumnos.updateOne({_id: ObjectId("61e22166374772d16fd34de7")},{$set:{nota:18}});

## Elimintar datos

db.alumnos.deleteOne({_id:copiar id})

## importa
from bson import json_utils --> Esto es para traer objetos directo de mongodb
