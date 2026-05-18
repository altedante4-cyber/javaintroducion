# 3. Análisis de Auditoría (CE.a, CE.c)

## 3.1. Introducción a la Auditoría de Código Generado por IA

### 3.1.1. Concepto de Auditoría de Generación IA

La auditoría de generación mediante inteligencia artificial es el proceso mediante el cual un arquitecto de datos revisa, valida y corrige el código sintetizado por un modelo generativo (GPT, Gemini, Claude, etc.) antes de incorporarlo a un sistema productivo. En el contexto de EcoDrive, este proceso de auditoría es especialmente crítico porque los asistentes de IA han sido entrenados predominantemente con documentación, foros y repositorios que durante décadas han estado dominados por el paradigma SQL y el modelo relacional. Como consecuencia directa, la IA tiende a trasladar de forma inconsciente los patrones de diseño de bases de datos relacionales a entornos NoSQL, produciendo código que, aunque sintácticamente válido, resulta arquitectónicamente incorrecto para el motor de base de datos objetivo.

Este fenómeno no es trivial: la IA no «piensa» en términos de agregados, particiones físicas, modelos de grafos o estructuras de datos en memoria. La IA genera secuencias de tokens estadísticamente probables basadas en su corpus de entrenamiento, y dado que el corpus contiene ingentes cantidades de SQL y pocos ejemplos de modelado NoSQL experto, el sesgo relacional emerge de forma natural. Detectarlo y corregirlo es responsabilidad ineludible del arquitecto de datos.

### 3.1.2. El Sesgo Relacional en la Generación Automática

El sesgo relacional se manifiesta de las siguientes formas concretas, todas ellas observadas durante la auditoría de los scripts generados para EcoDrive:

1. **Normalización automática:** La IA separa en tablas/colecciones distintas entidades que en el mundo NoSQL deberían formar un único agregado. En MongoDB, esto se traduce en colecciones separadas con referencias por ID; en Cassandra, en la creación de tablas que requieren `ALLOW FILTERING` porque no se diseñaron pensando en la consulta.

2. **Claves primarias con propósito puramente identificativo:** La IA genera `PRIMARY KEY (id)` como si fuera un `SERIAL` de PostgreSQL, sin comprender que en Cassandra la clave primaria tiene un propósito físico de distribución de datos en el anillo del clúster.

3. **Ignorancia de las estructuras de datos nativas:** Para Redis, la IA propone genéricos `SET`/`GET` con JSON serializado, ignorando estructuras como `HASH`, `ZSET`, `EXPIRE`, `INCRBY` o `DECRBY` que son precisamente las que dotan de valor a Redis como base de datos en memoria.

4. **Relaciones sin semántica en grafos:** En Neo4j, la IA crea nodos aislados o relaciones genéricas `(:User)-[:RELATED_TO]->(:User)`, desaprovechando toda la potencia del modelo de grafos: relaciones con dirección, tipo semántico y propiedades en el propio borde.

### 3.1.3. Pensar en Agregados: El Cambio de Mentalidad Fundamental

Para auditar correctamente el código generado, es imprescindible comprender qué significa «pensar en agregados». En el modelo relacional, normalizamos datos para eliminar redundancias y definir relaciones mediante claves foráneas. En el modelo documental (MongoDB) y en el modelo de columnas (Cassandra), el paradigma es opuesto: agrupamos en una misma unidad de almacenamiento todos los datos que se consultan y modifican juntos.

El agregado es la unidad atómica de coherencia en NoSQL. Cuando la IA genera código que separa en colecciones distintas `vehiculos` y `reparaciones`, está rompiendo el agregado: cada vez que la aplicación necesite mostrar un vehículo con su historial de reparaciones, tendrá que realizar dos lecturas y un join en memoria del lado del cliente. Esto contradice directamente el principio fundamental de MongoDB: «si lees los datos juntos, almacénalos juntos».

### 3.1.4. Query-First Design

El Query-First Design es una metodología de modelado que invierte el orden tradicional de diseño. En SQL, primero diseñamos el esquema entidad-relación y luego escribimos las consultas. En NoSQL, primero identificamos exactamente qué consultas va a realizar la aplicación y luego diseñamos el esquema para que esas consultas sean óptimas.

Esto implica:
- Conocer de antemano los patrones de acceso (lecturas vs. escrituras, frecuencia, volumen).
- Diseñar la Partition Key en Cassandra para que la consulta objetivo toque una sola partición.
- Diseñar el agregado en MongoDB para que una sola lectura devuelva todo lo necesario.
- Elegir la estructura de datos en Redis que minimice la complejidad computacional de la operación.

Durante la auditoría, hemos aplicado Query-First Design en los cuatro motores, partiendo de las consultas reales que EcoDrive necesita y corrigiendo los esquemas generados por la IA.

### 3.1.5. Persistencia Políglota

La persistencia políglota es el patrón arquitectónico que consiste en utilizar diferentes tecnologías de bases de datos, cada una optimizada para un tipo de carga de trabajo específico, en lugar de forzar todos los datos a un único motor. EcoDrive utiliza cuatro motores porque cada servicio tiene requisitos radicalmente distintos:

| Servicio | Motor | Motivo |
|---|---|---|
| Catálogo de vehículos (A) | MongoDB | Esquema flexible, datos semi-estructurados, agregados de vehículo+reparaciones |
| Telemetría IoT (B) | Cassandra | Escrituras masivas, escalabilidad horizontal, consultas por vehículo |
| Sesiones y caché (C) | Redis | Latencia de microsegundos, datos efímeros con TTL, estructuras atómicas |
| Red social carpooling (D) | Neo4j | Relaciones complejas, navegación por grafos, recomendaciones sociales |

### 3.1.6. Relación con los Criterios CE.a y CE.c

Este apartado de análisis de auditoría se vincula directamente con los criterios de evaluación del RA7:

- **CE.a (Características de los sistemas NoSQL):** Cada corrección demuestra la aplicación práctica de las características fundamentales de cada sistema: ausencia de esquema en MongoDB, distribución por Partition Key en Cassandra, modelos de datos en memoria en Redis, y navegabilidad por relaciones en Neo4j.

- **CE.c (Elementos utilizados en estas bases de datos):** La auditoría identifica y justifica la elección de elementos concretos: agregados incrustados en MongoDB, Partition Key y Clustering Columns en Cassandra, tipos de datos HASH y TTL en Redis, y relaciones semánticas en Neo4j.

A lo largo de las siguientes secciones, se documenta exhaustivamente cada corrección realizada sobre el código generado por IA, incluyendo el código erróneo original, el código corregido y la justificación técnica detallada de cada cambio.

---

## 3.2. Auditoría de MongoDB: Corrección de Normalización Encubierta

### 3.2.1. El Error: Código Generado por la IA (INCORRECTO)

Cuando se solicitó a la IA que generara un script de inserción de datos para el servicio de catálogo de vehículos de EcoDrive, el modelo generó el siguiente código:

