-- ============================================================
-- SANEAMIENTO BASE DE DATOS GHA_ANALYTICS
-- ============================================================
-- Práctica Avanzada: GHA_ANALYTICS
-- Grupo: 1
-- Estudiante: Michael Axel Aguilar Peredo
-- Fecha: 07/04/2026
-- ============================================================
-- Script: SANEAMIENTO
-- Descripción: Saneamiento completo de la base de datos
--              GHA_ANALYTICS usando transacciones
-- ============================================================

USE gha_analytics;

-- ============================================
-- FASE 1: Normalización de Identidad (PACIENTES)
-- ============================================

-- Paso 1.1: Limpiar NIFs (espacios y guiones) ANTES de buscar duplicados
START TRANSACTION;
    UPDATE pacientes SET nif = TRIM(nif);
    UPDATE pacientes SET nif = REPLACE(nif, '-', '');
COMMIT;

-- Paso 1.2: Eliminar NIFs problemáticos (NULL, vacíos, NULL_NIF)
START TRANSACTION;
    DELETE FROM pacientes 
    WHERE nif IS NULL 
       OR nif = '' 
       OR nif = 'NULL_NIF' 
       OR TRIM(nif) = '';
COMMIT;

-- Paso 1.3: Eliminar duplicados exactos (mismo NIF limpio)
START TRANSACTION;
    DELETE p1 FROM pacientes p1 
    INNER JOIN pacientes p2 
    WHERE p1.nif = p2.nif 
      AND p1.id > p2.id;
COMMIT;

-- Paso 1.4: Eliminar NIFs que no cumplan el patrón válido (8 números + 1 letra)
START TRANSACTION;
    DELETE FROM pacientes 
    WHERE nif NOT REGEXP '^[0-9]{8}[A-Z]$';
COMMIT;

SELECT 'FASE 1 OK: Normalización de identidad' AS resultado;

-- ============================================
-- FASE 2: Consistencia de Colegiados (MEDICOS)
-- ============================================

-- Paso 2.1: Limpiar espacios
START TRANSACTION;
    UPDATE medicos SET num_colegiado = TRIM(num_colegiado);
COMMIT;

-- Paso 2.2: Formato "28/5566" → "COL-28-5566"
START TRANSACTION;
    UPDATE medicos 
    SET num_colegiado = CONCAT('COL-', 
                               SUBSTRING_INDEX(num_colegiado, '/', 1), '-', 
                               LPAD(SUBSTRING_INDEX(num_colegiado, '/', -1), 4, '0')) 
    WHERE num_colegiado LIKE '%/%';
COMMIT;

-- Paso 2.3: Formato "28-7788" → "COL-28-7788"
START TRANSACTION;
    UPDATE medicos 
    SET num_colegiado = CONCAT('COL-', 
                               SUBSTRING_INDEX(num_colegiado, '-', 1), '-', 
                               LPAD(SUBSTRING_INDEX(num_colegiado, '-', -1), 4, '0')) 
    WHERE num_colegiado REGEXP '^[0-9]+-[0-9]+$' 
      AND num_colegiado NOT LIKE 'COL-%';
COMMIT;

-- Paso 2.4: Formato "COL289900" → "COL-28-9900"
START TRANSACTION;
    UPDATE medicos 
    SET num_colegiado = CONCAT('COL-', 
                               SUBSTRING(num_colegiado, 4, 2), '-', 
                               LPAD(SUBSTRING(num_colegiado, 6), 4, '0')) 
    WHERE num_colegiado REGEXP '^COL[0-9]{6}$';
COMMIT;

-- Paso 2.5: Formatos inválidos como "INV-999" → "COL-00-0999"
START TRANSACTION;
    UPDATE medicos 
    SET num_colegiado = CONCAT('COL-00-', LPAD(SUBSTRING(num_colegiado, -3), 4, '0')) 
    WHERE num_colegiado NOT LIKE 'COL-%-%';
COMMIT;

SELECT 'FASE 2 OK: Consistencia de colegiados' AS resultado;

-- ============================================
-- FASE 3: Integridad Referencial
-- ============================================

-- Paso 3.1: Corregir especialidad inexistente (id=99) → Medicina General (id=1)
START TRANSACTION;
    UPDATE medicos SET especialidad_id = 1 
    WHERE especialidad_id NOT IN (SELECT id FROM especialidades);
COMMIT;

-- Paso 3.2: Eliminar visitas con referencias huérfanas ANTES de agregar FK
START TRANSACTION;
    DELETE FROM visitas 
    WHERE paciente_id NOT IN (SELECT id FROM pacientes);
    DELETE FROM visitas 
    WHERE medico_id NOT IN (SELECT id FROM medicos);
COMMIT;

