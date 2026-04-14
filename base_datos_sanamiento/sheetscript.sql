-- ==========================================
-- SHEET SCRIPT - EXAMEN RA5
-- Script acumulativo con todos los ejercicios
-- ==========================================

-- ==========================================
-- EJERCICIO 1: GESTIÓN SALARIAL (2 pts)
-- ==========================================
USE logistica_global;

START TRANSACTION;

-- 1. Añadir columna salario_neto de tipo DECIMAL(10,2)
ALTER TABLE empleados ADD COLUMN salario_neto DECIMAL(10,2) AFTER salario_base_sucio;

-- 2. Extraer valor numérico (ignorando la divisa) y aplicar retención del 15% (multiplicar por 0.85)
UPDATE empleados 
SET salario_neto = CAST(REPLACE(REPLACE(salario_base_sucio, 'EUR', ''), ' ', '') AS DECIMAL(10,2)) * 0.85
WHERE salario_base_sucio IS NOT NULL 
AND salario_base_sucio NOT LIKE '%gratis%'
AND salario_base_sucio NOT LIKE '%Gratis%';

-- 3. Rollback y savepoint para aplicar retención del 18%
SAVEPOINT sp_irpf_18;

ROLLBACK TO SAVEPOINT sp_irpf_18;

-- Aplicar retención del 18% (multiplicar por 0.82 - que es 1 - 0.18)
UPDATE empleados 
SET salario_neto = CAST(REPLACE(REPLACE(salario_base_sucio, 'EUR', ''), ' ', '') AS DECIMAL(10,2)) * 0.82
WHERE salario_base_sucio IS NOT NULL 
AND salario_base_sucio NOT LIKE '%gratis%'
AND salario_base_sucio NOT LIKE '%Gratis%';

-- 4. Confirmar los cambios
COMMIT;

-- 5. Asignar valor de 0C (0 €) a empleados con salario erróneo
START TRANSACTION;

UPDATE empleados 
SET salario_neto = 0
WHERE salario_base_sucio IS NOT NULL 
AND (
    salario_base_sucio LIKE '%gratis%'
    OR salario_base_sucio LIKE '%Gratis%'
    OR salario_base_sucio NOT REGEXP '^[0-9]'
    OR CAST(REPLACE(REPLACE(salario_base_sucio, 'EUR', ''), ' ', '') AS DECIMAL(10,2)) < 0
);

COMMIT;


-- ==========================================
-- EJERCICIO 2: SANEAMIENTO DE INFRAESTRUCTURA (2 pts)
-- ==========================================
USE logistica_global;

START TRANSACTION;

-- Eliminación de almacenes duplicados basándose en cod_almacen
-- Conservamos el registro con nombre de sucursal más largo (más caracteres)
-- En caso de empate, conservamos el registro con id más bajo

CREATE TEMPORARY TABLE ids_a_quedar AS
SELECT a.id
FROM almacenes a
WHERE NOT EXISTS (
    SELECT 1 FROM almacenes a2
    WHERE a2.cod_almacen = a.cod_almacen
    AND LENGTH(a2.nombre_sucursal) > LENGTH(a.nombre_sucursal)
)
AND NOT EXISTS (
    SELECT 1 FROM almacenes a2
    WHERE a2.cod_almacen = a.cod_almacen
    AND LENGTH(a2.nombre_sucursal) = LENGTH(a.nombre_sucursal)
    AND a2.id < a.id
);

DELETE FROM almacenes WHERE id NOT IN (SELECT id FROM ids_a_quedar);

DROP TEMPORARY TABLE ids_a_quedar;

COMMIT;


-- ==========================================
-- EJERCICIO 3: INTEGRIDAD DE PLANTILLA (2 pts)
-- ==========================================
USE logistica_global;

START TRANSACTION;

-- 1. Reasignar empleados huérfanos (almacen_id no existe en almacenes) al almacén con id=1
UPDATE empleados 
SET almacen_id = 1 
WHERE almacen_id IS NOT NULL 
AND almacen_id NOT IN (SELECT id FROM almacenes);

-- 2. Definir FOREIGN KEY para evitar que vuelva a ocurrir
-- Primero verificamos si hay valores NULL y los manejamos
ALTER TABLE empleados 
MODIFY COLUMN almacen_id INT NULL;

-- Añadir la restricción de clave foránea
ALTER TABLE empleados 
ADD CONSTRAINT fk_empleados_almacen 
FOREIGN KEY (almacen_id) REFERENCES almacenes(id) 
ON DELETE SET NULL 
ON UPDATE CASCADE;

COMMIT;


-- ==========================================
-- EJERCICIO 4: AUDITORÍA DE RETRASOS (2 pts)
-- ==========================================
USE logistica_global;