```javascript
// ============================================================
// CÓDIGO GENERADO POR IA - VERSIÓN INCORRECTA
// Normalización Encubierta: separa vehículos y reparaciones
// en colecciones distintas con relación por ID.
// ============================================================

// Colección 1: vehiculos
db.vehiculos.insertMany([
  {
    _id: ObjectId("661a00000000000000000001"),
    matricula: "PAT-001",
    tipo: "patinete",
    modelo: "Xiaomi Pro 3",
    año: 2024,
    peso_maximo_kg: 120,
    autonomia_km: 45,
    estado: "disponible"
  },
  {
    _id: ObjectId("661a00000000000000000002"),
    matricula: "BIC-001",
    tipo: "bicicleta",
    modelo: "Orbea Vibe H30",
    año: 2023,
    marchas: 9,
    peso_kg: 16.5,
    estado: "mantenimiento"
  },
  {
    _id: ObjectId("661a00000000000000000003"),
    matricula: "COC-001",
    tipo: "coche",
    modelo: "Renault Zoe ZE50",
    año: 2024,
    tipo_combustible: "electrico",
    capacidad_bateria_kwh: 52,
    plazas: 5,
    estado: "disponible"
  }
]);

// Colección 2: reparaciones (SEPARADA de vehiculos)
db.reparaciones.insertMany([
  {
    _id: ObjectId("661b00000000000000000001"),
    vehiculo_id: ObjectId("661a00000000000000000001"),
    fecha: new Date("2025-01-15"),
    taller: "EcoFix Centro",
    pieza_reemplazada: "rueda delantera",
    coste: 45.00,
    observaciones: "Pinchazo por cristal en carril bici"
  },
  {
    _id: ObjectId("661b00000000000000000002"),
    vehiculo_id: ObjectId("661a00000000000000000001"),
    fecha: new Date("2025-03-20"),
    taller: "EcoFix Centro",
    pieza_reemplazada: "batería",
    coste: 120.00,
    observaciones: "Batería no retenía carga completa"
  },
  {
    _id: ObjectId("661b00000000000000000003"),
    vehiculo_id: ObjectId("661a00000000000000000002"),
    fecha: new Date("2025-02-10"),
    taller: "EcoBici Taller",
    pieza_reemplazada: "cadena y piñón",
    coste: 35.50,
    observaciones: "Desgaste por uso intensivo"
  }
]);
```

**Consulta generada para obtener un vehículo con sus reparaciones:**

```javascript
// INCORRECTO: Join manual en el cliente
var vehiculo = db.vehiculos.findOne({ matricula: "PAT-001" });
var reparaciones = db.reparaciones.find({ vehiculo_id: vehiculo._id }).toArray();

// El programador debe combinar manualmente los dos conjuntos de datos
var resultado = {
  vehiculo: vehiculo,
  historial_reparaciones: reparaciones
};
printjson(resultado);
```

### 3.2.2. Antipatrón Detectado: Normalización Encubierta

El antipatrón de **Normalización Encubierta** consiste en aplicar principios del diseño relacional (separar entidades en tablas distintas con claves foráneas) dentro de una base de datos documental como MongoDB. La IA ha reproducido el esquema mental de un modelo entidad-relación donde `vehiculos` y `reparaciones` son dos tablas relacionadas por el campo `vehiculo_id`.

**¿Por qué es incorrecto en MongoDB?**

1. **Joins manuales en la capa de aplicación:** Cada vez que la aplicación necesite mostrar la ficha completa de un vehículo con su historial de reparaciones —que es el caso de uso principal— deberá ejecutar dos consultas y combinar los resultados manualmente en el código de la aplicación. Esto duplica la latencia de red y añade complejidad algorítmica innecesaria.

2. **Pérdida de localidad de datos:** Los documentos de `reparaciones` se almacenan físicamente en una ubicación distinta que los documentos de `vehiculos`. MongoDB no garantiza ninguna cercanía física entre colecciones diferentes. Esto significa que, incluso en un clúter replicado, los datos que siempre se leen juntos están almacenados por separado, desperdiciando los beneficios de la localidad de datos.

3. **Atomicidad limitada:** Al estar separados en dos colecciones, no es posible realizar operaciones atómicas que afecten simultáneamente al vehículo y a sus reparaciones. Si la aplicación necesita actualizar el estado del vehículo a "disponible" tras completar una reparación, estas dos operaciones no pueden encapsularse en una única transacción sin recurrir a transacciones multi-documento, que tienen un rendimiento significativamente menor.

4. **Multiplicación de accesos a red:** En MongoDB, cada consulta implica un viaje de ida y vuelta por la red entre la aplicación y el servidor de bases de datos. Si una pantalla muestra un listado de 50 vehículos con sus últimas reparaciones, el enfoque de la IA requeriría 51 consultas (1 para los vehículos + 1 por cada vehículo para sus reparaciones). Con documentos incrustados, sigue siendo una sola consulta.

5. **Esquema rígido implícito:** La IA ha creado una colección `reparaciones` con un esquema uniforme (fecha, taller, pieza_reemplazada, coste, observaciones), cuando en realidad las reparaciones pueden requerir documentos parcialmente diferentes: una reparación programada, una reparación de emergencia, un mantenimiento preventivo, etc. Al separar en colección propia, la IA ha fijado implícitamente un esquema.

### 3.2.3. Código Corregido: Agregados Incrustados

Aplicando el principio de diseño por agregados y la guía del Anexo A2 (Incrustar vs. Referenciar), el código corregido unifica vehículo y sus reparaciones en un único documento:

```javascript
// ============================================================
// CÓDIGO AUDITADO Y CORREGIDO
// Agregado: vehículo con historial de reparaciones incrustado
// Los datos que se leen juntos se almacenan juntos.
// ============================================================

db.vehiculos.insertMany([
  {
    _id: ObjectId("661a00000000000000000001"),
    matricula: "PAT-001",
    tipo: "patinete",
    modelo: "Xiaomi Pro 3",
    año: 2024,
    peso_maximo_kg: 120,
    autonomia_km: 45,
    estado: "disponible",
    reparaciones: [
      {
        fecha: new Date("2025-01-15"),
        taller: "EcoFix Centro",
        pieza_reemplazada: "rueda delantera",
        coste: 45.00,
        observaciones: "Pinchazo por cristal en carril bici",
        tipo_reparacion: "correctiva"
      },
      {
        fecha: new Date("2025-03-20"),
        taller: "EcoFix Centro",
        pieza_reemplazada: "batería",
        coste: 120.00,
        observaciones: "Batería no retenía carga completa",
        tipo_reparacion: "correctiva"
      }
    ],
    ultima_revision: new Date("2025-03-20"),
    proxima_revision_programada: new Date("2025-06-20")
  },
  {
    _id: ObjectId("661a00000000000000000002"),
    matricula: "BIC-001",
    tipo: "bicicleta",
    modelo: "Orbea Vibe H30",
    año: 2023,
    marchas: 9,
    peso_kg: 16.5,
    estado: "mantenimiento",
    reparaciones: [
      {
        fecha: new Date("2025-02-10"),
        taller: "EcoBici Taller",
        pieza_reemplazada: "cadena y piñón",
        coste: 35.50,
        observaciones: "Desgaste por uso intensivo",
        tipo_reparacion: "preventiva"
      }
    ],
    ultima_revision: new Date("2025-02-10"),
    proxima_revision_programada: new Date("2025-05-10")
  },
  {
    _id: ObjectId("661a00000000000000000003"),
    matricula: "COC-001",
    tipo: "coche",
    modelo: "Renault Zoe ZE50",
    año: 2024,
    tipo_combustible: "electrico",
    capacidad_bateria_kwh: 52,
    plazas: 5,
    estado: "disponible",
    reparaciones: [],
    ultima_revision: new Date("2024-12-01"),
    proxima_revision_programada: new Date("2025-06-01")
  }
]);
```

**Consulta corregida:**

```javascript
// CORRECTO: Una sola consulta, un solo documento, un solo viaje
var vehiculo = db.vehiculos.findOne(
  { matricula: "PAT-001" },
  { matricula: 1, modelo: 1, estado: 1, reparaciones: 1 }
);

// El historial de reparaciones YA está dentro del documento
printjson({
  vehiculo: vehiculo.matricula,
  modelo: vehiculo.modelo,
  num_reparaciones: vehiculo.reparaciones.length,
  ultima_reparacion: vehiculo.reparaciones.slice(-1)[0]
});
```

### 3.2.4. Justificación Técnica Detallada de la Corrección

**Reducción de operaciones de lectura:**

En la versión incorrecta, obtener la ficha completa del patinete PAT-001 con su historial requería 2 consultas independientes. En la versión corregida, requiere 1 consulta. Esto supone una reducción del 50% en operaciones de lectura. En un escenario real con cientos de consultas por segundo, este ahorro es determinante para la capacidad de carga del servidor.

**Eliminación de joins manuales:**

