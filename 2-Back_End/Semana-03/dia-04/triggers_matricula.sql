-- Triggers
insert into tbl_alumno(alumno_nombre,alumno_email)
values('Aldo Rodriguez','algo@gmail.com');

select alumno_nombre,concat(lower(replace(alumno_nombre,' ', ' ')),'@codigo.edu.pe')
from tbl_alumno;

delimiter $$

create Trigger tg_correo_alumno
before insert
on tbl_alumno for each row
begin
    set NEW.alumno_email = concat(lower(replace(NEW.alumno_nombre,' ','')),'@codigo.edu.pe');
    --  (
        -- select  concat(lower(replace(alumno_nombre,' ','')),'@codigo.edu.pe')
        -- from tbl_alumno where alumno_id = NEW.alumno_id
    -- );
end
$$

delimiter ;


insert into tbl_alumno(alumno_nombre,alumno_email)
values('Lucero Yberhuen','LuceroY@transter.com');

-- drop TRIGGER tg_correo_alumno;
