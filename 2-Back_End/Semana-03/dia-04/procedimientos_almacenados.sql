select * from tbl_profesor;
DELIMITER $$

CREATE Procedure listar_profesores()
begin
    select * from tbl_profesor;
end
$$

DELIMITER ;

call listar_profesores();

-- Crear procedimiento para determinar la cantidad de cursos que está disctando un profesor
DELIMITER //

Drop PROCEDURE if EXISTS contar_cursos_profesor //

create procedure contar_cursos_profesor(in nombre varchar(200), out total int unsigned)
begin
    set total =( select count(*)
    FROM tbl_matricula_curso c
    inner join tbl_profesor p
    on c.profesor_id = p.profesor_id
    where p.profesor_nombre = nombre);
end //

DELIMITER ;

set @nombre = 'Cesar Mayta';

call contar_cursos_profesor(@nombre,@total);

call contar_cursos_profesor('Sebastian Yabiku',@total2);

select @total;
select @total2;

--create procedure bootcamp_de_alumno(in nombre varchar(255))


-- Ejemplo bucles en procedimientos almacenados
delimiter $$
create procedure ejemplo_bucle(in tope int,out suma int unsigned)
begin
    declare contador int;
    set contador = 1;
    set suma = 0;

    bucle: loop
        if contador > tope then
            leave bucle;
        end if;

        set suma = suma + contador;
        set contador = contador + 1;
    end loop;
end
$$

delimiter ;

call ejemplo_bucle(10,@resultado);

select @resultado;