El join manual implementado en JavaScript en la versión incorrecta obligaba a:
1. Esperar la primera consulta (`findOne`).
2. Extraer el `_id` del resultado.
3. Construir una segunda consulta con ese `_id`.
4. Esperar la segunda consulta.
5. Combinar manualmente ambas estructuras de datos.

En la versión corregida, este proceso desaparece. La aplicación recibe directamente el agregado completo.

**Mejora de localidad de datos:**

MongoDB almacena los documentos BSON en disco en bloques contiguos. Al incrustar las reparaciones dentro del documento del vehículo, todos los datos relativos a un mismo vehículo se almacenan en una única región del disco. Esto maximiza la eficiencia de la caché de almacenamiento y reduce los accesos a disco para lecturas secuenciales.

**Flexibilidad de esquema:**

La versión corregida permite que cada reparación tenga campos diferentes sin necesidad de modificar un esquema central. Por ejemplo, una reparación de un coche podría incluir un campo `codigo_dtc` (Diagnostic Trouble Code) que no tendría sentido para un patinete:

```javascript
reparaciones: [
  {
    fecha: new Date("2025-04-01"),
    taller: "EcoGaraje Norte",
    pieza_reemplazada: "inversor de tracción",
    coste: 890.00,
    codigo_dtc: "P0AA6",  // Campo específico de coches
    tipo_reparacion: "correctiva"
  }
]
```

Esta flexibilidad sería imposible en un esquema relacional normalizado, pero es natural en MongoDB gracias a su naturaleza sin esquema.

**Atomicidad:**

Al estar las reparaciones dentro del mismo documento, MongoDB puede garantizar atomicidad a nivel de documento. Si la aplicación necesita añadir una reparación y actualizar la `ultima_revision` y la `proxima_revision_programada`, todo puede hacerse en una sola operación:

```javascript
db.vehiculos.updateOne(
  { matricula: "PAT-001" },
  {
    $push: {
      reparaciones: {
        fecha: new Date(),
        taller: "EcoFix Centro",
        pieza_reemplazada: "manillar",
        coste: 25.00,
        tipo_reparacion: "correctiva"
      }
    },
    $set: {
      ultima_revision: new Date(),
      proxima_revision_programada: new Date(Date.now() + 90 * 24 * 3600 * 1000)
    }
  }
);
```

### 3.2.5. Ventajas e Inconvenientes del Modelo Incrustado

**Ventajas:**
- Reducción drástica del número de consultas.
- Atomicidad en operaciones de vehículo + reparaciones.
- Localidad de datos: todo el agregado físico está junto.
- Flexibilidad de esquema para cada reparación individual.
- Modelo mental alineado con el dominio: "un vehículo TIENE reparaciones".

**Inconvenientes (a considerar):**
- Límite de tamaño de documento BSON (16 MB). En vehículos con miles de reparaciones podría alcanzarse. Para EcoDrive, con una media estimada de 10-20 reparaciones por vehículo al año, es perfectamente viable.
- Si el historial de reparaciones creciese sin límite, habría que plantearse una colección separada. No es el caso.
- Actualizar una reparación existente requiere localizarla dentro del array con el operador posicional `$`.

### 3.2.6. Principios NoSQL Aplicados

| Principio | Aplicación |
|---|---|
| Diseño por agregados | Vehículo + reparaciones forman un agregado natural |
| Esquema flexible | Cada reparación puede tener campos diferentes |
| Denormalización consciente | Aceptamos duplicación de datos (redundancia del nombre del taller en cada reparación) a cambio de rendimiento en lectura |
| Embedding como opción por defecto | Los datos se leen juntos → se almacenan juntos |

---

## 3.3. Auditoría de Cassandra: Corrección de Partition Key Errónea

### 3.3.1. El Error: Código Generado por la IA (INCORRECTO)

Cuando se solicitó a la IA que diseñara la estructura de tabla para el servicio de telemetría IoT (Servicio B) en Cassandra, el modelo generó el siguiente esquema:

```sql
-- ============================================================
-- CÓDIGO GENERADO POR IA - VERSIÓN INCORRECTA
-- Partition Key con baja cardinalidad: tipo_vehiculo
-- Esto genera hotspots en el clúster.
-- ============================================================

CREATE TABLE IF NOT EXISTS eco_drive.telemetria (
    tipo_vehiculo TEXT,           -- 'patinete', 'bicicleta', 'coche'
    timestamp TIMESTAMP,
    vehicle_id UUID,
    latitud DOUBLE,
    longitud DOUBLE,
    velocidad_kmh DOUBLE,
    nivel_bateria INT,
    consumo_watts DOUBLE,
    PRIMARY KEY (tipo_vehiculo, timestamp, vehicle_id)
);

-- Inserción de datos incorrecta (propuesta por la IA)
INSERT INTO eco_drive.telemetria (tipo_vehiculo, timestamp, vehicle_id, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES ('coche', '2025-04-10 10:00:00', uuid(), 40.4168, -3.7038, 45.2, 85, 12000);

INSERT INTO eco_drive.telemetria (tipo_vehiculo, timestamp, vehicle_id, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES ('coche', '2025-04-10 10:00:05', uuid(), 40.4169, -3.7039, 47.1, 84, 12100);

INSERT INTO eco_drive.telemetria (tipo_vehiculo, timestamp, vehicle_id, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES ('patinete', '2025-04-10 10:00:00', uuid(), 40.4170, -3.7040, 15.3, 92, 250);

INSERT INTO eco_drive.telemetria (tipo_vehiculo, timestamp, vehicle_id, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES ('patinete', '2025-04-10 10:00:05', uuid(), 40.4171, -3.7041, 16.0, 91, 260);

-- Consulta propuesta por la IA (¡requiere ALLOW FILTERING!)
SELECT * FROM eco_drive.telemetria
WHERE vehicle_id = 123e4567-e89b-12d3-a456-426614174000
ALLOW FILTERING;
```

### 3.3.2. Antipatrón Detectado: Partition Key de Baja Cardinalidad (Hotspot)

El diseño generado por la IA contiene un error arquitectónico grave: la Partition Key es `tipo_vehiculo`, un campo con únicamente 3 valores posibles ("patinete", "bicicleta", "coche").

**¿Por qué es catastrófico para Cassandra?**

Cassandra utiliza un anillo distribuido donde cada nodo es responsable de un rango de tokens. Cuando un dato se inserta, Cassandra aplica una función hash a la Partition Key para determinar qué nodo del anillo almacenará la partición:

```
token = hash("tipo_vehiculo" + valor)
```

Si la Partition Key tiene baja cardinalidad, el número de particiones posibles es reducido. En nuestro caso, solo existen 3 valores de `tipo_vehiculo`, lo que significa que Cassandra creará exactamente 3 particiones físicas:

| Partición | Nodo asignado | Vehículos que contiene |
|---|---|---|
| `hash("coche")` | Nodo A | TODOS los coches de EcoDrive |
| `hash("patinete")` | Nodo B | TODOS los patinetes de EcoDrive |
| `hash("bicicleta")` | Nodo C | TODAS las bicicletas de EcoDrive |

**Consecuencias directas:**

1. **Hotspot en el nodo de coches:** Si EcoDrive tiene 500 coches que emiten un ping cada 5 segundos, eso son 500 × (86400/5) = 8.640.000 escrituras diarias dirigidas a un único nodo. Mientras tanto, si hay 200 bicicletas y 300 patinetes, los otros dos nodos están infrautilizados.

2. **Desperdicio de capacidad del clúster:** Si el clúster tiene 6 nodos, 3 nodos estarán vacíos (sin datos) y los otros 3 soportarán toda la carga. Se ha perdido el 50% de la capacidad de cómputo.

3. **Distribución asimétrica en crecimiento:** Cuando EcoDrive añada 1000 coches más, todo el peso caerá sobre el mismo nodo. Los demás nodos permanecerán ociosos. El clúster escalará linealmente en número de nodos, pero la capacidad efectiva estará limitada por un único nodo: el que almacena la partición "coche".