-- Paso 3.3: Agregar FK en medicos → especialidades
START TRANSACTION;
    ALTER TABLE medicos 
    ADD CONSTRAINT fk_medicos_especialidad 
    FOREIGN KEY (especialidad_id) REFERENCES especialidades(id);
COMMIT;

-- Paso 3.4: Agregar FK en visitas → pacientes
START TRANSACTION;
    ALTER TABLE visitas 
    ADD CONSTRAINT fk_visitas_paciente 
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id);
COMMIT;

-- Paso 3.5: Agregar FK en visitas → medicos
START TRANSACTION;
    ALTER TABLE visitas 
    ADD CONSTRAINT fk_visitas_medico 
    FOREIGN KEY (medico_id) REFERENCES medicos(id);
COMMIT;

SELECT 'FASE 3 OK: Integridad referencial' AS resultado;

-- ============================================
-- FASE 4: División de Tablas (seguros_pacientes)
-- ============================================
START TRANSACTION;

    -- Paso 4.1: Crear tabla de seguros separada
    CREATE TABLE IF NOT EXISTS seguros_pacientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        paciente_id INT NOT NULL,
        num_poliza VARCHAR(50),
        estado_poliza VARCHAR(20) DEFAULT 'ACTIVA',
        CONSTRAINT fk_seguros_paciente FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    );

    -- Paso 4.2: Migrar datos de num_poliza
    INSERT INTO seguros_pacientes (paciente_id, num_poliza)
    SELECT id, num_poliza 
    FROM pacientes 
    WHERE num_poliza IS NOT NULL 
      AND num_poliza != '';

    -- Paso 4.3: Eliminar columna de pacientes
    ALTER TABLE pacientes DROP COLUMN num_poliza;

COMMIT;

SELECT 'FASE 4 OK: División de tablas' AS resultado;

-- ============================================
-- FASE 5: Columnas Calculadas (VISITAS)
-- ============================================

-- Paso 5.1-5.4: Limpiar importes
START TRANSACTION;
    UPDATE visitas SET importe_sucio = TRIM(importe_sucio);
    UPDATE visitas SET importe_sucio = REPLACE(importe_sucio, '€', '');
    UPDATE visitas SET importe_sucio = REPLACE(importe_sucio, '$', '');
    UPDATE visitas SET importe_sucio = REPLACE(importe_sucio, 'EUR', '');
    UPDATE visitas SET importe_sucio = REPLACE(importe_sucio, ',', '.');
    UPDATE visitas SET importe_sucio = NULL 
    WHERE importe_sucio = '' OR UPPER(importe_sucio) = 'GRATIS';
COMMIT;

-- Paso 5.5: Convertir a DECIMAL
START TRANSACTION;
    ALTER TABLE visitas MODIFY importe_sucio DECIMAL(10,2) NULL;
COMMIT;

-- Paso 5.6: Añadir columna calculada (copago 20%)
START TRANSACTION;
    ALTER TABLE visitas ADD COLUMN copago_estimado DECIMAL(10,2);
    UPDATE visitas SET copago_estimado = ROUND(importe_sucio * 0.20, 2) WHERE importe_sucio IS NOT NULL;
COMMIT;

-- Paso 5.7: Hacer copago NOT NULL
START TRANSACTION;
    UPDATE visitas SET copago_estimado = 0 WHERE copago_estimado IS NULL;
    ALTER TABLE visitas MODIFY copago_estimado DECIMAL(10,2) NOT NULL DEFAULT 0;
COMMIT;

SELECT 'FASE 5 OK: Columnas calculadas' AS resultado;

-- ============================================
-- FASE 6: Ingesta de Datos (RAW_IMPORT_VISITAS)
-- ============================================

-- Paso 6.1: Parsear raw_data e insertar pacientes nuevos
-- Formato: "NIFytics Assertion Fecha|Coste"
START TRANSACTION;

    INSERT INTO pacientes (nif, nombre_completo, tel_contacto, f_nacimiento)
    SELECT 
        TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) AS nif,
        CONCAT(
            TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1)),
            ' (importado)'
        ) AS nombre_completo,
        raw_phone AS tel_contacto,
        NULL AS f_nacimiento
    FROM raw_import_visitas
    WHERE TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) NOT IN (
        SELECT nif FROM pacientes WHERE nif IS NOT NULL
    );

COMMIT;

-- Paso 6.2: Crear tabla temporal para visitas del staging
START TRANSACTION;
    CREATE TEMPORARY TABLE `temp_visitas_staging` (
        paciente_id INT,
        fecha_visita VARCHAR(100),
        importe VARCHAR(50)
    );
COMMIT;

