-- Inner Join
SELECT tbl_matricula.matricula_grupo,tbl_alumno.alumno_nombre
from tbl_matricula
inner join tbl_alumno
on tbl_matricula.matricula_id = tbl_alumno.alumno_id;

insert into tbl_alumno(alumno_nombre,alumno_email)
VALUES
('Jose Lopez','jose@gmail.com');

SELECT tbl_alumno.alumno_nombre,tbl_matricula.matricula_grupo
from tbl_alumno
left join tbl_matricula on tbl_alumno.alumno_id = tbl_matricula.alumno_id;

select tbl_alumno.alumno_nombre, tbl_matricula.matricula_grupo
from tbl_matricula
left join tbl_alumno on tbl_alumno.alumno_id = tbl_matricula.matricula_id;

insert into tbl_curso(curso_nombre) VALUES('GO');

select tbl_profesor.profesor_nombre,tbl_curso.curso_nombre
from tbl_profesor
inner join tbl_matricula_curso on tbl_profesor.profesor_id = tbl_matricula_curso.profesor_id
RIGHT join tbl_curso on tbl_matricula_curso.curso_id = tbl_curso.curso_id;

-- Consulta cuántos cursos dicta cada profesor
select tbl_profesor.profesor_nombre, count(tbl_matricula_curso.curso_id)
FROM tbl_profesor
left join tbl_matricula_curso
on tbl_profesor.profesor_id = tbl_matricula_curso.profesor_id
GROUP BY tbl_profesor.profesor_nombre;

insert into tbl_profesor(profesor_nombre)
VALUES ('Jorge Garnica');