4. **ALLOW FILTERING:** La consulta que la IA propone (`WHERE vehicle_id = ...`) requiere la cláusula `ALLOW FILTERING` porque `vehicle_id` no es parte de la clave primaria. Esto obliga a Cassandra a escanear todas las particiones (todos los tipos de vehículo) y dentro de cada una, todas las filas, para encontrar el `vehicle_id` solicitado. En una tabla con millones de registros, esta consulta agota los timeouts.

### 3.3.3. Explicación Técnica: Cómo Distribuye Cassandra los Datos

Para entender por qué la corrección es necesaria, hay que comprender el modelo de almacenamiento físico de Cassandra:

**Estructura de la clave primaria en Cassandra:**

```
PRIMARY KEY ((Partition Key), Clustering Column 1, Clustering Column 2, ...)
```

- **Partition Key (marcada con paréntesis dobles si es compuesta):** Determina el nodo del anillo donde se almacena la partición. Todos los datos con la misma Partition Key residen en el mismo nodo físico.

- **Clustering Columns:** Determinan el orden de los datos DENTRO de la partición. Los datos se ordenan en disco según el orden de las Clustering Columns.

Cassandra no permite consultas eficientes sin Partition Key porque eso requeriría un broadcast a todos los nodos del clúster.

**El orden físico en disco:**

Dentro de una partición, las filas se almacenan ordenadas según las Clustering Columns en orden ascendente. Esto significa que si definimos:

```sql
PRIMARY KEY (vehicle_id, timestamp)
```

Dentro de la partición de `vehicle_id = UUID-X`, las filas estarán ordenadas por `timestamp` de más antigua a más reciente. Podemos invertir el orden con `ORDER BY` o definiendo `WITH CLUSTERING ORDER BY (timestamp DESC)` en la creación de la tabla.

### 3.3.4. Código Corregido: Query-First Design

Partiendo de las consultas que EcoDrive realmente necesita:

1. **Consulta objetivo 1:** «Dado un vehicle_id, obtener todo su historial de telemetría ordenado por tiempo.»
2. **Consulta objetivo 2:** «Dado un vehicle_id, obtener las últimas N lecturas.»
3. **Consulta objetivo 3:** «Dado un vehicle_id, obtener las lecturas entre dos fechas.»

Ninguna de estas consultas necesita `tipo_vehiculo`. Todas necesitan `vehicle_id` como filtro. Aplicando Query-First Design:

```sql
-- ============================================================
-- CÓDIGO AUDITADO Y CORREGIDO
-- Partition Key: vehicle_id (alta cardinalidad, miles de valores)
-- Clustering Column: timestamp (orden temporal dentro del vehículo)
-- ============================================================

CREATE TABLE IF NOT EXISTS eco_drive.telemetria (
    vehicle_id UUID,              -- Partition Key: alta cardinalidad
    timestamp TIMESTAMP,          -- Clustering Column: orden dentro de la partición
    tipo_vehiculo TEXT,           -- Ahora es un atributo, no forma parte de la clave
    latitud DOUBLE,
    longitud DOUBLE,
    velocidad_kmh DOUBLE,
    nivel_bateria INT,
    consumo_watts DOUBLE,
    PRIMARY KEY (vehicle_id, timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Inserción de datos correcta
INSERT INTO eco_drive.telemetria (vehicle_id, timestamp, tipo_vehiculo, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES (123e4567-e89b-12d3-a456-426614174000, '2025-04-10 10:00:00', 'coche', 40.4168, -3.7038, 45.2, 85, 12000);

INSERT INTO eco_drive.telemetria (vehicle_id, timestamp, tipo_vehiculo, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES (123e4567-e89b-12d3-a456-426614174000, '2025-04-10 10:00:05', 'coche', 40.4169, -3.7039, 47.1, 84, 12100);

INSERT INTO eco_drive.telemetria (vehicle_id, timestamp, tipo_vehiculo, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES (123e4567-e89b-12d3-a456-426614174000, '2025-04-10 10:00:10', 'coche', 40.4170, -3.7040, 46.8, 84, 11950);

INSERT INTO eco_drive.telemetria (vehicle_id, timestamp, tipo_vehiculo, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES (987fcdeb-51a2-43d7-b890-123456789abc, '2025-04-10 10:00:00', 'patinete', 40.4180, -3.7050, 15.3, 92, 250);

INSERT INTO eco_drive.telemetria (vehicle_id, timestamp, tipo_vehiculo, latitud, longitud, velocidad_kmh, nivel_bateria, consumo_watts)
VALUES (987fcdeb-51a2-43d7-b890-123456789abc, '2025-04-10 10:00:05', 'patinete', 40.4181, -3.7051, 16.0, 91, 260);
```

**Consultas corregidas (eficientes, sin ALLOW FILTERING):**

```sql
-- Consulta 1: Historial completo de un vehículo (eficiente, una sola partición)
SELECT * FROM eco_drive.telemetria
WHERE vehicle_id = 123e4567-e89b-12d3-a456-426614174000;

-- Consulta 2: Últimas 10 lecturas de un vehículo (usa CLUSTERING ORDER BY)
SELECT * FROM eco_drive.telemetria
WHERE vehicle_id = 123e4567-e89b-12d3-a456-426614174000
LIMIT 10;

-- Consulta 3: Lecturas entre dos fechas (usa la Clustering Column)
SELECT * FROM eco_drive.telemetria
WHERE vehicle_id = 123e4567-e89b-12d3-a456-426614174000
  AND timestamp >= '2025-04-10 10:00:00'
  AND timestamp <= '2025-04-10 11:00:00';
```

### 3.3.5. Justificación Técnica Detallada de la Corrección

**Distribución equilibrada de datos:**

Con `vehicle_id` como Partition Key, Cassandra calcula:

```
token = hash("123e4567-e89b-12d3-a456-426614174000")
```

Cada vehículo tiene un UUID único. Con 1000 vehículos, hay 1000 valores distintos de Partition Key, y Cassandra distribuye uniformemente estas 1000 particiones entre todos los nodos del clúster. Si hay 4 nodos, cada nodo recibe aproximadamente 250 particiones. La carga de escritura se balancea perfectamente.

**Escalabilidad horizontal lineal:**

Cuando EcoDrive añada 1000 vehículos más, se crearán 1000 nuevas particiones que Cassandra distribuirá uniformemente. Si añadimos más nodos al clúster, Cassandra rebalancea automáticamente las particiones. La capacidad de escritura del sistema escala linealmente con el número de nodos.

**Consultas sin ALLOW FILTERING:**

Todas las consultas del sistema corregido incluyen la Partition Key (`vehicle_id`). Cassandra puede enrutar cada consulta directamente al nodo que contiene la partición, sin necesidad de broadcast. El tiempo de respuesta es determinista: O(1) en localización de la partición + O(log n) en búsqueda dentro de la partición (mergesort de SSTables).

**Orden físico en disco:**

Con `CLUSTERING ORDER BY (timestamp DESC)`, los datos más recientes están físicamente al principio de la partición. Esto hace que las consultas de "últimas N lecturas" (`LIMIT 10`) sean extremadamente rápidas: Cassandra simplemente lee las primeras 10 filas del SSTable, sin necesidad de ordenación adicional.

### 3.3.6. Principios NoSQL Aplicados

| Principio | Aplicación |
|---|---|
| Query-First Design | Tabla diseñada para responder `WHERE vehicle_id = ?` |
| Partition Key de alta cardinalidad | `vehicle_id` UUID con millones de valores posibles |
| Clustering Column para orden | `timestamp DESC` para consultar lo más reciente primero |
| Denormalización | `tipo_vehiculo` repetido en cada fila (no hay JOIN con tabla de vehículos) |
| Escalabilidad horizontal | Particiones distribuidas uniformemente entre nodos |

---

## 3.4. Auditoría de Redis: Corrección de Uso Pobre de Estructuras

### 3.4.1. El Error: Código Generado por la IA (INCORRECTO)

Cuando se solicitó a la IA que implementara la gestión de sesiones activas y batería de vehículos (Servicio C) en Redis, el modelo generó el siguiente código:

