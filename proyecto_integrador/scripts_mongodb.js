// ============================================================
// Scripts MongoDB para EcoDrive - Entregable 4
// Pegar en mongosh dentro de la BD ecoruta
// ============================================================

// --- 1. CREAR BASE DE DATOS ---
// use ecoruta

// --- 2. INSERTAR VEHÍCULOS ---

db.vehiculos.insertOne({
  matricula: "PAT-001",
  tipo: "patinete",
  marca: "Xiaomi",
  modelo: "Pro 3",
  año_fabricacion: 2024,
  peso_maximo_kg: 120,
  autonomia_km: 45,
  estado: "disponible",
  reparaciones: [
    { fecha: ISODate("2025-01-15"), tipo: "mantenimiento", coste: 45, taller: "MovilFix" },
    { fecha: ISODate("2025-03-22"), tipo: "reparacion", coste: 120, taller: "MovilFix" }
  ]
})

db.vehiculos.insertOne({
  matricula: "BIC-002",
  tipo: "bicicleta",
  marca: "Orbea",
  modelo: "Wild FS",
  año_fabricacion: 2023,
  marchas: 12,
  material_cuadro: "carbono",
  peso_kg: 19,
  estado: "disponible",
  reparaciones: [
    { fecha: ISODate("2025-02-10"), tipo: "revision", coste: 30, taller: "BiciTaller" }
  ]
})

db.vehiculos.insertOne({
  matricula: "COC-003",
  tipo: "coche",
  marca: "Renault",
  modelo: "Zoe",
  año_fabricacion: 2024,
  tipo_combustible: "electrico",
  plazas: 5,
  autonomia_km: 395,
  estado: "mantenimiento",
  reparaciones: [
    { fecha: ISODate("2025-04-01"), tipo: "reparacion", coste: 340, taller: "AutoTaller" }
  ]
})

// --- 3. CONSULTAS ---

// Consulta 1: Mostrar todos los vehículos
db.vehiculos.find().pretty()

// Consulta 2: Filtrar por campo exclusivo de coches (tipo_combustible)
db.vehiculos.find({ tipo_combustible: { $exists: true } }).pretty()

// Consulta 3: Vehículos en mantenimiento
db.vehiculos.find({ estado: "mantenimiento" }).pretty()

// Consulta 4: Vehículos con reparaciones de más de 100€
db.vehiculos.find({ "reparaciones.coste": { $gt: 100 } }).pretty()
