# Memoria Técnica - Servicio B: Telemetría y Sensores IoT (MongoDB)

---

## 1. Justificación Arquitectónica (CE.a, CE.b, CE.c)

### SGBD Elegido: **MongoDB** (Base de Datos Documental)

**Justificación:**
Se ha seleccionado MongoDB porque permite almacenar documentos JSON flexibles con un esquema dinámico, lo que lo hace ideal para registrar pings de telemetría con estructuras de datos heterogéneas.
Este servicio requiere almacenar millones de registros diarios de ubicación, velocidad y batería emitidos cada 5 segundos por cada vehículo, así como consultar el historial completo de un vehículo concreto para detectar anomalías en la batería. Además, gracias al uso de índices compuestos sobre `vehicle_id` y `timestamp`, es que las consultas por rango temporal se resuelven sin necesidad de ordenación en memoria.

**Elementos de diseño en MongoDB:**

- **Colección:** `telemetria`
- **Documento individual** (cada ping de 5s):

```json
{
  "_id": ObjectId,
  "vehicle_id": "VH-001",
  "timestamp": ISODate,
  "location": { "lat": 40.4168, "lng": -3.7038 },
  "speed": 25.5,
  "battery": 85
}
```

- **Índice compuesto** (equivalente a la Partition Key + Clustering Column de Cassandra):
  ```javascript
  db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })
  ```
  - `vehicle_id` como **shard key lógica**: agrupa físicamente todos los datos del mismo vehículo.
  - `timestamp` en orden descendente: las lecturas más recientes primero.

---

## 2. Prompts de Generación de Datos (IA)

### Prompt utilizado con la IA:

> "Genera un script de MongoDB para insertar 5 documentos de telemetría en una colección llamada 'telemetria'. Los documentos deben corresponder al vehículo con ID 'VH-001' en distintas horas del mismo día. Cada documento debe contener: vehicle_id, timestamp (en formato ISODate), location (con lat y lng), speed (número decimal) y battery (número entero 0-100). Los timestamps deben espaciarse al menos 1 hora entre sí. Los valores de batería deben decrecer con el tiempo para simular consumo real."

---

## 3. Análisis de Auditoría (CE.a, CE.c)

Se documentan **dos correcciones técnicas** realizadas sobre la propuesta original de la IA:

### Corrección 1: Normalización Encubierta → Agregados

**Problema detectado:**
La IA propuso originalmente dos colecciones separadas: `vehiculos` y `telemetria`, relacionándolas mediante `vehicle_id` como clave foránea, sugiriendo un `$lookup` (join) para obtener los datos juntos.

```javascript
// MAL (propuesta original de la IA)
db.telemetria.aggregate([
  { $lookup: { from: "vehiculos", localField: "vehicle_id", foreignField: "_id", as: "vehiculo" } }
])
```

**Corrección aplicada:**
Se eliminó la colección `vehiculos` y se incrustaron los datos relevantes del vehículo directamente en cada documento de telemetría. Los datos de telemetría y vehículo **siempre se leen juntos** en la consulta de historial, por lo que deben estar en el mismo documento (principio de Agregados en MongoDB).

```javascript
// BIEN (corregido)
{
  "vehicle_id": "VH-001",
  "vehicle_type": "patinete",
  "timestamp": ISODate("2025-06-01T10:00:00Z"),
  "location": { "lat": 40.4168, "lng": -3.7038 },
  "speed": 25.5,
  "battery": 85
}
```

### Corrección 2: Índice Ineficiente → Índice Compuesto

**Problema detectado:**
La IA propuso un índice solo sobre `vehicle_id`:

```javascript
// MAL (propuesta original de la IA)
db.telemetria.createIndex({ vehicle_id: 1 })
```

Esto permite filtrar por vehículo, pero no ordena los resultados temporalmente. Para obtener el historial ordenado, MongoDB tendría que hacer una ordenación en memoria (posible desbordamiento con 32MB de límite).

**Corrección aplicada:**
Se añadió `timestamp` como segundo campo del índice compuesto. Esto permite que MongoDB devuelva los resultados directamente ordenados desde el índice, sin necesidad de ordenación en memoria.

```javascript
// BIEN (corregido)
db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })
```

---

## 4. Scripts de Carga y Consultas (CE.d)

### 4.1 Creación del índice

```javascript
use ecodrive
db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })
```

### 4.2 Inserción de 5 registros de telemetría

```javascript
db.telemetria.insertMany([
  {
    vehicle_id: "VH-001",
    vehicle_type: "patinete",
    timestamp: new ISODate("2025-06-01T08:00:00Z"),
    location: { lat: 40.4168, lng: -3.7038 },
    speed: 0,
    battery: 100
  },
  {
    vehicle_id: "VH-001",
    vehicle_type: "patinete",
    timestamp: new ISODate("2025-06-01T09:00:00Z"),
    location: { lat: 40.4175, lng: -3.7030 },
    speed: 18.5,
    battery: 87
  },
  {
    vehicle_id: "VH-001",
    vehicle_type: "patinete",
    timestamp: new ISODate("2025-06-01T10:00:00Z"),
    location: { lat: 40.4182, lng: -3.7025 },
    speed: 22.0,
    battery: 72
  },
  {
    vehicle_id: "VH-001",
    vehicle_type: "patinete",
    timestamp: new ISODate("2025-06-01T11:00:00Z"),
    location: { lat: 40.4190, lng: -3.7020 },
    speed: 15.3,
    battery: 58
  },
  {
    vehicle_id: "VH-001",
    vehicle_type: "patinete",
    timestamp: new ISODate("2025-06-01T12:00:00Z"),
    location: { lat: 40.4198, lng: -3.7015 },
    speed: 0,
    battery: 45
  }
])
```

### 4.3 Consulta: Historial completo de un vehículo específico

```javascript
db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })
```

**Explicación:** El índice `{ vehicle_id: 1, timestamp: -1 }` cubre completamente esta consulta. MongoDB usa el índice para:
1. Localizar todos los documentos con `vehicle_id = "VH-001"` (primera parte del índice).
2. Ordenarlos por `timestamp` (segunda parte del índice) sin necesidad de ordenación en memoria.

---

## 5. Ejecución y Visualización (CE.e)

Para demostrar la correcta ejecución, se deben capturar las siguientes pantallas:

### Captura 1: Creación del índice
- Comando: `db.telemetria.createIndex({ vehicle_id: 1, timestamp: -1 })`
- Debe mostrarse el resultado: `{ "createdCollectionAutomatically": true, "numIndexesBefore": 1, "numIndexesAfter": 2 }`

### Captura 2: Inserción de datos
- Comando: `db.telemetria.insertMany([...])`
- Debe mostrarse el resultado con los 5 ObjectId generados.

### Captura 3: Consulta de historial
- Comando: `db.telemetria.find({ vehicle_id: "VH-001" }).sort({ timestamp: 1 })`
- Debe mostrarse el resultado con los 5 documentos ordenados por timestamp ascendente.

**Herramientas recomendadas:**
- Consola `mongosh`
- **Mongo Express** (interfaz web): `http://localhost:8081`
- **DataGrip** con conector MongoDB