```bash
# ============================================================
# CÓDIGO GENERADO POR IA - VERSIÓN INCORRECTA
# Uso exclusivo de SET/GET con JSON serializado
# Sin TTL en sesiones
# Sin estructura jerárquica en las claves
# ============================================================

# Incorrecto: Guardar sesión como string JSON
SET sesion_usuario_1 '{"user_id": 1, "vehiculo_id": "PAT-001", "inicio": "2025-04-10T10:00:00", "estado": "activo", "tarifa_por_minuto": 0.25}'

# Incorrecto: Guardar batería como string JSON
SET bateria_PAT-001 '{"vehiculo": "PAT-001", "nivel": 85, "ultima_actualizacion": "2025-04-10T10:00:00", "autonomia_restante_km": 38}'

# Incorrecto: Guardar batería de otro vehículo
SET bateria_BIC-001 '{"vehiculo": "BIC-001", "nivel": 72, "ultima_actualizacion": "2025-04-10T10:00:00", "autonomia_restante_km": 25}'

# Incorrecto: Intentar decrementar batería (¡no funciona con JSON string!)
DECR bateria_PAT-001
# Error: WRONGTYPE Operation against a key holding the wrong kind of value

# Incorrecto: No hay TTL, la sesión nunca expira
# La sesión ocupará memoria para siempre aunque el viaje haya terminado
```

### 3.4.2. Antipatrón Detectado: Redis como Almacén de Texto Plano

La IA ha reducido Redis a un simple `Map<String, String>`, utilizando exclusivamente el tipo de dato más básico (Strings) para almacenar JSON serializado. Esto presenta múltiples problemas graves:

**Problema 1: Imposibilidad de actualización parcial.**

Para modificar un solo campo (por ejemplo, decrementar la batería de 85 a 84), la aplicación debe:
1. Ejecutar `GET bateria_PAT-001` (lectura del JSON completo).
2. Deserializar el JSON en memoria.
3. Modificar el campo `nivel` en la estructura deserializada.
4. Serializar de nuevo a JSON.
5. Ejecutar `SET bateria_PAT-001 '{"...json modificado..."}'` (reescritura completa).

Esto se conoce como **read-modify-write** y es inherentemente lento, no atómico y desperdicia ancho de banda de red y memoria. Para una plataforma como EcoDrive, donde las baterías se actualizan cada 5 segundos, la sobrecarga es inaceptable.

**Problema 2: Ausencia de TTL (Time To Live).**

Redis es una base de datos en memoria. La memoria RAM es un recurso finito y caro. Si las sesiones de viaje no tienen TTL, cada sesión iniciada se queda en memoria para siempre, incluso después de que el viaje haya terminado. En un día con 10.000 viajes, habrá 10.000 entradas en Redis ocupando memoria sin ningún propósito. Al cabo de una semana, 70.000 entradas. La memoria se agotará y Redis empezará a hacer evicción de claves según la política configurada, potencialmente eliminando datos activos.

**Problema 3: Nomenclatura plana sin jerarquía.**

Las claves `sesion_usuario_1`, `bateria_PAT-001` no siguen ningún patrón jerárquico. Esto impide:
- Escanear por prefijos (`SCAN sesion:*` no funcionaría).
- Agrupar lógicamente las claves relacionadas.
- Aprovechar las funcionalidades de Redis que operan por patrones de claves.

**Problema 4: DECR inaplicable sobre Strings JSON.**

El comando `DECR` solo funciona sobre strings que representan números enteros. Almacenar un JSON impide usar las operaciones atómicas de Redis sobre números. Esto es especialmente grave para el caso de uso de EcoDrive: decrementar la batería en tiempo real debería ser una operación O(1) y atómica, no un proceso de read-modify-write.

### 3.4.3. Código Corregido: Estructuras Nativas y TTL

Aplicando los principios del Anexo A3 (Redis: Más allá del Texto) y las buenas prácticas de Redis:

```bash
# ============================================================
# CÓDIGO AUDITADO Y CORREGIDO
# Uso de HASH para objetos (actualización parcial)
# Uso de EXPIRE para sesiones (autogestión de memoria)
# Uso de DECRBY para batería (operación atómica)
# Nomenclatura jerárquica con ":" (agrupación lógica)
# ============================================================

# -----------------------------------------------------------
# SESIONES ACTIVAS - HASH + TTL
# -----------------------------------------------------------

# Crear sesión de viaje con HASH (no JSON string)
# La clave sigue nomenclatura jerárquica: sesion:<user_id>
HSET sesion:1 user_id 1 vehiculo_id "PAT-001" \
     inicio "2025-04-10T10:00:00" estado "activo" \
     tarifa_por_minuto 0.25 latitud 40.4168 longitud -3.7038

# Establecer TTL: la sesión expira automáticamente en 3600 segundos (1 hora)
# Si el usuario no finaliza el viaje explícitamente, Redis lo limpia solo
EXPIRE sesion:1 3600

# Actualizar ubicación del usuario durante el viaje (actualización parcial)
HSET sesion:1 latitud 40.4190 longitud -3.7060

# Finalizar viaje manualmente
HSET sesion:1 estado "finalizado" fin "2025-04-10T10:45:00"
EXPIRE sesion:1 300  # Mantener 5 minutos para consultas post-viaje, luego borrar

# -----------------------------------------------------------
# BATERÍA DE VEHÍCULOS - HASH + DECRBY
# -----------------------------------------------------------

# Crear registro de batería para PAT-001
# Nomenclatura jerárquica: vehiculo:<matricula>:bateria
HSET vehiculo:PAT-001:bateria nivel 85 autonomia_km 38 \
     ultima_actualizacion "2025-04-10T10:00:00"

# Crear registro de batería para BIC-001
HSET vehiculo:BIC-001:bateria nivel 72 autonomia_km 25 \
     ultima_actualizacion "2025-04-10T10:00:00"

# Crear registro de batería para COC-001
HSET vehiculo:COC-001:bateria nivel 92 autonomia_km 180 \
     ultima_actualizacion "2025-04-10T10:00:00"

# Decrementar batería de PAT-001 en 2 unidades (simula consumo)
# DECRBY opera atómicamente sobre el campo 'nivel' del HASH
HINCRBY vehiculo:PAT-001:bateria nivel -2

# Verificar el nuevo valor de batería
HGET vehiculo:PAT-001:bateria nivel
# Resultado: "83"

# Actualizar autonomía restante
HSET vehiculo:PAT-001:bateria autonomia_km 37 \
     ultima_actualizacion "2025-04-10T10:05:00"

# -----------------------------------------------------------
# CONSULTA DE VEHÍCULOS CERCANOS - Obtención de baterías
# -----------------------------------------------------------

# Obtener batería de todos los campos de un vehículo
HGETALL vehiculo:PAT-001:bateria
# Resultado:
# 1) "nivel"
# 2) "83"
# 3) "autonomia_km"
# 4) "37"
# 5) "ultima_actualizacion"
# 6) "2025-04-10T10:05:00"

# Escanear todas las baterías (útil para el dashboard de operaciones)
SCAN 0 MATCH vehiculo:*:bateria COUNT 100
```

### 3.4.4. Justificación Técnica Detallada de la Corrección

**Actualización parcial con HASH:**

El tipo de datos `HASH` de Redis almacena un mapa de campos y valores. Con `HSET` se puede modificar un único campo sin afectar al resto. La diferencia es abismal:

- **Strings JSON (versión IA):** Para actualizar la latitud: 1 GET (2 KB de red) + deserialización + modificación + serialización + 1 SET (2 KB de red) = ~4 KB de tráfico de red y 2 operaciones.
- **HASH (versión corregida):** Para actualizar la latitud: 1 HSET (100 bytes de red) = ~100 bytes de tráfico de red y 1 operación.

En un sistema con 1000 vehículos actualizándose cada 5 segundos:
- Strings: 1000 × (4 KB) / 5s = 800 KB/s solo en tráfico de baterías.
- HASH: 1000 × (100 B) / 5s = 20 KB/s.

