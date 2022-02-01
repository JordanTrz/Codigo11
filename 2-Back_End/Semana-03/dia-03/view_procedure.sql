-- Vistas

create View vw_profesor_cursos as
select tbl_profesor.profesor_nombre,tbl_curso.curso_nombre
from tbl_profesor

left join tbl_matricula_curso
on tbl_profesor.profesor_id = tbl_matricula_curso.profesor_id

inner join tbl_curso
on tbl_matricula_curso.curso_id = tbl_curso.curso_id;

select * from vw_profesor_cursos
where profesor_nombre = 'Cesar Mayta';

-- Procedimientos almacenados, la sp = sub proceso
delimiter;
CREATE PROCEDURE sp_cursosxalumno(in id int)
begin
    select tbl_curso.curso_nombre
    from tbl_curso
    inner join tbl_matricula_curso
    on tbl_curso.curso_id = tbl_matricula_curso.curso_id
    inner join tbl_matricula
    on tbl_matricula_curso.matricula_id = tbl_matricula.matricula_id
    where tbl_matricula.alumno_id = id;
end
delimiter;

call sp_cursosxalumno(1);