-- ==========================================
-- EJERCICIO 2: SANEAMIENTO DE INFRAESTRUCTURA
-- ==========================================
-- Objetivo: Eliminar almacenes duplicados por cod_almacen
-- Tags: DUPLICADOS, DELETE, TEMPORARY TABLE
-- ==========================================

USE logistica_global;

-- Configuraciones de seguridad para MySQL
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

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

-- Restaurar configuraciones
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;