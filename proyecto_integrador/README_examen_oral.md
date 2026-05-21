# Examen Oral — Fundamentos Teóricos NoSQL (30 min)

---

## 🔴 REDIS (Clave-Valor)

### 4. ¿Por qué Redis para alta concurrencia y baja latencia?

Redis guarda todo **en RAM**, no en disco. Sus estructuras nativas (HASH, List, Sorted Set, String) ejecutan operaciones completas **en un solo comando atómico**: incrementar, encolar, rankear. Sin transacciones ni locks. Por eso es el rey de **cachés, sesiones, colas y rate-limiting**.

### 5. Diferencia Redis vs MySQL

| | Redis | MySQL |
|---|---|---|
| **Dónde guarda** | RAM | Disco |
| **Velocidad** | Microsegundos | Milisegundos |
| **Modelo** | Clave-Valor | Tablas + SQL |
| **Cómo buscas** | Por clave, directo | Joins, subconsultas |
| **Para qué sirve** | Caché, sesiones, tiempo real | Datos transaccionales, históricos |

---

## 🟢 MONGODB (Documental)

### 4. ¿Por qué Documental frente a MySQL para Catálogos?

MongoDB guarda **documentos JSON con esquema dinámico**. Cada vehículo puede tener campos distintos en la misma colección: patinete con `peso_maximo`, bici con `marchas`, coche con `combustible`. Sin migraciones, sin NULLs, sin tablas separadas.

### 5. Diferencia aggregate en MongoDB vs SQL

El `aggregate` es un **pipeline de etapas** (`$match` → `$group` → `$sort`) que puedes reordenar según necesites. SQL tiene estructura fija (`SELECT-FROM-WHERE-GROUP BY`). En MongoDB los datos suelen ir incrustados en un solo documento, así que casi nunca necesitas `$lookup`. En SQL los JOINs son obligatorios porque los datos están normalizados en tablas separadas.

**Etapas del pipeline:**

| Etapa | Qué hace | Ejemplo |
|---|---|---|
| `$match` | Filtra documentos (como WHERE) | `{ $match: { vehicle_id: "VH-001" } }` |
| `$group` | Agrupa y acumula (como GROUP BY) | `{ $group: { _id: "$vehicle_id", media: { $avg: "$battery" } } }` |
| `$sort` | Ordena resultados (como ORDER BY) | `{ $sort: { timestamp: -1 } }` |
| `$lookup` | Join con otra colección | `{ $lookup: { from: "vehiculos", localField: "vehicle_id", foreignField: "_id", as: "info" } }` |

```javascript
// Ejemplo completo: vehículos con batería baja, ordenados
db.telemetria.aggregate([
  { $match: { battery: { $lt: 50 } } },
  { $group: { _id: "$vehicle_id", lecturas: { $sum: 1 } } },
  { $sort: { lecturas: -1 } }
])
```

---

## 🔵 NEO4J (Grafos)

### 4. ¿Por qué grafos para rutas y patrones complejos?

Neo4j modela **Nodos** (usuarios, destinos) y **Relaciones** (VIAJA_A, ES_AMIGO_DE) con dirección y propiedades. Para consultas como "amigos de amigos que viajan al mismo destino", Neo4j **recorre el grafo** paso a paso. SQL necesitaría múltiples JOINs que crecen exponencialmente.

```
(u1)-[:ES_AMIGO_DE]->(u2)-[:VIAJA_A]->(Madrid)
(u1)-[:VIAJA_A]->(Madrid)
→ u1 y u2 son amigos y viajan al mismo destino
```

### 5. Similitud con SQL en atributos de Relaciones

En ambos puedes poner datos en la relación: en Neo4j → `[:VIAJA_A {fecha, distancia}]`, en SQL → columnas en la tabla `VIAJA`. La diferencia: en Neo4j la relación se **recorre directamente** (sigue la flecha). En SQL necesitas **JOINs** para navegar de una tabla a otra.
