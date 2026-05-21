# Guía de Estudio — MongoDB + mongosh (Práctica EcoDrive)

---

## 1. TEORÍA: Preguntas frecuentes en la defensa

### ¿Por qué MongoDB y no otra base de datos para Telemetría?

| Base de Datos | Motivo de descarte |
|---|---|
| **Cassandra** (Columnar) | Ideal para telemetría, pero **no lo dimos en clase** |
| **Redis** (Clave-Valor) | Pensado para **caché/sesiones**, no para históricos masivos con consultas por rango de tiempo. No tiene índices secundarios complejos |
| **Neo4j** (Grafos) | Orientado a **relaciones** (amigos, rutas), no a series temporales de sensores |
| **MongoDB** (Documental) | ✅ **Elegido**: esquema flexible, índices compuestos, escrituras rápidas sin bloqueos |

### ¿Qué es una base de datos Documental?

Almacena datos en **documentos JSON** (BSON realmente). Cada documento puede tener estructura diferente (esquema flexible). Una **colección** es un grupo de documentos.

### ¿Qué son los Agregados (Embedding)?

Es **incrustar** datos relacionados dentro del mismo documento en lugar de separarlos en colecciones distintas con joins.

**Ejemplo de la práctica:**

```javascript
// ✅ BIEN (Agregado) - datos del vehículo dentro del documento de telemetría
{
  vehicle_id: "VH-001",
  vehicle_type: "patinete",   // <-- incrustado
  timestamp: ISODate("..."),
  speed: 22.0,
  battery: 72
}

// ❌ MAL (Normalización encubierta) - colecciones separadas con join
// db.vehiculos y db.telemetria relacionadas por vehicle_id
```

**¿Cuándo incrustar?** Cuando los datos **siempre se leen juntos**.
**¿Cuándo referenciar?** Cuando el dato hijo crece sin parar (millones de registros).

### En MongoDB no existe "Partition Key" como Cassandra, ¿qué usamos en su lugar?

Usamos un **índice compuesto** que cumple función similar:

```javascript
db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })
```

- `vehicle_id` (campo de alta cardinalidad): agrupa datos del mismo vehículo
- `timestamp` en orden descendente: lecturas más recientes primero

### ¿Qué es Query-First Design?

Diseñar primero **la consulta que voy a hacer** y luego crear la estructura para responderla eficientemente.

**Consulta objetivo:** "Dame el historial completo de telemetría del vehículo VH-001 ordenado por tiempo"
**Estructura:** Índice compuesto `{ vehicle_id: 1, timestamp: -1 }`

---

## 2. COMANDOS ESENCIALES DE mongosh

### Conexión y bases de datos

```javascript
// Conectar (dentro del contenedor Docker)
docker exec -it mongodb-telemetria mongosh

// Ver todas las bases de datos
show dbs

// Usar / crear una base de datos
use ecodrive

// Ver colecciones
show collections
```

### Creación de índices

```javascript
// Índice simple
db.telemetria.createIndex({ vehicle_id: 1 })

// Índice compuesto (el que usamos en la práctica)
db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })

// Ver índices de una colección
db.telemetria.getIndexes()

// Explicar plan de consulta (ver si usa el índice)
db.telemetria.find({ vehicle_id: "VH-001" }).explain("executionStats")
```

### Inserción de documentos

```javascript
// Insertar un solo documento
db.telemetria.insertOne({
  vehicle_id: "VH-001",
  vehicle_type: "patinete",
  timestamp: new ISODate("2025-06-01T08:00:00Z"),
  location: { lat: 40.4168, lng: -3.7038 },
  speed: 0,
  battery: 100
})

// Insertar varios documentos (insertMany)
db.telemetria.insertMany([
  { vehicle_id: "VH-001", vehicle_type: "patinete", timestamp: new ISODate("2025-06-01T08:00:00Z"), location: { lat: 40.4168, lng: -3.7038 }, speed: 0, battery: 100 },
  { vehicle_id: "VH-001", vehicle_type: "patinete", timestamp: new ISODate("2025-06-01T09:00:00Z"), location: { lat: 40.4175, lng: -3.7030 }, speed: 18.5, battery: 87 },
  { vehicle_id: "VH-002", vehicle_type: "bicicleta",  timestamp: new ISODate("2025-06-01T10:00:00Z"), location: { lat: 40.4182, lng: -3.7025 }, speed: 22.0, battery: 72 }
])
```

