-- ==========================================
-- EJERCICIO 1: GESTIÓN SALARIAL
-- ==========================================
-- Objetivo: Calcular salario neto con retención IRPF
-- Tags: SALARIO, IRPF, DECIMAL, TRANSACCIONES
-- ==========================================

USE logistica_global;

-- Configuraciones de seguridad para MySQL
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

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

-- 5. Asignar valor de 0€ (0) a empleados con salario erróneo
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

-- Restaurar configuraciones
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;