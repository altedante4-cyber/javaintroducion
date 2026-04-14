-- ==============================================================================
-- SCRIPT 2: SANEAMIENTO Y RESTRUCTURACIÓN (GHA Analytics)
-- Escenario 1: Blindaje Estructural
-- ==============================================================================

USE gha_analytics;

-- ==============================================================================
-- CONFIGURACIÓN DE SEGURIDAD
-- ==============================================================================
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- Iniciar transacción
START TRANSACTION;
SAVEPOINT inicio_saneamiento;

-- ==============================================================================
-- 1. NORMALIZACIÓN DE IDENTIDAD (PACIENTES)
-- ==============================================================================

-- 1.1 Eliminar duplicados exactos (mismo NIF y nombre), manteniendo el ID más bajo
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

-- 1.2 Limpiar NIF: eliminar espacios en blanco al inicio y final
UPDATE pacientes SET nif = TRIM(nif);

-- 1.3 Corregir NIFs con formato incorrecto (quitar guiones)
UPDATE pacientes SET nif = REPLACE(nif, '-', '') WHERE nif LIKE '%-%';

-- 1.4 Eliminar registros con NIF inválido (no cumple formato 8 números + 1 letra)
DELETE FROM pacientes 
WHERE nif NOT REGEXP '^[0-9]{8}[A-Z]$';

-- 1.5 Aplicar restricciones: UNIQUE y NOT NULL en columna nif
ALTER TABLE pacientes 
MODIFY nif VARCHAR(50) NOT NULL,
ADD UNIQUE (nif);

SAVEPOINT despues_pacientes;

-- ==============================================================================
-- 2. CONSISTENCIA DE COLEGIADOS (MÉDICOS)
-- ==============================================================================

-- 2.1 Estandarizar números de colegiado al formato COL-XX-YYYY
UPDATE medicos SET num_colegiado = TRIM(num_colegiado);

UPDATE medicos 
SET num_colegiado = CONCAT('COL-28-', LPAD(REPLACE(REPLACE(num_colegiado, 'COL-', ''), '-', ''), 4, '0'))
WHERE num_colegiado NOT LIKE 'COL-%';

-- 2.2 Aplicar restricción CHECK para validar formato COL-XX-YYYY
ALTER TABLE medicos 
ADD CONSTRAINT chk_num_colegiado CHECK (num_colegiado REGEXP '^COL-[0-9]{2}-[0-9]{4}$');

SAVEPOINT despues_medicos;

-- ==============================================================================
-- 3. INTEGRIDAD REFERENCIAL
-- ==============================================================================

-- 3.1 Los médicos con especialidades inexistentes → 'Medicina General' (id=1)
UPDATE medicos 
SET especialidad_id = 1 
WHERE especialidad_id NOT IN (SELECT id FROM especialidades);

-- 3.2 Añadir FOREIGN KEY en tabla medicos
ALTER TABLE medicos 
ADD CONSTRAINT fk_medicos_especialidad 
FOREIGN KEY (especialidad_id) REFERENCES especialidades(id);

-- 3.3 Añadir FOREIGN KEY en tabla visitas
-- Corregir referencias inválidas primero
DELETE FROM visitas WHERE paciente_id NOT IN (SELECT id FROM pacientes);
DELETE FROM visitas WHERE medico_id NOT IN (SELECT id FROM medicos);

-- Corregir IDs inválidos
UPDATE visitas SET medico_id = 1 WHERE medico_id = 888;
UPDATE visitas SET paciente_id = 1 WHERE paciente_id = 999;

-- Añadir claves foráneas
ALTER TABLE visitas 
ADD CONSTRAINT fk_visitas_paciente FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
ADD CONSTRAINT fk_visitas_medico FOREIGN KEY (medico_id) REFERENCES medicos(id);

SAVEPOINT despues_integridad;

-- ==============================================================================
-- 4. NORMALIZACIÓN Y DIVISIÓN DE TABLAS
-- ==============================================================================

-- 4.1 Crear tabla seguros_pacientes
CREATE TABLE seguros_pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    num_poliza VARCHAR(50) NOT NULL,
    estado_poliza VARCHAR(20) DEFAULT 'ACTIVA',
    CONSTRAINT fk_seguros_paciente FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    UNIQUE (paciente_id)
) ENGINE=InnoDB;