### Consultas (el profesor pedirá variaciones)

```javascript
// Todas las lecturas de un vehículo
db.telemetria.find({ vehicle_id: "VH-001" })

// Con ordenación
db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })
// 1 = ascendente, -1 = descendente

// Contar documentos
db.telemetria.countDocuments({ vehicle_id: "VH-001" })

// Filtrar por rango de tiempo
db.telemetria.find({
  vehicle_id: "VH-001",
  timestamp: {
    $gte: ISODate("2025-06-01T09:00:00Z"),
    $lte: ISODate("2025-06-01T11:00:00Z")
  }
})

// Filtrar por batería baja (anomalías)
db.telemetria.find({ vehicle_id: "VH-001", battery: { $lt: 50 } })

// Filtrar por velocidad > 0 (vehículo en movimiento)
db.telemetria.find({ vehicle_id: "VH-001", speed: { $gt: 0 } })

// Proyectar solo ciertos campos
db.telemetria.find(
  { vehicle_id: "VH-001" },
  { timestamp: 1, speed: 1, battery: 1, _id: 0 }
)

// Limitar resultados
db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: -1 }).limit(3)

// Última lectura de cada vehículo (con aggregate)
db.telemetria.aggregate([
  { $sort: { timestamp: -1 } },
  { $group: { _id: "$vehicle_id", ultima_lectura: { $first: "$$ROOT" } } }
])
```

### Actualizaciones

```javascript
// Actualizar un campo específico
db.telemetria.updateOne(
  { vehicle_id: "VH-001", timestamp: ISODate("2025-06-01T08:00:00Z") },
  { $set: { battery: 95 } }
)

// Incrementar/decrementar un valor
db.telemetria.updateOne(
  { vehicle_id: "VH-001", timestamp: ISODate("2025-06-01T08:00:00Z") },
  { $inc: { battery: -5 } }  // decrementa 5
)
```

### Borrado

```javascript
// Borrar un documento
db.telemetria.deleteOne({ vehicle_id: "VH-001", timestamp: ISODate("2025-06-01T08:00:00Z") })

// Borrar todos los de un vehículo
db.telemetria.deleteMany({ vehicle_id: "VH-001" })

// Borrar toda la colección
db.telemetria.drop()
```

---

## 3. COMANDOS ÚTILES PARA EL EXAMEN (inspección + utilidades)

### Equivalente a `DESCRIBE` de MySQL

En MySQL: `DESCRIBE vehiculos;` → muestra columnas, tipos, restricciones.

En MongoDB **no hay esquema fijo**, pero estos comandos te muestran la estructura real de los documentos:

```javascript
// 🥇 EQUIVALENTE DIRECTO: ver 1 documento con campos y valores
db.telemetria.findOne()

// Solo nombres de campos (como DESCRIBE pero sin tipos)
Object.keys(db.telemetria.findOne())

// Si hay documentos con distinta estructura, lista TODOS los campos únicos
db.telemetria.aggregate([
  { $project: { campos: { $objectToArray: "$$ROOT" } } },
  { $unwind: "$campos" },
  { $group: { _id: "$campos.k" } },
  { $sort: { _id: 1 } }
])
```

| MySQL | MongoDB |
|---|---|
| `DESCRIBE tabla` | `db.col.findOne()` + `Object.keys()` |
| `SHOW TABLES` | `show collections` |
| `SHOW DATABASES` | `show dbs` |
| `SELECT * FROM tabla` | `db.col.find()` |

