-- ==========================================
-- EJERCICIO 3: INTEGRIDAD DE PLANTILLA
-- ==========================================
-- Objetivo: Corregir empleados huérfanos y añadir FOREIGN KEY
-- Tags: FOREIGN KEY, HUÉRFANOS, INTEGRIDAD REFERENCIAL
-- ==========================================

USE logistica_global;

-- Configuraciones de seguridad para MySQL
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

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

-- Restaurar configuraciones
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;