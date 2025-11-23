use ejemplos_tipos_join;


show tables;
-- Ejercicio 1
-- Enunciado: Listado de alumnos con sus id_curso (sólo emparejados)

   select  alumnos.id_alumno,alumnos.nombre, matriculas.id_curso  from alumnos
     join matriculas on alumnos.id_alumno = matriculas.id_alumno;
    
    

-- Ejercicio 2
-- Enunciado: Alumnos sin ninguna matrícula (anti-join).

show tables ;

select alumnos.id_alumno , alumnos.nombre from alumnos 
left join matriculas on alumnos.id_alumno = matriculas.id_alumno
where matriculas.id_matricula is null;

-- seria trae todos los alumnos de la tabla izuierda y las matricuolas que coincidan 
-- where matriculas.id_matricula is null filtra por solo los registro donde no hubo coincidencia en la derecha 




-- Ejercicio 3
-- Enunciado: Matrículas sin alumno (huérfanas).


select matriculas.id_matricula , matriculas.id_alumno , matriculas.id_curso from matriculas
left join alumnos on matriculas.id_alumno = alumnos.id_alumno 
where alumnos.id_alumno is null ;

-- con el left join alumnos traemos los alumonn sque coincidan
-- where alumnos.id_alumno is null =>> filtramos solo las matriculas que no encontraron alumnos coincidente 

-- Ejercicio 4
-- Enunciado: Cursos del catálogo sin ninguna matrícula.
 
 describe cursos;
 
 select cursos.id_curso , cursos.nombre_curso from  cursos
 left join matriculas on cursos.id_curso = matriculas.id_curso
 where matriculas.id_curso is null ;
 
   

-- Ejercicio 5
-- Enunciado: Número de matrículas por alumno (incluye 0).

 select alumnos.id_alumno , alumnos.nombre , count(matriculas.id_alumno) from alumnos
left join matriculas on alumnos.id_alumno = matriculas.id_alumno 
 group by alumnos.id_alumno , alumnos.nombre ;





-- Ejercicio 6
-- Enunciado: Alumnos con más de un curso.

select alumnos.id_alumno , alumnos.nombre , count(matriculas.id_curso) as n  from alumnos
left join matriculas on alumnos.id_alumno = matriculas.id_alumno 
group by alumnos.id_alumno , alumnos.nombre 
having count(matriculas.id_curso) > 1 ;



-- Ejercicio 7
-- Enunciado: FULL OUTER JOIN emulado (alumnos y sus matrículas, incluyendo huérfanas).
-- Resultado esperado (7 filas) : las 6 left  + la fila 1004 

select alumnos.id_alumno , alumnos.nombre , matriculas.id_matricula,  matriculas.id_curso 
from alumnos
left join matriculas 
on  alumnos.id_alumno = matriculas.id_alumno 

union

select alumnos.id_alumno , alumnos.nombre, matriculas.id_matricula , matriculas.id_curso
from alumnos 
right join matriculas
on matriculas.id_alumno = alumnos.id_alumno
where alumnos.id_alumno  is null 
group by 1 is null , alumnos.id_alumno  , matriculas.id_matricula ;

   




-- Ejercicio 8
-- Enunciado: Para cada curso del catálogo, número de alumnos con matrícula válida (alumno y curso existen).

 describe cursos;
  select cursos.id_curso , cursos.nombre_curso , count(alumnos.id_alumno) as n_alumnos from cursos 
  left join matriculas on cursos.id_curso = matriculas.id_curso
  left join alumnos on matriculas.id_alumno = alumnos.id_alumno 
  group  by cursos.id_curso , cursos.nombre_curso 
  order by cursos.id_curso;
  
  -- con el primer left join traemos  las matriculas que coincidan con cada curso 
  -- con el segundo left join traemos  los alumnos que coincida on esas matriculas
  -- contamos solo alumnos que existen (no contamos los nulls) 