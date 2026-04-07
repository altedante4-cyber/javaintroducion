use gha_analytics;

start transaction;

-- eliminar duplicados exactos (mismo nif y nombre) manteniendo id mas bajo 
delete p1 from pacientes p1
join pacientes p2
where p1.nif = p2.nif
and p1.nombre_completo = p2.nombre_completo
and p1.id > p2.id;


-- 1.2limpiar nifs espacios al inicio /final
update pacientes set nif = TRIM(nif);
-- 1.3 eliminar guiones del nif 
update pacientes set nif = replace(nif,'-','');
-- 1.4 eliminar nifs problematicos
delete from pacientes
where nif is null
or nif = ''
or nif = 'NULL_NIF'
or trim(nif)='';

-- 1.5 eliminar nifs que no cumplan el patorn valido (8 numeros + 1 letra)
delete from pacientes
where nif not regexp '^[0-9]{8}[A-Z]$';
commit ;


select 'FASE 1 OK : normalizacion de identidad' as resultado ;

-- fase 2 consistencia de colegiados

start transaction;


 -- 2.1 limpiar espacios

update medicos set num_colegiados = trim(num_colegiado);

update medicos
set num_colegiado = concat('COL-',substring_index(num_colegiado,'/',1),'-',
lpad(substring_index(num_colegiado,'/',-1),4,'0'))
where num_colegiado like '%/%',

-- 2.3 formato "28-777"
update medicos
set num_olegiado = concat('COL-',replace(num_colegiado , '-','-'))
where  num_colegiado like '%-%' and num_colegiado not like 'COL-%';

-- 2.4 formato "COL2899990"
update medicos
set num_colegiado = concat('COL-',substring(num_colegiado,4,2),'-',
lpad(substring(num_colegiado,6),4,'0'))
where num_colegiado like 'COL[0-9]%' and num_colegiado not like 'COL-%-%';


-- 2.5 formmatos invalidos como "INV-999" -> "COL-00-0999"
update medicos
set num_colegiado = concat ('COL-00-' , LPAD(substring(num_colegiado,-3),4,'0'))
where num_colegiado not like 'COL-%-%'

commit ;

select 'FASE 2 OK: Consistencia de colegiados' as resultado ;

-- FASE3 integridad referencial
-- 3.1 corregir especialidad inexistente(id=99) 
start transaction;
update medicos set especialidad_id = 1
where especialidad_id not in(select id from especialidades);
commit ;


-- 3.2 agregar fk en medicos -> especialidades
start transaction;
alter table medicos add constraint fk_medicos_especialidad  foreign key (especialidad_id) references especialidades(id);
commit ;

-- 3.3 eliminar visitas con referencias huesfanas

start transaction;
-- eliminar visitas donde paciente_id no existe (excepto 99 que ya elimnaremos)
delete from visitas
where paciente_id not in (select  id from pacientes) 
and paciente_id != 999
delete from visitas where paciente_id = 999 ;

-- eliminar visitas donde medico_id no existe ( excepto 888 que ya eliminaremos)
delete from visitas
where medico_id not in(select id from medicos)
and medico_id != 888;
delete from visitas where medico_id = 888;
commit ;

-- 3.4 agregr fk en visitas
start transaction;
alter table visitas
add constraint fk_viistas_paciente
foreign key (paciente_id) references pacientes(id);
commit ;

start transaction;
alter table visitas
add constraint fk_visitas_medico
foreign key (medico_id) references medicos(id) ;
commit ;

select 'Fase 3 ok : Integridad referencial' as resultado ;

-- ===
-- fase 4 diviison de tablas

start transaction;
-- 4.1 crear tablas de seguros separada
create table seguros_pacientes(
	id int auto_increment primary key,
paciente_id int not null ,
num_poliza varchar(50),
estado_poliza varchar(20) default 'ACTIVA',
constraint fk_seguros_pacientes foreign key (paciente_id) references pacientes(id)
);
-- 4.2 migrar datos ede num_pliza
insert into seguros_pacientes (paciente_id,num_poliza)
select id,num_poliza
from pacientes
where num_poliza is not null ;

-- 4.3 eliminar columnas de pacientes
alter table pacientes  drop column num_poliza;
commit ;

select 'FASE 4 OK'  as resultado ;

-- fase 5  columnas calculadas 

start transaction;

-- 5.1 limpiar importes espacios
update visitas set importe_sucio = trim(importe_sucio);

