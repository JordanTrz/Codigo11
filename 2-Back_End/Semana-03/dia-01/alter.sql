alter table cliente
add column pais varchar(200) after nombre;

alter table cliente
modify column id int auto_increment;