Factor de mejora: **40x menos tráfico de red**.

**Atomicidad sin condición de carrera:**

`HINCRBY vehiculo:PAT-001:bateria nivel -2` es una operación atómica. Redis garantiza que ningún otro comando se interponga durante su ejecución. En la versión con Strings, si dos hilos intentan decrementar la batería simultáneamente, ambos pueden leer el mismo valor (85), decrementar a 83 cada uno, y escribir 83, cuando el resultado correcto debería ser 81. Esto se conoce como **condición de carrera** y es imposible con `HINCRBY` porque la operación es atómica.

**Gestión automática de memoria con TTL:**

El TTL (Time To Live) permite que Redis borre automáticamente las claves cuando expiran. Para las sesiones de EcoDrive:
- Cada sesión se crea con `EXPIRE sesion:N 3600` (1 hora).
- Si el viaje termina correctamente, se actualiza el TTL a 300 segundos para permitir consultas post-viaje.
- Si el usuario abandona el vehículo sin finalizar el viaje (pérdida de conexión, abandono), Redis borra la sesión automáticamente a la hora.

Sin TTL, cada sesión muerta ocupa aproximadamente 500 bytes de RAM:
- 10.000 viajes/día × 500 bytes = 5 MB/día.
- En un mes sin TTL: 150 MB de memoria ocupada por datos inservibles.

**Nomenclatura jerárquica con dos puntos:**

El uso de `:` como separador jerárquico es un convenio estándar en Redis. Permite:
- Agrupar lógicamente: todas las claves que empiezan por `vehiculo:` son datos de vehículos.
- Escaneo por patrones: `SCAN 0 MATCH sesion:*` encuentra todas las sesiones activas.
- Eliminación masiva: `DEL vehiculo:PAT-001:*` borra todos los datos de un vehículo.
- Legibilidad: la jerarquía `vehiculo:<id>:bateria` es autoexplicativa.

### 3.4.5. Comparativa de Rendimiento

| Operación | Versión IA (String JSON) | Versión Corregida (HASH) | Mejora |
|---|---|---|---|
| Actualizar batería (-2%) | GET + deserializar + modificar + serializar + SET (~2 ms) | HINCRBY (~0.05 ms) | 40x |
| Actualizar ubicación | GET + deserializar + modificar + serializar + SET (~2 ms) | HSET (~0.05 ms) | 40x |
| Leer sesión completa | GET + deserializar (~0.5 ms) | HGETALL (~0.1 ms) | 5x |
| Limpieza de sesiones | Manual (script externo) | Automática (EXPIRE) | Operacional |
| Consumo de red por update | ~4 KB | ~100 bytes | 40x |

### 3.4.6. Principios NoSQL Aplicados

| Principio | Aplicación |
|---|---|
| Modelo de datos orientado a estructuras | HASH para objetos, no Strings serializados |
| Atomicidad sin bloqueos | HINCRBY para decremento de batería |
| Gestión de ciclo de vida | EXPIRE para limpieza automática de sesiones |
| Convención de nomenclatura | Claves jerárquicas con `:` para agrupación lógica |
| Datos efímeros como ciudadanos de primera clase | TTL como parte fundamental del diseño |

---

## 3.5. Auditoría de Neo4j: Corrección de Nodos-Tabla

### 3.5.1. El Error: Código Generado por la IA (INCORRECTO)

Cuando se solicitó a la IA que modelara la red social de carpooling (Servicio D) en Neo4j, el modelo generó el siguiente código:

```cypher
// ============================================================
// CÓDIGO GENERADO POR IA - VERSIÓN INCORRECTA
// Modelo tabular: nodos sin semántica relacional
// Relaciones genéricas sin dirección ni significado
// ============================================================

// Crear nodos como si fueran filas de una tabla
CREATE (u1:User {id: 1, nombre: "Ana", email: "ana@email.com", ciudad: "Madrid"});
CREATE (u2:User {id: 2, nombre: "Carlos", email: "carlos@email.com", ciudad: "Madrid"});
CREATE (u3:User {id: 3, nombre: "Elena", email: "elena@email.com", ciudad: "Barcelona"});

// Crear rutas como nodos sin relación con usuarios
CREATE (r1:Ruta {id: 1, origen: "Madrid", destino: "Valencia", distancia_km: 350});
CREATE (r2:Ruta {id: 2, origen: "Barcelona", destino: "Valencia", distancia_km: 350});

// Relaciones genéricas y sin dirección semántica
MATCH (u1:User {id: 1}), (u2:User {id: 2})
CREATE (u1)-[:RELACIONADO_CON]->(u2);

MATCH (u1:User {id: 1}), (u3:User {id: 3})
CREATE (u1)-[:RELACIONADO_CON]->(u3);

MATCH (u1:User {id: 1}), (r1:Ruta {id: 1})
CREATE (u1)-[:TIENE]->(r1);

MATCH (u3:User {id: 3}), (r2:Ruta {id: 2})
CREATE (u3)-[:TIENE]->(r2);

// Consulta para encontrar usuarios que van a Valencia (ineficiente y poco semántica)
MATCH (u:User)-[:TIENE]->(r:Ruta {destino: "Valencia"})
RETURN u.nombre, r.origen, r.destino;
```

### 3.5.2. Antipatrón Detectado: Nodos-Tabla y Relaciones Genéricas

Este es un ejemplo clásico de **Nodos-Tabla**, donde la IA modela el grafo como si fuera un esquema relacional: tablas convertidas en etiquetas de nodo, y relaciones genéricas sin semántica que actúan como claves foráneas.

**¿Por qué es incorrecto en Neo4j?**

1. **Relaciones sin semántica (`:RELACIONADO_CON`, `:TIENE`):** En un grafo de conocimiento (knowledge graph), las relaciones son el elemento más importante. Una relación `:RELACIONADO_CON` no comunica nada. ¿Son amigos? ¿Compañeros de trabajo? ¿Viajaron juntos? En el mundo del carpooling, necesitamos saber relaciones específicas como `:AMIGO_DE`, `:VIAJA_A`, `:COMPARTE_TRAYECTO`.

2. **Falta de dirección semántica:** La relación `(u1)-[:RELACIONADO_CON]->(u2)` tiene dirección, pero no tiene significado direccional. ¿Ana conoce a Carlos pero Carlos no conoce a Ana? No lo sabemos. Para la amistad en carpooling, la dirección puede ser relevante (seguimiento, reputación).

3. **Propiedades en nodos que deberían estar en relaciones:** La información de *cuándo* dos usuarios se hicieron amigos, o *cuántas veces* han compartido trayecto, debería estar en la relación, no en los nodos. La IA no utiliza propiedades en las relaciones.

4. **Modelo plano sin traversal aprovechable:** La consulta `MATCH (u:User)-[:TIENE]->(r:Ruta {destino: "Valencia"})` es básicamente un `JOIN` entre dos tablas. No está aprovechando la potencia del grafo para navegación multinivel (amigos de amigos, recomendaciones basadas en patrones de viaje).

5. **Ausencia de relaciones entre usuarios y destinos directas:** La ruta se modela como un nodo intermedio, pero en un modelo de grafo bien diseñado, un usuario debería poder tener una relación directa `:VIAJA_A` con el destino (como concepto), no a través de un nodo `Ruta` que actúa como tabla puente.

### 3.5.3. Código Corregido: Relaciones Semánticas con Dirección y Propiedades

Aplicando los principios del Anexo A4 (Neo4j: Las Relaciones son Ciudadanos de Primera):

