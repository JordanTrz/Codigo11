Introducción a MySQL

se ingresa desde el terminal utilizando:

sudo mysql

se utiliza la función "select"

select current_date;
select version();
select 4+1;
select sin(pi()/4),(4+1)*5;

select databases;

para poder visualizar las bases de datos creadas se usa:

show databases;
show tables;

use mysql;

Codigo2022!

# Muestra todos los usuarios que se tienen creado en mysql
select host,user from user;

# Se crea usuario
create user 'codigo'@'localhost' identified by 'codigo2022';

# Se le asigna privilegios a todas las tablas
grant all privileges on *.* to 'codigo'@'localhost';

como loguearse

mysql -u "nombre de usuario" -p

create database codigog11;

show databases;

use codigog11;
show tables;
create table cliente(
id INT(11) PRIMARY KEY,
nombre VARCHAR(100),
email VARCHAR(100)
);

show tables;
describe cliente;

# para importar tabla en mysql
source "ruta donde se encuentra el document"

Si se quiere importar directamente sin colocar toda la ruta, se tiene que ir con el CLI hasta donde se encuentre el .sql a importar

# Sentencias DDL
Definen las estructuras que almacenarán los datos

create
alter
drop --> table "nombre tabla"

# DML Data manipulating language
permite instroducir datos para posteriormente realizar tareas de consultas o modificación

select
insert
update
delete

alter table cliente add column "titulo" varchar(200) after "lugar donde quiere colocar la nueva columna"

insert into "xx" values "()" --> esto depende de la cantidad de columnas
ejemplo:
insert into cliente(nombre,pais,email) values('Jordan','Peru','jt@gmail.com')

select * from cliente; #Esto selecciona todos los datos que se encuentran en cliente

update cliente set nombre='Jordan', email='jordan.terrazos@gmail.com'
where id = 2;

Si no se coloca el "where" se actualiza toda la tabla

Ya no se utiliza el delete debido a que se puede bajar información sensible que ya no se puede recuperar

alter table cliente
add column state har(1) default '1' not null;

Cómo realizar búsquedas/filtrados:

select nombre,email from cliente where nombre like 'A%' and pais='Peru'

select count(*) from cliente;

select count(*) from cliente where pais='Peru';

select pais,count(*) from cliente group by pais order by pais asc;


select pais, count(*) from cliente group by pais order by count(*) desc;

distinct --> se utiliza para mostrar resultados sin duplicados

# semana 03 - día 2

select * from movie;
select count(*) from movie;
describe movie;
select title,overview,popularity,release_date,revenue from movie;
select * from movie where title like '%harry%pot%';
select * from movie where title = 'star wars';
SELECT * from movie where title like '%resident%evil%';
select * from movie where revenue > 1000000000;
select * from movie where revenue < 100000000;
select * from country where country_name = 'Peru';
select * from movie where revenue between 1000000 and 3000000;
select * from movie order by revenue asc limit 1;
select avg(revenue) from movie;
select * from movie where revenue > (select avg(revenue) from movie);
select * from country where country_name = 'Peru';
select distinct runtime from movie where runtime > 200 order by runtime;
select year(release_date) from movie where title like '%star wars: episode%';
select * from movie where year(release_date) in (select year(release_date) from movie where title like '%star wars: episode%');

Se puede realizar subconsultas

# claves foraneas

Se utilizan para entrelazar tablas

ejemplo:
`create table venta_detalle(
  id int(11) not null AUTO_INCREMENT,
  computadora_id int(11) not null,
  cantidad int(5) not null,
  precio DOUBLE,
  venta_id int(11) not null,
  PRIMARY KEY(id),
  FOREIGN KEY(computadora_id) REFERENCES computadora(id),
  FOREIGN KEY(venta_id) REFERENCES venta(id)
)`

# Esto es para poder permitir el ingreso de la extensión. en caso no funcione quitar el "localhost"

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

# semana 03 - día 2

## Normalización de tablas

### 1ra forma de normal
Se tiene que eliminar de las tablas las columnas que se repitan, es decir, los títulos que se repitan, por ejemplo:
id / nombre / profesor / curso1 / curso2 / curso3

Este caso tendría que juntarse todos los curso1-2-3 en una sola tabla.

### 2da forma normalización
Se debe tener en 1fn.
no deben existir valores repetidos. por lo que se deben crear nuevas tablas. Si una columna no depende funcionalmente de otra columna, debe crearse una nueva tabla

### 3ra forma normalización
Se deben eliminar datos que no dependan de la clave. Si existe un atribudo que no depende de la clave primaria. se debe mover a otra tabla.

# Agregar y eliminar datos

## Creaciones
create database "nombre_database"
create table "nombre_table"

create table publicaciones(
  id int(11) not null auto_increment,
  autor_id int(11) not null,
  titulo varchar(150) not null,
  texto text not null,
  primary key (id),
  foreign key (autor_id) references usuarios(id)
);

insert into "nombre_table"(nombre,apellido,telefono) values('jordan','terrazos','999600566')

## Modificaciones
update "nombre_tabla"
set nombre='Gianmarco',apellido='Acuña'
where id='1';

## eliminaciones
delete from "nombre_table" where id='1';


# Consultas en MySQL

## Consultas básicas
se pueden usar inner join, left join, right join. Ejemplos:

## Buscar todos los ususarios:
select * from "name_tabla";

## Buscar un dato con id:
select * from "name_tabla" where id='1'

## Buscar varios datos con id:
select nombre,apellido from "name_tabla" where id='1';
select * from "name_tabla" where apellido like '%o%';
## Creaciones de View
Son consultas ya realizadas pero grabadas dentro de una variable

## Creaciones de procedure
son como funciones donde se le pasa un argumento
El @ se utiliza para poder guardar como variable;

## Delimiter

Se utiliza para poder cambiar con qué letra/signo se va a realizar la delimitación entre ĺíneas de consultas.

## Procedimientos almacenados

son procedure que se pueden tener internamente código como bucles y salidas, programación en mysql

## Funciones

Son código que retorna algo cuando se les pasa un argumento

## Trigger

El trigger se utiliza cuando alguien ingresa un valor en una tabla, también se "dispare" una acción en la misma u otra tabla