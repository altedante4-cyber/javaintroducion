-- ==========================================
-- EJERCICIO 5: NORMALIZACIÓN DE GESTIÓN (BONUS)
-- ==========================================
-- Objetivo: Crear tabla de tipos_gestion y normalizar almacenes
-- Tags: NORMALIZACIÓN, FOREIGN KEY, CREATE TABLE
-- ==========================================

USE logistica_global;

-- Configuraciones de seguridad para MySQL
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

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

-- Restaurar configuraciones
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;