```cypher
// ============================================================
// CÓDIGO AUDITADO Y CORREGIDO
// Relaciones semánticas con dirección
// Propiedades en relaciones
// Modelo navegable para consultas sociales complejas
// ============================================================

// Crear nodos de usuario con perfil social
CREATE (ana:User {
    nombre: "Ana",
    email: "ana@email.com",
    ciudad: "Madrid",
    reputacion: 4.8,
    verificado: true,
    fecha_registro: date("2024-09-01")
});

CREATE (carlos:User {
    nombre: "Carlos",
    email: "carlos@email.com",
    ciudad: "Madrid",
    reputacion: 4.5,
    verificado: true,
    fecha_registro: date("2024-10-15")
});

CREATE (elena:User {
    nombre: "Elena",
    email: "elena@email.com",
    ciudad: "Barcelona",
    reputacion: 4.9,
    verificado: true,
    fecha_registro: date("2024-08-20")
});

// Crear nodos de destino (ciudades, no rutas como tabla puente)
CREATE (madrid:Destino {nombre: "Madrid", pais: "España"});
CREATE (valencia:Destino {nombre: "Valencia", pais: "España"});
CREATE (barcelona:Destino {nombre: "Barcelona", pais: "España"});

// -----------------------------------------------------------
// RELACIONES SEMÁNTICAS CON DIRECCIÓN
// -----------------------------------------------------------

// Ana y Carlos son amigos (amistad recíproca con propiedades)
MATCH (ana:User {nombre: "Ana"}), (carlos:User {nombre: "Carlos"})
CREATE (ana)-[:AMIGO_DE {
    desde: date("2024-11-01"),
    nivel_confianza: "alto",
    viajes_compartidos: 3
}]->(carlos);

MATCH (carlos:User {nombre: "Carlos"}), (ana:User {nombre: "Ana"})
CREATE (carlos)-[:AMIGO_DE {
    desde: date("2024-11-01"),
    nivel_confianza: "alto",
    viajes_compartidos: 3
}]->(ana);

// Ana conoce a Elena (amistad unidireccional: Ana sigue a Elena)
MATCH (ana:User {nombre: "Ana"}), (elena:User {nombre: "Elena"})
CREATE (ana)-[:AMIGO_DE {
    desde: date("2025-01-15"),
    nivel_confianza: "medio",
    viajes_compartidos: 1
}]->(elena);

// Relaciones de viaje: VIAJA_A con dirección y propiedades
MATCH (ana:User {nombre: "Ana"}), (valencia:Destino {nombre: "Valencia"})
CREATE (ana)-[:VIAJA_A {
    frecuencia: "semanal",
    ultimo_viaje: date("2025-04-08"),
    hora_preferida: "08:00",
    plazas_ofrecidas: 3,
    precio_sugerido_eur: 15.00
}]->(valencia);

MATCH (carlos:User {nombre: "Carlos"}), (valencia:Destino {nombre: "Valencia"})
CREATE (carlos)-[:VIAJA_A {
    frecuencia: "quincenal",
    ultimo_viaje: date("2025-04-01"),
    hora_preferida: "07:30",
    plazas_ofrecidas: 2,
    precio_sugerido_eur: 15.00
}]->(valencia);

MATCH (elena:User {nombre: "Elena"}), (valencia:Destino {nombre: "Valencia"})
CREATE (elena)-[:VIAJA_A {
    frecuencia: "mensual",
    ultimo_viaje: date("2025-03-20"),
    hora_preferida: "09:00",
    plazas_ofrecidas: 1,
    precio_sugerido_eur: 18.00
}]->(valencia);

MATCH (elena:User {nombre: "Elena"}), (barcelona:Destino {nombre: "Barcelona"})
CREATE (elena)-[:RESIDE_EN]->(barcelona);

MATCH (ana:User {nombre: "Ana"}), (madrid:Destino {nombre: "Madrid"})
CREATE (ana)-[:RESIDE_EN]->(madrid);

MATCH (carlos:User {nombre: "Carlos"}), (madrid:Destino {nombre: "Madrid"})
CREATE (carlos)-[:RESIDE_EN]->(madrid);
```

### 3.5.4. Consultas Sociales Complejas (Potencial del Grafo)

**Consulta 1: Usuarios que viajan a Valencia y son amigos entre sí**

```cypher
// CORRECTO: Relaciones semánticas permiten consultas expresivas
MATCH (u1:User)-[:VIAJA_A]->(d:Destino {nombre: "Valencia"})
MATCH (u2:User)-[:VIAJA_A]->(d)
MATCH (u1)-[:AMIGO_DE]->(u2)
WHERE u1.nombre < u2.nombre  // Evitar duplicados simétricos
RETURN u1.nombre AS usuario1,
       u2.nombre AS usuario2,
       u1.hora_preferida AS hora_u1,
       u2.hora_preferida AS hora_u2,
       d.nombre AS destino
ORDER BY u1.nombre;
```

**Resultado esperado:**

| usuario1 | usuario2 | hora_u1 | hora_u2 | destino |
|---|---|---|---|---|
| Ana | Carlos | 08:00 | 07:30 | Valencia |
| Ana | Elena | 08:00 | 09:00 | Valencia |

**Consulta 2: Amigos de amigos que viajan a Valencia (recomendaciones)**

```cypher
// Potencia del grafo: navegación multinivel
MATCH (yo:User {nombre: "Ana"})
MATCH (yo)-[:AMIGO_DE]->(amigo)-[:AMIGO_DE]->(amigo2:User)
MATCH (amigo2)-[:VIAJA_A]->(d:Destino {nombre: "Valencia"})
WHERE NOT (yo)-[:AMIGO_DE]->(amigo2)  // Que no sean amigos directos
RETURN amigo2.nombre AS recomendado,
       count(amigo) AS amigos_en_comun,
       collect(amigo.nombre) AS lista_amigos_comun,
       amigo2.reputacion AS reputacion
ORDER BY amigos_en_comun DESC, reputacion DESC
LIMIT 5;
```

**Explicación de la navegación en grafo:**

Esta consulta recorre el grafo en tres niveles:
1. Nivel 1: `(Ana)-[:AMIGO_DE]->(amigo)` — encuentra los amigos directos de Ana.
2. Nivel 2: `(amigo)-[:AMIGO_DE]->(amigo2)` — encuentra los amigos de esos amigos.
3. Nivel 3: `(amigo2)-[:VIAJA_A]->(Valencia)` — filtra solo los que viajan a Valencia.

En SQL, esto requeriría múltiples JOINs y subconsultas con complejidad O(n³). En Neo4j, la navegación por el grafo es la operación natural y se ejecuta en tiempo lineal respecto al número de relaciones traversadas.

**Consulta 3: Detección de usuarios con mismos horarios y destino**

```cypher
// Encontrar coincidencias perfectas para carpooling
MATCH (u1:User)-[:VIAJA_A {hora_preferida: "08:00"}]->(d:Destino {nombre: "Valencia"})
MATCH (u2:User)-[:VIAJA_A {hora_preferida: "08:00"}]->(d)
WHERE u1.nombre < u2.nombre
RETURN u1.nombre AS usuario,
       u2.nombre AS companero,
       d.nombre AS destino,
       "08:00" AS hora,
       u1.plazas_ofrecidas + u2.plazas_ofrecidas AS plazas_totales
ORDER BY plazas_totales DESC;
```

### 3.5.5. Justificación Técnica Detallada de la Corrección

**Navegación eficiente (Traversal):**

En Neo4j, el traversal es el mecanismo fundamental de acceso a datos. A diferencia de las tablas SQL donde cada JOIN requiere una operación de hash-match o nested-loop, en un grafo el traversal sigue punteros físicos entre nodos y relaciones. La corrección introducida permite a Neo4j:

1. Comenzar en el nodo `Ana`.
2. Seguir el puntero físico de la relación `:AMIGO_DE` para llegar a `Carlos`.
3. Seguir el puntero físico de `:VIAJA_A` para llegar a `Valencia`.

Cada paso es una operación O(1) de acceso directo por puntero, no una búsqueda en índice.

**Semántica de relaciones como elemento de filtrado:**

Las relaciones con nombre semántico permiten filtros expresivos. `:AMIGO_DE` y `:VIAJA_A` no son solo etiquetas: son tipos de relación que Neo4j indexa por separado. La consulta `MATCH (u1)-[:VIAJA_A]->(d)` no tiene que examinar todas las relaciones de `u1`, solo las de tipo `:VIAJA_A`. Esto reduce drásticamente el espacio de búsqueda.

