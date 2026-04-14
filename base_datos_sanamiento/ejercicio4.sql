-- ==========================================
-- EJERCICIO 4: AUDITORÍA DE RETRASOS
-- ==========================================
-- Objetivo: Normalizar fechas y calcular días de retraso
-- Tags: FECHAS, DATEDIFF, REGEXP, AUDITORÍA
-- ==========================================

USE logistica_global;

-- Configuraciones de seguridad para MySQL
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

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

-- Restaurar configuraciones
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;