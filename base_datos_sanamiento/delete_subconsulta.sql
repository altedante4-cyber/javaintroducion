-- ==============================================================================
-- EJERCICIOS DELETE CON SUBCONSULTA
-- Preparación para examen GHA Analytics
-- ==============================================================================

USE gha_analytics;

-- ==============================================================================
-- EJERCICIO 1: Eliminar pacientes duplicados (mismo NIF y nombre)
-- Mantener el ID más bajo, eliminar los demás
-- ==============================================================================

DELETE FROM pacientes 
WHERE id IN (
    SELECT id FROM (
        SELECT p2.id 
        FROM pacientes p1
        JOIN pacientes p2 ON p1.nif = p2.nif 
                      AND TRIM(p1.nombre_completo) = TRIM(p2.nombre_completo)
                      AND p1.id < p2.id
    ) AS duplicados
);

-- ==============================================================================
-- EJERCICIO 2: Eliminar visitas de pacientes inexistentes
-- ==============================================================================

DELETE FROM visitas 
WHERE paciente_id NOT IN (
    SELECT id FROM pacientes
);

-- ==============================================================================
-- EJERCICIO 3: Eliminar médicos de especialidades inexistentes
-- ==============================================================================

DELETE FROM medicos 
WHERE especialidad_id NOT IN (
    SELECT id FROM especialidades
);

-- ==============================================================================
-- EJERCICIO 4: Eliminar visitas con importe 0 o NULL
-- ==============================================================================

DELETE FROM visitas 
WHERE importe_sucio IS NULL 
   OR importe_sucio = '' 
   OR CAST(importe_sucio AS DECIMAL(10,2)) = 0;

-- ==============================================================================
-- EJERCICIO 5: Eliminar pacientes sin email ni teléfono
-- ==============================================================================

DELETE FROM pacientes 
WHERE email IS NULL 
  AND tel_contacto IS NULL;

-- ==============================================================================
-- EJERCICIO 6: Eliminar NIFs con formato inválido
-- Formato válido: 8 números + 1 letra mayúscula
-- ==============================================================================

DELETE FROM pacientes 
WHERE nif NOT REGEXP '^[0-9]{8}[A-Z]$';

-- ==============================================================================
-- EJERCICIO 7: Eliminar visitas antiguas (antes de 2025)
-- ==============================================================================

DELETE FROM visitas 
WHERE STR_TO_DATE(fecha_visita, '%d/%m/%Y') < '2025-01-01';

-- ==============================================================================
-- EJERCICIO 8: Eliminar pólizas duplicadas (mantener más reciente)
-- ==============================================================================

DELETE FROM seguros_pacientes 
WHERE id NOT IN (
    SELECT * FROM (
        SELECT MAX(id)
        FROM seguros_pacientes
        GROUP BY paciente_id
    ) AS max_id
);

-- ==============================================================================
-- EJERCICIO 9: Eliminar médicos sin especialidad asignada
-- ==============================================================================

DELETE FROM medicos 
WHERE especialidad_id IS NULL;

-- ==============================================================================
-- EJERCICIO 10: Eliminar registros de raw_import ya procesados
-- ==============================================================================
-- Suponiendo que tenemos una tabla que controla los ya importados

DELETE FROM raw_import_visitas 
WHERE ext_id IN (
    SELECT ext_id 
    FROM raw_import_visitas 
    WHERE TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) IN (
        SELECT nif FROM pacientes
    )
);

-- ==============================================================================
-- VARIANTES DE DELETE CON SUBCONSULTA
-- ==============================================================================

-- Variante A: DELETE con subconsulta en WHERE (correlacionada)
DELETE FROM visitas v
WHERE EXISTS (
    SELECT 1 FROM pacientes p 
    WHERE p.id = v.paciente_id AND p.nif IS NULL
);

-- Variante B: DELETE con subconsulta con ANY/ALL
DELETE FROM medicos 
WHERE especialidad_id > ALL (
    SELECT id FROM especialidades
);

-- Variante C: DELETE con subconsulta con IN
DELETE FROM pacientes 
WHERE id IN (
    SELECT paciente_id FROM seguros_pacientes WHERE estado_poliza = 'CANCELADA'
);

-- Variante D: DELETE con subconsulta con NOT IN
DELETE FROM seguros_pacientes 
WHERE paciente_id NOT IN (
    SELECT id FROM pacientes
);

-- Variante E: DELETE con subconsulta con JOIN
DELETE p FROM pacientes p
INNER JOIN seguros_pacientes s ON p.id = s.paciente_id
WHERE s.estado_poliza = 'CANCELADA';

-- ==============================================================================
-- NOTAS IMPORTANTES PARA EL EXAMEN:
-- ==============================================================================
-- 1. MySQL requiere envolver subconsultas deletes en otra subconsulta
--    cuando se referencia la misma tabla
-- 2. Usar SET SQL_SAFE_UPDATES = 0 antes de DELETE
-- 3. Verificar siempre con SELECT antes de hacer DELETE
-- 4. Usar transacciones para pruebas
-- ==============================================================================