START TRANSACTION;

-- 1. Añadir columna dias_retraso de tipo INT
ALTER TABLE envios ADD COLUMN dias_retraso INT AFTER f_entrega_real;

-- 2. Procesar fechas con formato de año de 4 dígitos (interpretación unívoca)
-- Formatos válidos: dd/mm/yyyy, dd-mm-yyyy, yyyy-mm-dd, yyyy/mm/dd
-- No aceptamos: dd/mm/yy, dd-mm-yy, yy-mm-dd, yy/mm/dd

-- Convertir f_llegada_prevista a fecha
UPDATE envios 
SET f_llegada_prevista = DATE(STR_TO_DATE(f_llegada_prevista, '%d/%m/%Y'))
WHERE f_llegada_prevista IS NOT NULL
AND f_llegada_prevista REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$';

UPDATE envios 
SET f_llegada_prevista = DATE(STR_TO_DATE(f_llegada_prevista, '%d-%m-%Y'))
WHERE f_llegada_prevista IS NOT NULL
AND f_llegada_prevista REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$';

UPDATE envios 
SET f_llegada_prevista = DATE(STR_TO_DATE(f_llegada_prevista, '%Y-%m-%d'))
WHERE f_llegada_prevista IS NOT NULL
AND f_llegada_prevista REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

UPDATE envios 
SET f_llegada_prevista = DATE(STR_TO_DATE(f_llegada_prevista, '%Y/%m/%d'))
WHERE f_llegada_prevista IS NOT NULL
AND f_llegada_prevista REGEXP '^[0-9]{4}/[0-9]{2}/[0-9]{2}$';

-- Convertir f_entrega_real a fecha
UPDATE envios 
SET f_entrega_real = DATE(STR_TO_DATE(f_entrega_real, '%d/%m/%Y'))
WHERE f_entrega_real IS NOT NULL
AND f_entrega_real REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$';

UPDATE envios 
SET f_entrega_real = DATE(STR_TO_DATE(f_entrega_real, '%d-%m-%Y'))
WHERE f_entrega_real IS NOT NULL
AND f_entrega_real REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$';

UPDATE envios 
SET f_entrega_real = DATE(STR_TO_DATE(f_entrega_real, '%Y-%m-%d'))
WHERE f_entrega_real IS NOT NULL
AND f_entrega_real REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

UPDATE envios 
SET f_entrega_real = DATE(STR_TO_DATE(f_entrega_real, '%Y/%m/%d'))
WHERE f_entrega_real IS NOT NULL
AND f_entrega_real REGEXP '^[0-9]{4}/[0-9]{2}/[0-9]{2}$';

-- 3. Calcular dias_retraso usando DATEDIFF
-- Si f_llegada_prevista y f_entrega_real son fechas válidas
UPDATE envios 
SET dias_retraso = DATEDIFF(f_entrega_real, f_llegada_prevista)
WHERE f_llegada_prevista IS NOT NULL 
AND f_entrega_real IS NOT NULL
AND f_llegada_prevista != ''
AND f_entrega_real != '';

COMMIT;


-- ==========================================
-- EJERCICIO 5: NORMALIZACIÓN DE GESTIÓN (BONUS 1 pto)
-- ==========================================
USE logistica_global;

START TRANSACTION;

-- 1. Crear nueva tabla tipos_gestion con clave primaria autoincremental y columna nombre
CREATE TABLE tipos_gestion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 2. Trasladar valores únicos de tipo_gestion a la nueva tabla
-- Normalizando: eliminar espacios en blanco y convertir a mayúsculas para evitar duplicados
INSERT INTO tipos_gestion (nombre)
SELECT DISTINCT UPPER(TRIM(tipo_gestion))
FROM almacenes
WHERE tipo_gestion IS NOT NULL AND tipo_gestion != ''
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

-- 3. Modificar tabla almacenes añadiendo columna tipo_gestion_id
ALTER TABLE almacenes ADD COLUMN tipo_gestion_id INT AFTER tipo_gestion;

-- 4. Vincular cada almacén con su tipo correspondiente
UPDATE almacenes a
INNER JOIN tipos_gestion tg ON UPPER(TRIM(a.tipo_gestion)) = tg.nombre
SET a.tipo_gestion_id = tg.id;

-- 5. Eliminar la columna original tipo_gestion
ALTER TABLE almacenes DROP COLUMN tipo_gestion;

-- Añadir FOREIGN KEY
ALTER TABLE almacenes
ADD CONSTRAINT fk_almacenes_tipo_gestion
FOREIGN KEY (tipo_gestion_id) REFERENCES tipos_gestion(id);

COMMIT;