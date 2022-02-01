
delimiter $$

create function fn_contar_cursos(id int(11))
    RETURNS int unsigned
begin
    declare total int unsigned;

    SELECT count(*) into total
    from tbl_matricula_curso
    where profesor_id = id;

    return total;
end
$$

delimiter ;
select fn_contar_cursos(3);
select profesor_nombre,fn_contar_cursos(profesor_id)
from tbl_profesor;

delimiter $$
create Function fn_contar_alumno_cursos(intIdAlumno int(11))
    returns int unsigned
begin
    declare totalCursos int unsigned;

    set totalCursos = (
        select count(*)
        from
        tbl_matricula_curso mc inner join tbl_matricula m on mc.matricula_id = m.matricula_id
        where m.alumno_id = intIdAlumno
    );

    RETURN totalCursos;
end
$$

delimiter ;

select alumno_id,alumno_nombre,fn_contar_alumno_cursos(alumno_id)
from tbl_alumno;

delimiter $$