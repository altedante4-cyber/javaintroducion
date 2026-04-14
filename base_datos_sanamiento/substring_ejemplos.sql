-- ==============================================================================
-- EJERCICIOS SUBSTRING / SUBSTRING_INDEX
-- Preparación para examen GHA Analytics
-- ==============================================================================

USE gha_analytics;

-- ==============================================================================
-- SUBSTRING vs SUBSTRING_INDEX
-- ==============================================================================
-- SUBSTRING(cadena, inicio, longitud) - Extrae desde posición específica
-- SUBSTRING_INDEX(cadena, delimitador, n) - Extrae hasta el énésimo delimitador

-- ==============================================================================
-- EJERCICIO 1: Extraer NIF del campo raw_data
-- Formato: "NIF%|████████|FechaVisita|Coste"
-- ==============================================================================

-- Con SUBSTRING_INDEX (primera parte hasta |)
SELECT SUBSTRING_INDEX(raw_data, '|', 1) AS nif
FROM raw_import_visitas;

-- Con SUBSTRING (desde posición 1, 9 caracteres)
SELECT SUBSTRING(raw_data, 1, 9) AS nif
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 2: Extraer nombre del campo raw_data
-- Formato: "NIF|apellidosNombre|FechaVisita|Coste"
-- ==============================================================================

-- Segunda parte (entre primer y segundo |)
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1) AS nombre
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 3: Extraer fecha del campo raw_data
-- Tercera parte
-- ==============================================================================

SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 3), '|', -1) AS fecha
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 4: Extraer importe del campo raw_data
-- Cuarta parte (última)
-- ==============================================================================

SELECT SUBSTRING_INDEX(raw_data, '|', -1) AS importe
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 5: Limpiar importes con símbolos de moneda
-- ==============================================================================

-- Eliminar todo después de |
SELECT TRIM(SUBSTRING_INDEX(raw_data, '|', -1)) AS importe_limpio
FROM raw_import_visitas;

-- Eliminar símbolos €, $, EUR
SELECT TRIM(REPLACE(REPLACE(REPLACE(
    SUBSTRING_INDEX(raw_data, '|', -1), 
    '€', ''), '$', ''), 'EUR', '')) AS importe_limpio
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 6: Extraer provincia del número de colegiado
-- Formato: COL-XX-YYYY
-- ==============================================================================

-- Extraer XX (posición 5-6)
SELECT SUBSTRING(num_colegiado, 5, 2) AS provincia
FROM medicos;

-- ==============================================================================
-- EJERCICIO 7: Extraer número de colegiado sin prefijo
-- Formato: COL-XX-YYYY -> YYYY
-- ==============================================================================

SELECT SUBSTRING(num_colegiado, 9, 4) AS num_sin_prefijo
FROM medicos;

-- ==============================================================================
-- EJERCICIO 8: Extraer año de fecha_visita
-- Formato: dd/mm/aaaa
-- ==============================================================================

-- Con SUBSTRING (últimos 4 caracteres)
SELECT SUBSTRING(fecha_visita, -4, 4) AS año
FROM visitas;

-- Con SUBSTRING_INDEX después del último /
SELECT SUBSTRING_INDEX(fecha_visita, '/', -1) AS año
FROM visitas;

-- ==============================================================================
-- EJERCICIO 9: Extraer mes de fecha_visita
-- ==============================================================================

-- Con SUBSTRING_INDEX (segunda parte)
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(fecha_visita, '/', 2), '/', -1) AS mes
FROM visitas;

-- ==============================================================================
-- EJERCICIO 10: Extraer día de fecha_visita
-- ==============================================================================

SELECT SUBSTRING_INDEX(fecha_visita, '/', 1) AS dia
FROM visitas;

-- ==============================================================================
-- EJERCICIO 11: Procesar raw_data completo con TRIM
-- ==============================================================================

SELECT 
    TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) AS nif,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1)) AS nombre,
    SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 3), '|', -1) AS fecha,
    TRIM(REPLACE(REPLACE(REPLACE(SUBSTRING_INDEX(raw_data, '|', -1), '€', ''), '$', ''), 'EUR', '')) AS importe
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 12: Actualizar NIF en pacientes desde raw_data
-- ==============================================================================

UPDATE pacientes p
INNER JOIN raw_import_visitas r ON p.nif = SUBSTRING_INDEX(r.raw_data, '|', 1)
SET p.nif = TRIM(SUBSTRING_INDEX(r.raw_data, '|', 1));

-- ==============================================================================
-- EJERCICIO 13: Insertar nuevos pacientes desde raw
-- ==============================================================================

INSERT INTO pacientes (nif, nombre_completo, f_nacimiento)
SELECT 
    TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) AS nif,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1)) AS nombre,
    SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 3), '|', -1) AS fecha
FROM raw_import_visitas
WHERE TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) NOT IN (
    SELECT nif FROM pacientes
);

-- ==============================================================================
-- EJERCICIO 14: Contar partes en raw_data
-- ==============================================================================

SELECT 
    raw_data,
    LENGTH(raw_data) - LENGTH(REPLACE(raw_data, '|', '')) + 1 AS num_partes
FROM raw_import_visitas;

-- ==============================================================================
-- EJERCICIO 15: Validar formato raw_data (4 partes)
-- ==============================================================================

SELECT raw_data
FROM raw_import_visitas
WHERE LENGTH(raw_data) - LENGTH(REPLACE(raw_data, '|', '')) + 1 != 4;

-- ==============================================================================
-- EJERCICIO 16: Extraer extensión de email
-- ==============================================================================

SELECT email, SUBSTRING_INDEX(email, '@', -1) AS dominio
FROM pacientes
WHERE email IS NOT NULL;

-- ==============================================================================
-- EJERCICIO 17: Extraer prefijo de teléfono
-- ==============================================================================

SELECT tel_contacto, SUBSTRING(tel_contacto, 1, 3) AS prefijo
FROM pacientes
WHERE tel_contacto LIKE '+34%';

-- ==============================================================================
-- EJERCICIO 18: Convertir formato de fecha
-- ==============================================================================

-- Cambiar formato dd/mm/aaaa a aaaa-mm-dd
SELECT 
    CONCAT(
        SUBSTRING_INDEX(fecha_visita, '/', -1), '-',
        SUBSTRING_INDEX(SUBSTRING_INDEX(fecha_visita, '/', 2), '/', -1), '-',
        SUBSTRING_INDEX(fecha_visita, '/', 1)
    ) AS fecha_sql
FROM visitas;

-- ==============================================================================
-- EJERCICIO 19: Extraer caracteres del centro
-- ==============================================================================

SELECT nombre_completo, SUBSTRING(nombre_completo, 3, 5) AS recorte
FROM pacientes;

-- ==============================================================================
-- EJERCICIO 20: Combinar SUBSTRING con otras funciones
-- ==============================================================================

SELECT 
    UPPER(SUBSTRING(nombre_completo, 1, 1)) AS primera_letra,
    LENGTH(nombre_completo) AS longitud
FROM pacientes;

-- ==============================================================================
-- RESUMEN DE FUNCIONES SUBSTRING
-- ==============================================================================
-- SUBSTRING(cadena, inicio)           - Desde posición
-- SUBSTRING(cadena, inicio, longitud)  - Con longitud
-- SUBSTRING(cadena, -inicio)          - Desde el final
-- SUBSTRING_INDEX(cadena, delim, n)      - Hacia el énésimo delim
-- SUBSTRING_INDEX(cadena, delim, -n)  - Desde el final (-1 = último)
-- ==============================================================================