-- Paso 6.3: Parsear e insertar visitas desde staging
START TRANSACTION;

    INSERT INTO `temp_visitas_staging` (paciente_id, fecha_visita, importe)
    SELECT 
        p.id AS paciente_id,
        TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 3), '|', -1)) AS fecha,
        TRIM(SUBSTRING_INDEX(raw_data, '|', -1)) AS importe
    FROM raw_import_visitas r
    INNER JOIN pacientes p ON TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) = p.nif;

COMMIT;

-- Paso 6.4: Insertar visitas normalizadas
START TRANSACTION;

    INSERT INTO visitas (paciente_id, fecha_visita, importe_sucio, descuento_aplicado)
    SELECT 
        paciente_id,
        fecha_visita,
        REPLACE(REPLACE(REPLACE(REPLACE(importe, '€', ''), '$', ''), 'EUR', ''), ',', '.'),
        0
    FROM `temp_visitas_staging`
    WHERE importe IS NOT NULL 
      AND UPPER(importe) NOT LIKE '%GRATIS%';

COMMIT;

-- Paso 6.5: Eliminar objetos de staging
START TRANSACTION;
    DROP TEMPORARY TABLE IF EXISTS `temp_visitas_staging`;
    DROP TABLE IF EXISTS raw_import_visitas;
COMMIT;

SELECT 'FASE 6 OK: Ingesta de datos' AS resultado;

-- ============================================
-- ESCENARIO 2: Saneamiento Profundo
-- ============================================

-- Paso 7.1: Gestionar emails nulos o vacíos
START TRANSACTION;
    UPDATE pacientes 
    SET email = 'desconocido@sinemail.com' 
    WHERE email IS NULL OR email = '';
COMMIT;

-- Paso 7.2: Limpiar fechas de nacimiento
START TRANSACTION;
    UPDATE pacientes SET f_nacimiento = TRIM(f_nacimiento);
    UPDATE pacientes SET f_nacimiento = REPLACE(f_nacimiento, '.', '/');
    UPDATE pacientes SET f_nacimiento = NULL 
    WHERE f_nacimiento = '' OR f_nacimiento IS NULL;
COMMIT;

-- Paso 7.3: Limpiar fechas de visita
START TRANSACTION;
    UPDATE visitas SET fecha_visita = TRIM(fecha_visita);
    UPDATE visitas SET fecha_visita = REPLACE(fecha_visita, '.', '-');
COMMIT;

-- Paso 7.4: Normalizar descuento_aplicado
START TRANSACTION;
    ALTER TABLE visitas MODIFY descuento_aplicado DECIMAL(10,2) DEFAULT 0;
    UPDATE visitas SET descuento_aplicado = 0 WHERE descuento_aplicado IS NULL;
COMMIT;

SELECT 'ESCENARIO 2 OK: Saneamiento profundo' AS resultado;

-- ============================================
-- FASE 8: Índices de Optimización
-- ============================================
START TRANSACTION;

    CREATE INDEX idx_pacientes_nif ON pacientes(nif);
    CREATE INDEX idx_pacientes_email ON pacientes(email);

COMMIT;

START TRANSACTION;

    CREATE INDEX idx_medicos_colegiado ON medicos(num_colegiado);
    CREATE INDEX idx_medicos_especialidad ON medicos(especialidad_id);

COMMIT;

START TRANSACTION;

    CREATE INDEX idx_visitas_fecha ON visitas(fecha_visita);
    CREATE INDEX idx_visitas_paciente ON visitas(paciente_id);
    CREATE INDEX idx_visitas_medico ON visitas(medico_id);

COMMIT;

START TRANSACTION;

    CREATE INDEX idx_seguros_paciente ON seguros_pacientes(paciente_id);

COMMIT;

SELECT 'FASE 8 OK: Índices creados' AS resultado;

-- ============================================
-- VERIFICACIÓN FINAL
-- ============================================
SELECT '========================================' AS '';
SELECT 'RESUMEN DE SANEAMIENTO' AS '';
SELECT '========================================' AS '';

SELECT COUNT(*) AS total_pacientes FROM pacientes;
SELECT COUNT(*) AS total_medicos FROM medicos;
SELECT COUNT(*) AS total_visitas FROM visitas;
SELECT COUNT(*) AS total_seguros FROM seguros_pacientes;

SELECT 'Pacientes saneados:' AS '';
SELECT id, nif, nombre_completo, email FROM pacientes;

SELECT 'Médicos normalizados:' AS '';
SELECT id, num_colegiado, nombre, especialidad_id FROM medicos;

SELECT 'Visitas limpias:' AS '';
SELECT id, paciente_id, medico_id, fecha_visita, importe_sucio, copago_estimado FROM visitas;

SELECT '========================================' AS '';
SELECT 'SANEAMIENTO COMPLETADO' AS '';
SELECT '========================================' AS '';
