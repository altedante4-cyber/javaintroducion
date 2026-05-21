# Preguntas tipo para la defensa del proyecto (Servicio B)

Respuestas directas para cada sección de la memoria.

---

## 1. JUSTIFICACIÓN ARQUITECTÓNICA

### ¿Por qué MongoDB y no otra?

Porque el Servicio B necesita **escrituras masivas y rápidas** (pings cada 5s de miles de vehículos) y **consultas por rango temporal** (historial de un vehículo). Cassandra es la opción natural para telemetría, pero no la dimos. Entre las que sí:

- **Redis**: está en RAM, no da para históricos masivos. Si el contenedor se cae, pierdes millones de registros.
- **Neo4j**: es de grafos, no tiene sentido para series temporales.
- **MongoDB**: documentos JSON flexibles, índices compuestos, escrituras sin bloqueos.

### ¿Qué ventaja tiene el esquema flexible?

Cada ping puede llevar campos distintos según el vehículo. Un coche puede enviar `combustible` y un patinete no. En MongoDB ambos documentos van en la misma colección. En MySQL necesitarías columnas NULLables o tablas separadas.

### ¿Qué es el índice compuesto y por qué ese?

`{ vehicle_id: 1, timestamp: -1 }` — la consulta que vamos a hacer es "dame el historial de VH-001 ordenado por tiempo". El índice:
1. Filtra por `vehicle_id` (solo los documentos de ese vehículo).
2. Ya los devuelve ordenados por `timestamp` sin tener que ordenar en RAM.

Es el equivalente a **Partition Key + Clustering Column** de Cassandra, adaptado a MongoDB.

### ¿Por qué `vehicle_id` y no otro campo?

Porque es el campo por el que **siempre vamos a filtrar**. Y tiene **alta cardinalidad** (muchos valores distintos), lo que distribuye bien los datos.

---

## 2. PROMPTS DE GENERACIÓN DE DATOS

### ¿Qué prompt usaste?

"Genera un script de MongoDB para insertar 5 documentos de telemetría en una colección llamada 'telemetria'. Los documentos deben corresponder al vehículo con ID 'VH-001' en distintas horas del mismo día. Cada documento debe contener: vehicle_id, timestamp (en formato ISODate), location (con lat y lng), speed (número decimal) y battery (número entero 0-100). Los timestamps deben espaciarse al menos 1 hora entre sí. Los valores de batería deben decrecer con el tiempo para simular consumo real."

### ¿Por qué ese prompt?

Porque le digo exactamente:
- **Qué** quiero (5 documentos)
- **Cómo** quiero los datos (campos, tipos, formato)
- **Reglas de negocio** (batería decreciente, timestamps espaciados)

Así la IA no alucina estructuras ni formatos.

---

## 3. ANÁLISIS DE AUDITORÍA

### ¿Qué corrigió la IA y por qué?

**Corrección 1: Normalización encubierta**

La IA creó dos colecciones: `vehiculos` y `telemetria`, con un `$lookup` (join) para unirlas. Eso es **pensar en SQL**. En MongoDB, si siempre lees los datos juntos, debes **incrustarlos** en el mismo documento (Agregado). Así evitas el join y ganas velocidad.

**Corrección 2: Índice simple → compuesto**

La IA puso índice solo en `vehicle_id`. Eso filtra bien, pero al ordenar por `timestamp` MongoDB tiene que ordenar en RAM. Con el índice compuesto `{ vehicle_id: 1, timestamp: -1 }`, el orden ya viene del índice. Con millones de registros, ordenar en RAM daría error (límite de 32MB).

### ¿Cómo detectaste esos errores?

Por los **antipatrones NoSQL** del anexo: Normalización Encubierta (MongoDB) y Diseño de Claves Erróneo (aunque aquí es índice, el mismo principio).

---

## 4. SCRIPTS DE CARGA Y CONSULTAS

### ¿Por qué `insertMany` y no 5 `insertOne`?

`insertMany` hace una sola operación de red. 5 `insertOne` serían 5 viajes de ida y vuelta al servidor. Con millones de pings, la diferencia de rendimiento es enorme.

### ¿Por qué `timestamp: 1` en el `find` si el índice es `-1`?

El índice es descendente (`-1`) porque las lecturas más recientes son las que más se consultan. Pero en la consulta de historial pido ascendente (`1`). MongoDB **puede recorrer el índice en ambas direcciones** con la misma eficiencia, así que no hay problema.

### ¿Qué pasa si no creo el índice?

La consulta funciona igual, pero hace un **collection scan** (lee toda la colección) y ordena en RAM. Con 5 documentos no notas nada. Con 5 millones, la consulta tarda minutos o da error de memoria.

---

## 5. EJECUCIÓN Y VISUALIZACIÓN

### ¿Cómo verificaste que funciona?

Tres capturas:
1. `createIndex` devuelve `numIndexesAfter: 2` (el índice `_id` por defecto + el nuestro).
2. `insertMany` devuelve `acknowledged: true` con 5 ObjectId.
3. `find` devuelve los 5 documentos ordenados por hora.

### ¿Y si no sale ordenado?

Revisar que el índice existe con `db.telemetria.getIndexes()` y que la consulta lo usa con `.explain("executionStats")` — si pone `COLLSCAN` es que no hay índice; si pone `IXSCAN` lo está usando.

---

## PREGUNTAS TRAMPOSAS

### ¿MongoDB no es solo para documentos, por qué lo usas para telemetría?

Cada ping **es un documento JSON**. Un ping es: `{ vehicle_id, timestamp, location, speed, battery }`. Eso es un documento. No hay mejor modelo para guardar eventos estructurados con campos variables.

### ¿Y si mañana crecen los datos y un vehículo tiene mil millones de lecturas?

MongoDB escala horizontalmente con **sharding**. El shard key sería `vehicle_id`, exactamente el primer campo de nuestro índice. No hay que cambiar nada en el código.

### ¿Por qué no usaste el `_id` como índice?

El `_id` es único por documento. Si filtro por `_id`, obtengo una sola lectura. La consulta que necesito es "todas las lecturas de un vehículo", no "una lectura concreta".

### ¿Y si quiero buscar por ubicación en lugar de por vehículo?

Ahí MongoDB tiene **índices 2dsphere** para geolocalización. Sería otro índice distinto para otra consulta distinta — eso es **Query-First Design**.