-- 5.2 eliminar simbolos de moneda 
update visitas set importe_sucio = replace(importe_sucio,'€','');
update visitas set importe_sucio = replace(importe_sucio,'$','');
update visitas set importe_sucio = replace(importe_sucio,'EUR','');

-- 5.3 convertir coma decimal a punto 
update visitas set importe_sucio = replace(importe_sucio,',','.');

-- 5.4 manejar casos especiales (vacio o 'Gratis')
update visitas set importe_sucio = null
where importe_sucio = '' or upper(importe_sucio) = 'GRATIS';
commit ;

--- 5.5 convertir a decimal
start transaction;
alter table visitas modify importe_sucio decimal (10,2);
commit ;

-- 5.6 añadir columna calculada (copago20%)
start transaction;
alter table visitas add column copago_estimado decimal(10,2);
update visitas set copago_estimado = roung(importe_sucio * 0,20 , 2);
alter table visitas modify copago_estimado decimal (10,2) not null ;
commit ;

select 'fase 5 ok ' as resultado ;

-- fase 6 ingesta de datos 

start transaction;
-- 6.1 parsear raw_data a insertar pacientes nuevos
-- formato
insert into pacientes (nif,nombre_completo,tel_contacto,f_nacimiento)
select 
trim(substring_index(raw_data,'|',1)) as nif,
trim(substring_index(substring(raw_data,locate('|',raw_data) + 1),'|',1)) as nombre,
raw_phone as tel_contacto,
null as  f_nacimiento
from ram_import_visitas
where trim(substring_index(raw_data,'|',1)) not in (select nif from pacientes where nif is not null );

-- 6.2 crear tabla temporal para visitas del staging
create temporary table temp_visitas_stagin(
	paciente_id int ,
	fecha_visita varchar(100),
	importe varchar(50)
);

-- 6.3 parsear e insertar desde stagin
insert into temp_visitas_stagin(paciente_id, fecha_visitas,importe)
select
	p.id as paciente_id,
	trim(substring_index(substring(raw_data, locate('|',raw_data)+1),'|',-2)) as fecha,
trim(substring_index(raw_data,'|',-1)) as importe
from raw_import_visitas r
inner join pacientes p on trim(substring_index(raw_data,'|',1)) = p.nif;
commit ;


-- 6.4 insertar visitas normalizadas
start transaction;
insert into visitas (paciente_id, fecha_visita,importe_sucio,
descuento_aplicado)
select
	paciente_id,
	fecha_visita,
	replace(replace(replace(importe,'€',''),'$',''),',','.'),
	null
from temp_visitas_stagin
where importe not like '%GRATIS%';
drop temporary table temp_visitas_staging;
commit ;
-- 6.5 eliminar tabla de stagin
start  transaction;
drop table raw_import_visitas;
commit ;

select 'FASE 6 OK' as resultado ;

-- escenario dos sanmiento profunto
-- gestionar email nulos o vacios
start transaction;
update pacientes 
set email = 'desconocido@sinemail.com'
where email is null or email ='';
commit ;

-- 7.2 limpiar fecha de nacimiento
start transaction;
	update pacientes set f_nacimiento = trim(f_nacimiento);
	update pacientes set f_nacimiento = replace(f_nacimiento,'.','/');
	update pacientes set f_nacimiento = null
	where f_nacimiento = '' or upper(f_nacimiento) = 'NULL';
commit ;

-- 7.3 limpiar fechas de visita 
start transaction;
update visitas set fecha_visita = trim(fecha_visita);
update visitas set fecha_visita = replace(fecha_visita,'.','-');
commit ;


-- 7.4 normalizar descuento_aplicado

start transaction;
alter table visitas modify descuento_aplicado decimal(10,2);
update visitas set descuentio_aplicado = 0 where descuento_aplicado is null;
commit ;

select 'escenario2 ok sanamiento profundo' as resultado ;

-- fase 8 indice de optimisacion


start transaction;
create index idx_pacientes_nif on pacientes(nif);
create index idx_pacientes_email on pacientes(email);
create index idx_medicos_colegiado on medicos(num_colegiado);
create index idx_medicos_especialidad on medicos(especialidad_id);
create index idx_visitas_fecha on visitas (fecha_visita);
create index idx_visitas_paciente on visitas(paciente_id);
create index idx_visitas_medico on visitas(medico_id);
create index idx_seguros_paciente on seguros_pacientes(paciente_id);
commit ;


select 'fase8 ok indeces creados ' as resultado ;


-- verificacion final 