-- 4.2 Insertar datos de pólizas desde pacientes
INSERT INTO seguros_pacientes (paciente_id, num_poliza)
SELECT id, num_poliza 
FROM pacientes 
WHERE num_poliza IS NOT NULL AND num_poliza != '';

-- 4.3 Eliminar columna num_poliza de pacientes
ALTER TABLE pacientes DROP COLUMN num_poliza;

SAVEPOINT despues_seguros;

-- ==============================================================================
-- 5. COLUMNAS CALCULADAS Y BLINDAJE
-- ==============================================================================

-- 5.1 Añadir columna copago_estimado DECIMAL(10,2) a visitas
ALTER TABLE visitas ADD COLUMN copago_estimado DECIMAL(10,2);

-- 5.2 Saneamiento de importe_sucio
UPDATE visitas SET importe_sucio = TRIM(importe_sucio);
UPDATE visitas SET importe_sucio = REPLACE(REPLACE(REPLACE(importe_sucio, '€', ''), '$', ''), 'EUR', '');
UPDATE visitas SET importe_sucio = '0' WHERE LOWER(importe_sucio) = 'gratis';
UPDATE visitas SET importe_sucio = REPLACE(importe_sucio, ',', '.');

-- 5.3 Calcular copago_estimado como 20% del importe
UPDATE visitas 
SET copago_estimado = CAST(importe_sucio AS DECIMAL(10,2)) * 0.20;

-- 5.4 Blindaje Final: hacer obligatorios (NOT NULL)
ALTER TABLE visitas MODIFY copago_estimado DECIMAL(10,2) NOT NULL;
ALTER TABLE seguros_pacientes MODIFY num_poliza VARCHAR(50) NOT NULL;

SAVEPOINT despues_copago;

-- ==============================================================================
-- 6. INGESTA DE DATOS EXTERNOS
-- ==============================================================================

-- 6.1 Insertar nuevos pacientes desde raw_import_visitas
INSERT INTO pacientes (nif, nombre_completo, f_nacimiento, num_poliza)
SELECT 
    TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) AS nif,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1)) AS nombre,
    SUBSTRING_INDEX(raw_data, '|', 3) AS fecha,
    'PENDIENTE' AS poliza
FROM raw_import_visitas
WHERE SUBSTRING_INDEX(raw_data, '|', 1) NOT IN (SELECT nif FROM pacientes);

-- 6.2 Importar visitas de datos externos
INSERT INTO visitas (paciente_id, medico_id, fecha_visita, importe_sucio, copago_estimado)
SELECT 
    p.id AS paciente_id,
    1 AS medico_id,
    SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 3), '|', -1) AS fecha,
    TRIM(REPLACE(REPLACE(REPLACE(SUBSTRING_INDEX(raw_data, '|', 4), '€', ''), '$', ''), 'EUR', '')) AS importe,
    CAST(REPLACE(REPLACE(REPLACE(SUBSTRING_INDEX(raw_data, '|', 4), '€', ''), '$', ''), 'EUR', '') AS DECIMAL(10,2)) * 0.20 AS copago
FROM raw_import_visitas r
LEFT JOIN pacientes p ON TRIM(SUBSTRING_INDEX(r.raw_data, '|', 1)) = p.nif
WHERE p.id IS NOT NULL;

-- ==============================================================================
-- FINALIZACIÓN
-- ==============================================================================

-- Reactivar verificación de claves foráneas
SET FOREIGN_KEY_CHECKS = 1;
SET SQL_SAFE_UPDATES = 1;

-- Confirmar todos los cambios
COMMIT;

-- ==============================================================================
-- RESUMEN DE RESTRICCIONES APLICADAS
-- ==============================================================================
-- Tabla pacientes:       nif UNIQUE NOT NULL
-- Tabla medicos:         num_colegiado CHECK (formato COL-XX-YYYY), FK a especialidades
-- Tabla visitas:         FK a pacientes y medicos, copago_estimado NOT NULL
-- Tabla seguros_pacientes: paciente_id UNIQUE, num_poliza NOT NULL, FK a pacientes
-- ==============================================================================