**Propiedades en relaciones como metadatos de contexto:**

Almacenar `frecuencia`, `ultimo_viaje`, `plazas_ofrecidas` en la relación `:VIAJA_A` permite consultar no solo **qué** conexión existe, sino **cómo** es esa conexión. Esto es imposible en el modelo de la IA, donde la ruta era un nodo separado con esos atributos, obligando a un JOIN adicional.

**Amigos de amigos (navegación multinivel):**

La detección de amigos de amigos es el caso de uso emblemático de los grafos. En el modelo incorrecto de la IA, habría que hacer:
```cypher
MATCH (u1:User)-[:RELACIONADO_CON]->(intermedio:User)-[:RELACIONADO_CON]->(u2:User)
```

Pero como todas las relaciones se llaman igual, no se distingue si la conexión es de amistad, laboral, o de viaje. En el modelo corregido, `:AMIGO_DE` es semánticamente precisa y la intención de la consulta es explícita.

### 3.5.6. Comparativa: Modelo Incorrecto vs. Corregido

| Aspecto | Modelo IA (incorrecto) | Modelo Corregido |
|---|---|---|
| Relaciones | Genéricas (`:RELACIONADO_CON`, `:TIENE`) | Semánticas (`:AMIGO_DE`, `:VIAJA_A`, `:RESIDE_EN`) |
| Dirección | Sin significado direccional | Dirección significativa (quién sigue a quién) |
| Propiedades en relaciones | No usa | `desde`, `frecuencia`, `plazas_ofrecidas`, etc. |
| Navegación multinivel | Ineficiente (todo son `:RELACIONADO_CON`) | Eficiente (tipos de relación filtran traversal) |
| Modelado de destinos | Nodo intermedio `Ruta` (tabla puente) | Nodo semántico `Destino` con relación directa |
| Consultas sociales | Simples (una relación genérica) | Complejas (amigos de amigos, coincidencias) |

### 3.5.7. Principios NoSQL Aplicados

| Principio | Aplicación |
|---|---|
| Relaciones como ciudadanos de primera clase | `:AMIGO_DE`, `:VIAJA_A` con propiedades propias |
| Dirección semántica | La dirección de la relación tiene significado de negocio |
| Modelado natural del dominio | Los usuarios viajan a destinos (relación directa) |
| Traversal como operación fundamental | Consultas de amigos de amigos aprovechan punteros físicos |
| Propiedades en relaciones | Contexto de viaje almacenado en la relación, no en nodos intermedios |

---

## 3.6. Resumen de Correcciones

| Sistema | Error Generado por IA | Antipatrón Detectado | Corrección Aplicada | Beneficio Arquitectónico |
|---|---|---|---|---|
| **MongoDB** | Colecciones separadas `vehiculos` y `reparaciones` con relación por `vehiculo_id` | Normalización Encubierta | Incrustación del array `reparaciones` dentro del documento `vehiculos` | Reducción del 50% en consultas, atomicidad, localidad de datos |
| **Cassandra** | `PRIMARY KEY (tipo_vehiculo, timestamp)` con solo 3 valores posibles de partition key | Partition Key de baja cardinalidad (Hotspot) | `PRIMARY KEY (vehicle_id, timestamp)` con `CLUSTERING ORDER BY (timestamp DESC)` | Distribución uniforme entre nodos, escalabilidad lineal, sin ALLOW FILTERING |
| **Redis** | Strings JSON con `SET`/`GET` para todo, sin TTL, sin jerarquía de claves | Redis como almacén de texto plano | `HSET`/`HINCRBY` para objetos, `EXPIRE` para sesiones, claves `:` jerárquicas | 40x menos tráfico de red, atomicidad, autogestión de memoria |
| **Neo4j** | Relaciones genéricas `:RELACIONADO_CON` y `:TIENE`, rutas como tabla puente | Nodos-Tabla y relaciones sin semántica | Relaciones `:AMIGO_DE`, `:VIAJA_A`, `:RESIDE_EN` con propiedades y dirección | Navegación multinivel eficiente, consultas sociales complejas, modelado natural |

---

## 3.7. Conclusión del Análisis de Auditoría

La bitácora de auditoría presentada en este apartado demuestra que la generación de código mediante inteligencia artificial, si bien es una herramienta productiva para obtener esqueletos de código funcional, no puede ser incorporada a un sistema productivo sin un proceso riguroso de revisión arquitectónica. Los cuatro casos analizados en EcoDrive revelan un patrón consistente: la IA tiende a reproducir modelos mentales relacionales incluso cuando se le solicita explícitamente código para bases de datos NoSQL.

**La importancia de auditar código generado por IA** radica en que los errores detectados no son errores sintácticos — el código funciona y devuelve resultados — sino errores semánticos de diseño que comprometen la escalabilidad, el rendimiento y la mantenibilidad del sistema a medio y largo plazo. El hotspot en Cassandra provocado por una Partition Key de baja cardinalidad no se manifiesta con 100 vehículos, pero se convierte en una caída catastrófica del clúster con 10.000. La ausencia de TTL en Redis no es problemática en un piloto de 1 hora, pero agota la memoria RAM en un despliegue de producción de 24 horas.

**NoSQL exige un cambio de mentalidad fundamental** que la IA todavía no ha internalizado. Este cambio tiene tres pilares:

1. **Pensar en agregados:** En lugar de normalizar como haríamos en SQL, debemos agrupar en una misma unidad de almacenamiento todo lo que se consulta y modifica conjuntamente. Este principio se aplicó en la corrección de MongoDB (vehículo + reparaciones como un solo documento) y es la base del diseño en bases de datos documentales.

2. **Diseñar según las consultas (Query-First Design):** El diseño del esquema no puede hacerse aisladamente del conocimiento de los patrones de acceso. En Cassandra, la elección de la Partition Key depende exclusivamente de cómo vamos a consultar los datos. En el error generado por la IA, se diseñó la tabla primero y luego se forzó la consulta con `ALLOW FILTERING`. En la corrección, se partió de las consultas objetivo para diseñar la clave primaria.

3. **Aprovechar las estructuras de datos nativas:** Cada base de datos NoSQL ofrece estructuras de datos optimizadas para casos de uso específicos. Redis dispone de HASH, SET, ZSET, LIST, HyperLogLog, etc. Usar solo Strings para todo es como tener un coche y usar solo la primera marcha. Neo4j ofrece relaciones con dirección, tipo y propiedades; ignorar estas capacidades reduce el grafo a un conjunto de tablas desconectadas.

**La persistencia políglota** ha demostrado ser el enfoque arquitectónico correcto para EcoDrive. Cada subsistema tiene requisitos radicalmente distintos, y cada motor NoSQL aporta su fortaleza específica:
- MongoDB proporciona la flexibilidad de esquema que necesita un catálogo con tipos de vehículo heterogéneos.
- Cassandra proporciona la escalabilidad de escritura que necesita un sistema IoT con millones de lecturas diarias.
- Redis proporciona la latencia de microsegundos y la autogestión de datos efímeros que necesita un sistema de sesiones en tiempo real.
- Neo4j proporciona la navegabilidad por relaciones que necesita un sistema de recomendación social.

**La escalabilidad de EcoDrive** depende directamente de la corrección de estos errores de diseño. Un esquema mal diseñado en Cassandra no escala horizontalmente por más nodos que se añadan al clúster — todos los datos seguirán concentrados en una única partición. Un modelo de Redis sin TTL colapsa la memoria RAM cuando el número de usuarios crece. Una auditoría de código generado por IA no es, por tanto, un ejercicio académico: es una necesidad operativa para garantizar que el sistema puede crecer de forma sostenible.

Este análisis ha cubierto los criterios CE.a (características de los sistemas NoSQL) y CE.c (elementos utilizados: agregados, claves, nodos, tipos de datos) mediante la identificación, corrección y justificación técnica de cuatro antipatrones reales generados por inteligencia artificial en el contexto del proyecto EcoDrive.
