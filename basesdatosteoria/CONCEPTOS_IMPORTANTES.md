# Guía Completa: Actualización de Bases de Datos (UPDATE y más)

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Seguridad y Modo Seguro](#seguridad-y-modo-seguro)
3. [Integridad Referencial](#integridad-referencial)
4. [Inserciones Avanzadas](#inserciones-avanzadas)
5. [UPDATE y Saneamiento](#update-y-saneamiento)
6. [Manejo de NULLs](#manejo-de-nulls)
7. [Modificación del Esquema](#modificación-del-esquema)
8. [Optimización y Rendimiento](#optimización-y-rendimiento)
9. [Eliminación de Datos](#eliminación-de-datos)

---

## Conceptos Fundamentales

### ¿Qué es una operación UPDATE?
Una operación UPDATE modifica datos existentes en una tabla. Es una operación DML (Data Manipulation Language).

**Estructura básica:**
```sql
UPDATE nombre_tabla
SET columna1 = valor1, columna2 = valor2
WHERE condición;
```

### ¿Por qué es importante aprender esto?
- **Limpieza de datos**: Corregir errores en datos importados
- **Migraciones**: Transformar datos al pasar de un sistema a otro
- **Mantenimiento**: Actualizar información regularmente
- **Auditoría**: Registrar cambios críticos en los datos

---

## Seguridad y Modo Seguro

### El Error 1175: El Guardaespaldas de MySQL

**¿Qué pasa?**
MySQL Workbench y otros clientes gráficos tienen activado por defecto `SQL_SAFE_UPDATES = 1`. Esto significa:
- ❌ NO puedes hacer UPDATE sin especificar la clave primaria en el WHERE
- ❌ NO puedes hacer DELETE sin especificar la clave primaria en el WHERE

**¿Por qué existe?**
Para evitar que un click accidental borre o modifique TODOS los registros de una tabla.

**Ejemplo del problema:**
```sql
-- ❌ Esto falla en Workbench (Error 1175)
UPDATE clientes SET estado = 'Bloqueado';

-- ✅ Esto funciona (especificamos la PK)
UPDATE clientes SET estado = 'Bloqueado' WHERE id = 5;
```

**Cómo sortearlo:**
```sql
-- Opción 1: Desactivar temporalmente
SET SQL_SAFE_UPDATES = 0;
UPDATE clientes SET estado = 'Bloqueado';
SET SQL_SAFE_UPDATES = 1;

-- Opción 2: Usar PK en el WHERE (siempre recomendado)
UPDATE clientes SET estado = 'Bloqueado' WHERE id IN (1, 2, 3);

-- Opción 3: Usar condiciones en PK
UPDATE clientes SET estado = 'Bloqueado' WHERE id > 10;
```

### 💡 Consejo
En producción, **SIEMPRE** mantén `SQL_SAFE_UPDATES = 1`. Protege también con:
- Backups regulares
- Transacciones (BEGIN, ROLLBACK)
- Pruebas en entornos de desarrollo

---

## Integridad Referencial

### Las Claves Foráneas (FK) y sus comportamientos

Una **clave foránea** es una columna que referencia a la columna de clave primaria de otra tabla. Garantiza que los datos sean coherentes.

```sql
CREATE TABLE ventas (
    id INT PRIMARY KEY,
    id_cliente INT,
    monto DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
```

### Comportamientos ante actualizaciones

#### 1️⃣ RESTRICT (Bloqueo)
```sql
ALTER TABLE ventas
ADD CONSTRAINT fk_cliente
FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE RESTRICT;

-- Intenta borrar cliente con id=1 (tiene ventas)
DELETE FROM clientes WHERE id = 1;  -- ❌ ERROR: No se puede, hay ventas
```

**Uso**: Cuando NUNCA debes perder la referencia.

#### 2️⃣ CASCADE (Eliminación en cascada)
```sql
ALTER TABLE ventas
ADD CONSTRAINT fk_cliente
FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE;

-- Borrar cliente con id=1
DELETE FROM clientes WHERE id = 1;  -- ✅ OK, pero también borra sus ventas
SELECT * FROM ventas;  -- Las ventas del cliente 1 desaparecen
```

**⚠️ Peligro**: Pérdida masiva de datos. Usa cuando los datos dependientes no tienen valor sin el padre.

#### 3️⃣ SET NULL (Dejar huérfano)
```sql
ALTER TABLE ventas
ADD CONSTRAINT fk_cliente
FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE SET NULL;

-- Borrar cliente con id=1
DELETE FROM clientes WHERE id = 1;  -- ✅ OK
SELECT * FROM ventas;  -- Las ventas ahora tienen id_cliente = NULL
```

**Uso**: Cuando quieres guardar el historial aunque el cliente desaparezca.

### Desactivar FK temporalmente para migraciones
```sql
SET FOREIGN_KEY_CHECKS = 0;  -- Ignora todas las claves foráneas
-- Ahora puedes insertar, actualizar o vaciar tablas en cualquier orden
TRUNCATE TABLE ventas;
TRUNCATE TABLE clientes;
SET FOREIGN_KEY_CHECKS = 1;  -- Reactivar ✅ OBLIGATORIO
```

---

## Inserciones Avanzadas

### INSERT INTO ... SELECT (Migración de datos)

**Caso real**: Tienes una tabla vieja `clientes_legacy` y quieres migrar a `clientes_nuevo` transformando los datos.

```sql
-- Tabla vieja (desorganizada)
CREATE TABLE clientes_legacy (
    id INT,
    nombre_apellido VARCHAR(200),  -- "Juan Gomez"
    email_contacto VARCHAR(150),
    credito_limite DECIMAL(10,2)
);

-- Tabla nueva (mejor estructura)
CREATE TABLE clientes_nuevo (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    credito_anual DECIMAL(10,2),
    fecha_inscripcion DATETIME
);

-- Migración con transformación
INSERT INTO clientes_nuevo (id, nombre, apellido, email, credito_anual)
SELECT 
    id,
    SUBSTRING_INDEX(nombre_apellido, ' ', 1) as nombre,
    SUBSTRING_INDEX(nombre_apellido, ' ', -1) as apellido,
    LOWER(TRIM(email_contacto)) as email,
    credito_limite * 1.15 as credito_anual
FROM clientes_legacy
WHERE credito_limite > 0;
```

**¿Qué ocurrió?**
1. Dividimos "Juan Gomez" en nombre y apellido
2. Normalizamos emails a minúsculas
3. Aumentamos el crédito 15%
4. Solo migramos clientes con crédito válido

### UPSERT: Insertar o Actualizar

**Caso**: Importas clientes de un proveedor externo. Si existen, actualiza datos; si no, inserta.

```sql
INSERT INTO clientes (id, nombre, email, credito)
VALUES (1, 'Juan Gomez', 'juan@mail.com', 150.00)
ON DUPLICATE KEY UPDATE
    nombre = VALUES(nombre),
    email = VALUES(email),
    credito = credito + VALUES(credito);
```

**Resultado**:
- Si `id = 1` no existe → Se crea nuevo registro
- Si `id = 1` existe → Se actualiza nombre, email y se suma crédito

---

## UPDATE y Saneamiento

### Operaciones básicas de normalización

**Caso**: Importaste datos de Excel y los teléfonos están en formatos diferentes.

```sql
-- Datos iniciales:
-- "+34 600-123-456"
-- "0034 600 123 456"
-- "600123456"

UPDATE clientes
SET telefono = REPLACE(REPLACE(REPLACE(telefono, '+34', ''), '0034', ''), '-', '')
WHERE telefono IS NOT NULL;

-- Después: "600123456" (todos iguales)

-- Luego eliminar espacios
UPDATE clientes
SET telefono = TRIM(telefono);
```

### UPDATE con JOINs: Actualizar basándose en otra tabla

**Caso**: Tienes una tabla de nuevos precios, actualiza el catálogo.

```sql
CREATE TABLE catalogo (
    referencia VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

CREATE TABLE nuevos_precios (
    referencia VARCHAR(50),
    precio_actualizado DECIMAL(10,2)
);

-- Actualizar con JOIN
UPDATE catalogo c
INNER JOIN nuevos_precios n ON c.referencia = n.referencia
SET c.precio = n.precio_actualizado;
```

### UPDATE con subconsultas

**Caso**: Bloquea a todos los clientes con cuentas fraudulentas.

```sql
UPDATE clientes
SET estado = 'BLOQUEADO'
WHERE id IN (
    SELECT id_cliente 
    FROM cuentas_bancarias 
    WHERE fraude = TRUE
);
```

### CASE: Lógica condicional compleja

**Caso**: Según el email, asignar una categoría de cliente.

```sql
UPDATE clientes
SET categoria = CASE
    WHEN email LIKE '%.empresa.com' THEN 'CORPORATIVO'
    WHEN email LIKE '%.edu.%' THEN 'ESTUDIANTE'
    WHEN credito > 5000 THEN 'PREMIUM'
    ELSE 'ESTÁNDAR'
END;
```

**Ventaja**: Una sola pasada por la tabla, no múltiples UPDATEs.

---

## Manejo de NULLs

### El problema del NULL en concatenaciones

```sql
-- ❌ Problema
SELECT CONCAT('Cliente: ', nombre, ' - Teléfono: ', telefono)
FROM clientes;

-- Si telefono = NULL, el resultado es NULL (catastrófico)
-- Resultado: NULL (no "Cliente: Juan - Teléfono: NULL")
```

### Solución 1: IFNULL (binario)

```sql
SELECT CONCAT(
    'Cliente: ', nombre, 
    ' - Teléfono: ', 
    IFNULL(telefono, 'No disponible')
)
FROM clientes;

-- Resultado: "Cliente: Juan - Teléfono: No disponible"
```

### Solución 2: COALESCE (múltiples opciones)

**Caso**: Si no tiene email, usar teléfono; si no tiene teléfono, usar "Sin contacto".

```sql
SELECT 
    nombre,
    COALESCE(email, telefono, 'SIN CONTACTO') as contacto
FROM clientes;

-- Devuelve el primer valor NO NULL
```

### Ejemplo práctico: Saneamiento

```sql
-- Actualizar teléfonos NULL
UPDATE clientes
SET telefono = IFNULL(telefono, '000000000')
WHERE nombre LIKE '%Empresa%';

-- Crear un campo de contacto prioritario
UPDATE clientes
SET contacto_principal = COALESCE(email, telefono, 'CONTACTAR_DIRECTAMENTE')
WHERE activo = 1;
```

---

## Modificación del Esquema

### Agregar columnas

```sql
-- Agregar columna simple
ALTER TABLE clientes ADD COLUMN fecha_registro DATETIME DEFAULT NOW();

-- Agregar en posición específica
ALTER TABLE clientes ADD COLUMN nif VARCHAR(12) AFTER nombre;
```

### Cambiar tipos de datos

```sql
-- Ampliar un VARCHAR
ALTER TABLE clientes MODIFY COLUMN nombre VARCHAR(250);

-- Cambiar tipo o nombre
ALTER TABLE clientes CHANGE COLUMN credito credito_disponible DECIMAL(12,2);
```

### Agregar restricciones

**Problema**: Quieres que los emails sean únicos hacia el futuro.

```sql
ALTER TABLE clientes ADD CONSTRAINT uq_email UNIQUE (email);
```

**Nota**: Si hay duplicados existentes, fallará. Primero limpia:

```sql
-- 1. Identificar duplicados
SELECT email, COUNT(*) as veces
FROM clientes
GROUP BY email
HAVING COUNT(*) > 1;

-- 2. Eliminar o corregir duplicados
DELETE FROM clientes WHERE id NOT IN (
    SELECT MIN(id) FROM clientes GROUP BY email
);

-- 3. Ahora sí, agregar la restricción
ALTER TABLE clientes ADD CONSTRAINT uq_email UNIQUE (email);
```

### Hacer columna obligatoria (NOT NULL)

```sql
-- Primero, sanear los NULLs
UPDATE clientes SET nif = '00000000T' WHERE nif IS NULL;

-- Luego, aplicar la restricción
ALTER TABLE clientes MODIFY COLUMN nif VARCHAR(12) NOT NULL;
```

### Validaciones (CHECK)

```sql
-- Crédito no puede ser negativo
ALTER TABLE clientes 
ADD CONSTRAINT chk_credito_positivo 
CHECK (credito >= 0);

-- Validación compleja: NIF debe tener 8 dígitos + 1 letra
ALTER TABLE clientes
ADD CONSTRAINT chk_nif_formato
CHECK (nif REGEXP '^[0-9]{8}[A-Z]$');
```

---

## Optimización y Rendimiento

### SARGability: El destrozo de los índices

Una columna indexada **pierde su índice** si aplicas funciones sobre ella en el WHERE.

```sql
-- ❌ MAL (Full Table Scan - examina TODAS las filas)
SELECT * FROM clientes 
WHERE UPPER(email) = 'JUAN@MAIL.COM';
-- El índice de email NO se usa porque aplicamos UPPER()

-- ✅ BIEN (Index Seek - encuentra rápido)
SELECT * FROM clientes 
WHERE email = 'juan@mail.com';
-- El índice se usa directamente
```

**Comparación de rendimiento** (tabla con 1 millón de registros):
- ❌ SARGable: ~500ms (examina 1.000.000 filas)
- ✅ SARGable: ~5ms (busca directo en índice)

### Otras prácticas que rompen índices

```sql
-- ❌ Con función - No usa índice
UPDATE clientes SET estado = 'Nuevo' WHERE YEAR(fecha) = 2025;

-- ✅ Sin función - Usa índice
UPDATE clientes SET estado = 'Nuevo' WHERE fecha >= '2025-01-01';

-- ❌ Con operación - No usa índice
UPDATE clientes SET estado = 'Nuevo' WHERE credito / 2 > 100;

-- ✅ Sin operación - Usa índice
UPDATE clientes SET estado = 'Nuevo' WHERE credito > 200;
```

---

## Eliminación de Datos

### DELETE vs TRUNCATE: La batalla eterna

| Característica | DELETE | TRUNCATE |
|---|---|---|
| **Tipo** | DML (fila a fila) | DDL (estructura) |
| **Velocidad** | Lenta (millones) | Instantánea |
| **WHERE** | ✅ Soporta | ❌ No |
| **Triggers** | ✅ Se disparan | ❌ No |
| **FOREIGN KEY** | ✅ Verifica | ❌ Ignora |
| **Log** | ✅ Registra cada fila | ❌ Mínimo |
| **AUTO_INCREMENT** | ✅ Mantiene | ❌ Resetea |

**DELETE:**
```sql
-- Borrar archivos de logs más antiguos de 5 años
DELETE FROM sys_logs
WHERE created_at < DATE_SUB(NOW(), INTERVAL 5 YEAR);

-- Es lento pero seguro: respeta FKs, dispara triggers
```

**TRUNCATE:**
```sql
-- Después de un proceso ETL, vaciar tabla de trabajo
TRUNCATE TABLE import_raw;

-- Es rápido pero peligroso: no verifica integridad
-- ⚠️ AUTO_INCREMENT se resetea a 1
```

### Verificación post-operación (Auditoría)

```sql
-- Después de eliminar duplicados
SELECT email, COUNT(*) as repetidos
FROM clientes
GROUP BY email
HAVING COUNT(*) > 1;
-- Debe devolver 0 filas

-- Verificar distribución después de cambios
SELECT estado, COUNT(*) as total, ROUND(COUNT(*)*100/1000, 2) as porcentaje
FROM clientes
GROUP BY estado;
```

---

## 🎯 Checklist de Buenas Prácticas

- [ ] ✅ Siempre haz un SELECT primero para verificar qué vas a modificar
- [ ] ✅ Usa transacciones: `START TRANSACTION; ... COMMIT; ROLLBACK;`
- [ ] ✅ Especifica el WHERE (evita modificar toda la tabla)
- [ ] ✅ Mantén SQL_SAFE_UPDATES = 1 en producción
- [ ] ✅ Haz backup antes de operaciones masivas
- [ ] ✅ Verifica datos antes y después (con COUNT, GROUP BY)
- [ ] ✅ Usa índices correctamente (sin funciones en WHERE)
- [ ] ✅ Documenta cambios (especialmente en producción)

---

## 📝 Ejemplo Completo: Migración y Limpieza

```sql
-- 1. Crear tabla nueva
CREATE TABLE clientes_limpio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    credito DECIMAL(10,2) DEFAULT 0,
    estado VARCHAR(20) DEFAULT 'ACTIVO',
    fecha_inscripcion DATETIME DEFAULT NOW()
);

-- 2. Empezar transacción
START TRANSACTION;

-- 3. Insertar datos transformados
INSERT INTO clientes_limpio (id, nombre, apellido, email, telefono, credito)
SELECT 
    id,
    TRIM(SUBSTRING_INDEX(nombre_completo, ' ', 1)),
    TRIM(SUBSTRING_INDEX(nombre_completo, ' ', -1)),
    LOWER(TRIM(email_original)),
    IFNULL(TRIM(telefono), NULL),
    CASE 
        WHEN credito < 0 THEN 0
        WHEN credito > 50000 THEN 50000
        ELSE credito
    END
FROM clientes_viejo
WHERE email_original NOT LIKE '%,com';  -- Evita emails rotos

-- 4. Verificar integridad
SELECT COUNT(*) as insertados FROM clientes_limpio;
SELECT COUNT(*) as duplicados FROM clientes_limpio GROUP BY email HAVING COUNT(*) > 1;

-- 5. Si todo está bien
COMMIT;

-- Si hay error
-- ROLLBACK;
```

---

## 📚 Referencias y Conceptos Relacionados

- **ETL** (Extract-Transform-Load): Proceso de migración de datos
- **Data Profiling**: Analizar calidad de datos antes de operaciones
- **Atomicidad**: Transacción completa o ninguna (ACID)
- **Index Seek vs Full Table Scan**: Rendimiento en búsquedas
- **Lógica Tri-valuada**: SQL maneja TRUE, FALSE y NULL