### Información de colecciones y bases de datos

```javascript
// Estadísticas de la colección (cantidad docs, tamaño, índices)
db.telemetria.stats()

// Ver tamaño de la colección en bytes
db.telemetria.totalSize()

// Ver todos los índices y su tamaño
db.telemetria.getIndexes()

// Validar integridad de la colección
db.telemetria.validate()

// Listar bases de datos
show dbs

// Ver base de datos actual
db.getName()

// Ayuda rápida integrada
db.help()
db.telemetria.help()
```

### Fechas y tipos de datos

```javascript
// Crear fechas (mongoose/new Date vs ISODate)
new ISODate("2025-06-01T08:00:00Z")  // recomendado
new Date("2025-06-01T08:00:00Z")     // equivalente

// Fecha actual
new ISODate()

// Consultar por tipo de campo ($type)
// battery debe ser número (double)
db.telemetria.find({ battery: { $type: "double" } })

// battery debe ser entero (int)
db.telemetria.find({ battery: { $type: "int" } })

// Tipos comunes: "string", "double", "int", "bool", "date", "object", "array"

// $exists: documentos que tengan o no un campo
db.telemetria.find({ combustible: { $exists: true } })  // solo coches
db.telemetria.find({ battery: { $exists: false } })     // docs sin batería
```

### Operadores de comparación ($eq, $ne, $in, $nin)

```javascript
// Igual a
db.telemetria.find({ vehicle_type: "patinete" })

// No igual a
db.telemetria.find({ vehicle_type: { $ne: "coche" } })

// Está en un conjunto
db.telemetria.find({ vehicle_id: { $in: ["VH-001", "VH-002"] } })

// No está en un conjunto
db.telemetria.find({ vehicle_id: { $nin: ["VH-001"] } })
```

### Operadores lógicos ($and, $or, $not)

```javascript
// AND implícito (varios campos en el mismo filtro)
db.telemetria.find({ vehicle_id: "VH-001", battery: { $lt: 50 } })

// AND explícito
db.telemetria.find({ $and: [
  { vehicle_id: "VH-001" },
  { battery: { $lt: 50 } }
]})

// OR
db.telemetria.find({ $or: [
  { vehicle_type: "patinete" },
  { battery: { $gt: 90 } }
]})
```

### Distinct (valores únicos)

```javascript
// Tipos de vehículos distintos
db.telemetria.distinct("vehicle_type")
// Resultado: ["patinete", "bicicleta", "coche"]

// IDs de vehículos distintos
db.telemetria.distinct("vehicle_id")
```

### Aggregate (tuberías útiles para examén)

```javascript
// Promedio de batería por vehículo
db.telemetria.aggregate([
  { $group: { _id: "$vehicle_id", bateria_media: { $avg: "$battery" } } }
])

// Máxima, mínima y media por vehículo
db.telemetria.aggregate([
  { $group: {
    _id: "$vehicle_id",
    max_bateria: { $max: "$battery" },
    min_bateria: { $min: "$battery" },
    media: { $avg: "$battery" },
    total_lecturas: { $sum: 1 }
  }}
])

// Vehículos con batería crítica (última lectura < 20)
db.telemetria.aggregate([
  { $sort: { timestamp: -1 } },
  { $group: { _id: "$vehicle_id", ultima_bateria: { $first: "$battery" } } },
  { $match: { ultima_bateria: { $lt: 20 } } }
])

// Contar cuántas lecturas tiene cada vehículo
db.telemetria.aggregate([
  { $group: { _id: "$vehicle_id", lecturas: { $sum: 1 } } },
  { $sort: { lecturas: -1 } }
])
```

### Crear colecciones con validación de esquema

