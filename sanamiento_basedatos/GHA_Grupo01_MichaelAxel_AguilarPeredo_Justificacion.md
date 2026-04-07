# JUSTIFICACIÓN DEL SANEAMIENTO DE BASE DE DATOS

**Práctica Avanzada: GHA_ANALYTICS**

**Grupo:** 1  
**Estudiante:** Michael Axel Aguilar Peredo  
**Fecha:** 07/04/2026

---

## Lo que encontré en la base de datos

Cuando miré los datos por primera vez me encontré un desastre total. La tabla de pacientes tenía NIFs con espacios al principio y al final, algunos con guiones en medio, había duplicados exactos, y un par de registros con "NULL_NIF" como si alguien hubiera copiado texto plano en vez de dejar el campo vacío.

Los médicos tampoco se escapaban. Cada uno tenía el número de colegiado escrito de forma distinta: uno usaba barra, otro guión, otro todo pegado sin separación. Y para rematar, había un médico con especialidad_id = 99 que ni siquiera existía en la tabla de especialidades.

Las visitas ni te cuento. Importes con símbolos de moneda (€, $, EUR), algunos con coma en vez de punto para decimales, espacios por todos lados, y la palabra "Gratis" en vez de un número. Había visitas que referenciaban pacientes y médicos que no existían.

---

## Lo que hice y por qué

### PACIENTES - Lo primero que limpié

Empecé por los NIFs porque es la identidad de cada paciente. Primero quité los espacios con TRIM y los guiones con REPLACE. Después borré los registros problemáticos: los que tenían NULL, vacío, o el texto "NULL_NIF". Luego me encargué de los duplicados con un DELETE que compara el NIF y se queda con el id más bajo.

Los NIFs que quedaban con formato raro (menos de 8 números o sin letra mayúscula al final) los eliminé también porque no eran válidos.

Los emails que estaban vacíos o nulos les puse un valor por defecto "desconocido@sinemail.com" para que no haya huecos.

Las fechas de nacimiento tenían puntos en vez de barras, así que las convertí con REPLACE.

### MÉDICOS - Los carnets de colegiado

Aquí había varios formatos distintos y los fui convirtiendo uno por uno. Los que tenían barra (como 28/5566) los convertí a COL-28-5566. Los que tenían guión (28-7788) también los convertí. Los que ya empezaban con COL pero estaban pegados (COL289900) los separé. Los que tenían formato raro como INV-999 los convertí a COL-00-0999.

La especialidad 99 del médico provisional la cambié a 1 (Medicina General) porque era la única forma de que la foreign key funcionara.

### VISITAS - Los importes eran un caos

Primero去掉 todos los símbolos de moneda: euros, dólares, y el texto EUR. Luego convertí las comas en puntos para que MySQL entendiera que son decimales. Los espacios los quité con TRIM. La palabra "Gratis" la convertí a NULL porque no tiene sentido guardarla como texto.

Después cambié el tipo de la columna de VARCHAR a DECIMAL para que funcione como número de verdad.

Añadí una columna nueva llamada copago_estimado que es el 20% del importe. Lo calculé con ROUND para que tenga 2 decimales limpios.

Las visitas que apuntaban a pacientes o médicos que no existían las borré. Si no, la foreign key no se podría crear.

### Integridad referencial

Una vez limpios los datos, creé las foreign keys. Son las que garantizan que no se pueda insertar una visita con un paciente que no existe, por ejemplo. Siempre hay que crear las FK después de limpiar, nunca antes.

### División de tablas

La columna num_poliza de pacientes la pasé a una tabla aparte llamada seguros_pacientes. Es mejor tenerla separada porque un paciente puede tener varias pólizas y además así la tabla de pacientes queda más limpia.

### raw_import_visitas

Esta tabla contenía datos en formato texto mezclado con tuberías (|). Parseé cada campo usando SUBSTRING_INDEX para separar por el delimitador. Inserté los pacientes nuevos y las visitas que faltaban.

### Índices

Al final creé índices en las columnas que más se usan para buscar: el NIF, el email, el número de colegiado, las fechas. Esto hace que las consultas sean más rápidas.

---

## Por qué hice las cosas en este orden

El orden importa mucho. No puedes crear una foreign key si todavía hay registros huérfanos. No puedes buscar duplicados si los NIFs todavía tienen espacios o guiones. No puedes convertir a número si todavía hay texto como "Gratis" o símbolos de moneda.

Siempre se empieza por lo más básico (limpiar textos) y se acaba con lo que depende de todo lo demás (índices, foreign keys).

---

## Lo que aprendí

Los datos sucios vienen de muchos sitios: importaciones de CSV mal formateadas, copias de Excel, formularios mal validado... Nunca te fiees de los datos que te dan. Siempre hay que mirarlos bien antes de trabajar con ellos.

Las transacciones son fundamentales. Si algo falla a mitad de proceso, puedes volver atrás y no dejas la base de datos a medias.

Y lo más importante:documenta lo que haces. Si mañana alguien tiene que entender qué pasó, la justificación debe explicar el por qué de cada decisión, no solo el qué.
