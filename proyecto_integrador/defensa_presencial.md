# Guión para la defensa presencial — Servicio B

Habla en este orden cuando el profe llegue a tu sitio.

---

## 1. QUÉ ES EL SERVICIO B (30 seg)

"Me ha tocado el **Servicio B: Telemetría y Sensores IoT**. Consiste en almacenar los pings que los vehículos envían cada 5 segundos con su ubicación, velocidad y batería. Se generan millones al día. La consulta principal es: *'dame el historial completo de un vehículo para detectar anomalías en la batería'.*"

---

## 2. QUÉ BASE DE DATOS ELEGÍ Y POR QUÉ (1 min)

"He elegido **MongoDB**, base de datos **Documental**, porque:

- Cada ping es un **documento JSON** — encaja perfecto.
- Necesito **esquema flexible**: un coche puede mandar `combustible`, un patinete no. En MongoDB van en la misma colección sin problemas.
- Necesito **índices compuestos** para que las consultas por vehículo + rango de tiempo sean rápidas.

Descarté Cassandra porque no la dimos. Redis está en RAM y no sirve para históricos masivos. Neo4j es de grafos, no tiene sentido para series temporales."

---

## 3. CÓMO DISEÑÉ LA ESTRUCTURA (30 seg)

"Una sola colección: **`telemetria`**. Cada documento tiene:

```
vehicle_id, timestamp, location {lat, lng}, speed, battery
```

Y creé un **índice compuesto**: `{ vehicle_id: 1, timestamp: -1 }`

- `vehicle_id` primero → agrupa todos los datos del mismo vehículo.
- `timestamp` después → las lecturas ya vienen ordenadas.

Es mi **Query-First Design**: diseñé el índice pensando en la consulta que voy a hacer."

---

## 4. LAS DOS CORRECCIONES QUE HICE A LA IA (1 min — IMPORTANTE)

"La IA me generó código, pero tuve que corregirle **dos antipatrones NoSQL**:

**Primera corrección — Normalización encubierta:**
La IA creó dos colecciones: `vehiculos` y `telemetria`, con un `$lookup` para unirlas. Eso es **pensar en SQL**. En MongoDB, cuando los datos siempre se leen juntos, se **incrustan** en el mismo documento. Corregí: puse `vehicle_type` directamente dentro del documento de telemetría.

**Segunda corrección — Índice incompleto:**
La IA puso índice solo en `vehicle_id`. Filtra bien, pero al ordenar por `timestamp` MongoDB tiene que ordenar en RAM — con millones de registros eso da error (límite 32MB). Corregí: añadí `timestamp` al índice para que el orden venga del índice."

---

## 5. LOS SCRIPTS QUE EJECUTÉ (30 seg)

"Primero, crear el índice:

```javascript
db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })
```

Luego, insertar 5 registros del vehículo VH-001 en distintas horas con `insertMany` —lo uso en vez de 5 `insertOne` para hacer una sola llamada de red.

Y la consulta final:

```javascript
db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })
```

Devuelve las 5 lecturas ordenadas de más antigua a más reciente."

---

## 6. LAS CAPTURAS (15 seg)

"Tengo tres capturas: una del índice creado, otra de la inserción con los 5 ObjectId, y otra del resultado de la consulta ordenado. Lo ejecuté todo en **mongosh** dentro del contenedor Docker."

---

## 7. POSIBLES PREGUNTAS DEL PROFE Y RESPUESTAS

### ¿Y si mañana tienes mil millones de lecturas?

"MongoDB escala con **sharding**. El shard key sería `vehicle_id`, el mismo campo que uso en el índice. No habría que cambiar el código."

### ¿Por qué `insertMany` y no cinco `insertOne`?

"`insertMany` hace **una sola operación de red**. Cinco `insertOne` serían cinco viajes al servidor. Con millones de pings la diferencia es enorme."

### ¿Y si quiero buscar vehículos por ubicación?

"Habría que crear un **índice 2dsphere** para geolocalización. Ese sería otro índice para otra consulta — eso es Query-First Design."

### ¿El `_id` no sirve como índice?

"El `_id` es único por documento. Si filtro por `_id` obtengo **una** lectura. Yo necesito **todas** las de un vehículo. Por eso uso `vehicle_id`."

### ¿Qué pasa si insertas un documento sin `battery`?

"MongoDB lo acepta sin problema. Es **esquema flexible**. Ese documento simplemente no tendrá campo `battery`, y al hacer `find` aparecerá sin él."

---

## RESUMEN PARA EL FINAL (10 seg)

"En resumen: MongoDB por su esquema flexible y sus índices compuestos. Una colección `telemetria` con `vehicle_id + timestamp` como clave de ordenación. Dos correcciones a la IA: incrustar en vez de referenciar, e índice compuesto en vez de simple. Y todo funcionando en Docker con mongosh."