```javascript
// Crear colección con validación (opcional, para examen)
db.createCollection("telemetria", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["vehicle_id", "timestamp", "speed", "battery"],
      properties: {
        vehicle_id: { bsonType: "string", description: "obligatorio" },
        timestamp: { bsonType: "date", description: "obligatorio" },
        speed: { bsonType: "double", minimum: 0 },
        battery: { bsonType: "int", minimum: 0, maximum: 100 }
      }
    }
  }
})
```

### Borrar colección / base de datos

```javascript
// Borrar colección
db.telemetria.drop()

// Borrar base de datos entera
db.dropDatabase()
```

---

## 4. POSIBLES MODIFICACIONES QUE PIDAN EN EL EXAMEN

### "Añade un nuevo vehículo con más campos"

```javascript
db.telemetria.insertOne({
  vehicle_id: "CO-001",
  vehicle_type: "coche",
  timestamp: new ISODate("2025-06-01T14:00:00Z"),
  location: { lat: 40.4200, lng: -3.7000 },
  speed: 45.0,
  battery: 92,
  combustible: "eléctrico",     // <-- campo nuevo, solo en coches
  matricula: "1234ABC"          // <-- campo nuevo, solo en coches
})
```

### "Cambia la consulta para que muestre solo los coches"

```javascript
db.telemetria.find({ vehicle_type: "coche" })
// o filtrar por campo que solo exista en coches:
db.telemetria.find({ combustible: { $exists: true } })
```

### "Agrupa por vehículo y calcula el promedio de batería"

```javascript
db.telemetria.aggregate([
  { $group: {
    _id: "$vehicle_id",
    promedio_bateria: { $avg: "$battery" },
    lecturas: { $sum: 1 }
  }}
])
```

### "Borra todos los datos y vuelve a insertar otros"

```javascript
db.telemetria.deleteMany({})
db.telemetria.insertMany([ /* nuevos datos */ ])
```

### "¿Qué pasa si insertas un documento sin campo battery?"

```javascript
db.telemetria.insertOne({
  vehicle_id: "VH-003",
  vehicle_type: "patinete",
  timestamp: new ISODate("2025-06-01T15:00:00Z"),
  location: { lat: 40.4210, lng: -3.6990 },
  speed: 12.0
  // sin battery
})
// ✅ MongoDB lo acepta sin problemas (esquema flexible)
```

### "Explica qué hace el índice compuesto"

El índice `{ vehicle_id: 1, timestamp: -1 }` almacena los documentos ordenados primero por `vehicle_id` y dentro de cada vehículo por `timestamp` descendente. Cuando haces:

```javascript
db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })
```

MongoDB localiza todos los documentos con `vehicle_id = "VH-001"` en el índice y los devuelve ya ordenados, **sin tener que ordenar en memoria**. Sin el índice, MongoDB haría un "collection scan" (leer toda la colección) y luego ordenar en RAM, lo que es lentísimo con millones de registros.

---

## 4. COMANDOS RÁPIDOS PARA DOCKER

```bash
# Iniciar MongoDB
docker run -d --name mongodb-telemetria -p 27017:27017 mongo:7

# Entrar a mongosh
docker exec -it mongodb-telemetria mongosh

# Ver logs
docker logs mongodb-telemetria

# Parar y borrar contenedor
docker stop mongodb-telemetria
docker rm mongodb-telemetria

# Mongo Express (interfaz web)
docker run -d --name mongo-express -p 8081:8081 --link mongodb-telemetria:mongo mongo-express
# Abrir en navegador: http://localhost:8081
```

---

## 5. CHECKLIST RÁPIDO PARA LA PRÁCTICA

- [ ] `docker run -d --name mongodb-telemetria -p 27017:27017 mongo:7`
- [ ] `docker exec -it mongodb-telemetria mongosh`
- [ ] `use ecodrive`
- [ ] `db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })`
- [ ] Insertar 5 documentos con `insertMany`
- [ ] `db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })`
- [ ] Capturar pantallas de cada paso
