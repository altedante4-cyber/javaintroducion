-- ==============================================================================
-- CONSULTAS DE VALIDACIÓN
-- Verificaciones post-sanenamiento GHA Analytics
-- ==============================================================================

USE gha_analytics;

-- ==============================================================================
-- 1. VALIDACIÓN DE PACIENTES
-- ==============================================================================

-- 1.1 Verificar NIFs duplicados
SELECT nif, COUNT(*) AS duplicados
FROM pacientes
GROUP BY nif
HAVING COUNT(*) > 1;

-- 1.2 Verificar NIFs con formato inválido
SELECT id, nif, nombre_completo
FROM pacientes
WHERE nif NOT REGEXP '^[0-9]{8}[A-Z]$';

-- 1.3 Verificar pacientes sin NIF
SELECT id, nombre_completo, email
FROM pacientes
WHERE nif IS NULL OR nif = '';

-- 1.4 Verificar pacientes sin email ni teléfono
SELECT id, nombre_completo, email, tel_contacto
FROM pacientes
WHERE email IS NULL AND tel_contacto IS NULL;

-- 1.5 Contar pacientes totales
SELECT COUNT(*) AS total_pacientes FROM pacientes;

-- ==============================================================================
-- 2. VALIDACIÓN DE MÉDICOS
-- ==============================================================================

-- 2.1 Verificar números de colegiado con formato inválido
SELECT id, num_colegiado, nombre
FROM medicos
WHERE num_colegiado NOT REGEXP '^COL-[0-9]{2}-[0-9]{4}$';

-- 2.2 Verificar médicos sin especialidad
SELECT id, nombre, num_colegiado, especialidad_id
FROM medicos
WHERE especialidad_id IS NULL;

-- 2.3 Verificar médicos con especialidad inexistente
SELECT m.id, m.nombre, m.especialidad_id
FROM medicos m
LEFT JOIN especialidades e ON m.especialidad_id = e.id
WHERE e.id IS NULL;

-- 2.4 Listar médicos por especialidad
SELECT m.nombre, m.num_colegiado, e.nombre AS especialidad
FROM medicos m
INNER JOIN especialidades e ON m.especialidad_id = e.id;

-- ==============================================================================
-- 3. VALIDACIÓN DE VISITAS
-- ==============================================================================

-- 3.1 Verificar visitas con paciente inexistente
SELECT v.id, v.paciente_id, v.fecha_visita
FROM visitas v
LEFT JOIN pacientes p ON v.paciente_id = p.id
WHERE p.id IS NULL;

-- 3.2 Verificar visitas con médico inexistente
SELECT v.id, v.medico_id, v.fecha_visita
FROM visitas v
LEFT JOIN medicos m ON v.medico_id = m.id
WHERE m.id IS NULL;

-- 3.3 Verificar visitas con importe inválido
SELECT id, paciente_id, importe_sucio
FROM visitas
WHERE importe_sucio IS NULL 
   OR importe_sucio = '' 
   OR importe_sucio NOT REGEXP '^[0-9.,]+$';

-- 3.4 Verificar copago_estimado nulo
SELECT id, paciente_id, copago_estimado
FROM visitas
WHERE copago_estimado IS NULL;

-- 3.5 Calcular total facturado
SELECT SUM(CAST(importe_sucio AS DECIMAL(10,2))) AS total_facturado
FROM visitas;

-- ==============================================================================
-- 4. VALIDACIÓN DE SEGUROS
-- ==============================================================================

-- 4.1 Verificar pólizas sin paciente
SELECT s.id, s.paciente_id, s.num_poliza
FROM seguros_pacientes s
LEFT JOIN pacientes p ON s.paciente_id = p.id
WHERE p.id IS NULL;

-- 4.2 Verificar pólizas duplicadas por paciente
SELECT paciente_id, COUNT(*) AS duplicados
FROM seguros_pacientes
GROUP BY paciente_id
HAVING COUNT(*) > 1;

-- 4.3 Verificar pacientes sin seguro
SELECT p.id, p.nombre_completo
FROM pacientes p
LEFT JOIN seguros_pacientes s ON p.id = s.paciente_id
WHERE s.id IS NULL;

-- 4.4 Listar pólizas activas
SELECT p.nombre_completo, s.num_poliza, s.estado_poliza
FROM pacientes p
INNER JOIN seguros_pacientes s ON p.id = s.paciente_id
WHERE s.estado_poliza = 'ACTIVA';

-- ==============================================================================
-- 5. VALIDACIÓN DE INTEGRIDAD REFERENCIAL
-- ==============================================================================

-- 5.1 Verificar todas las FK de visitas
SELECT 
    v.id,
    CASE 
        WHEN p.id IS NULL THEN 'FK paciente inválida'
        WHEN m.id IS NULL THEN 'FK médico inválida'
        ELSE 'OK'
    END AS estado
FROM visitas v
LEFT JOIN pacientes p ON v.paciente_id = p.id
LEFT JOIN medicos m ON v.medico_id = m.id;

-- 5.2 Verificar médicos con FK a especialidades
SELECT m.id, m.nombre, m.especialidad_id, e.nombre
FROM medicos m
LEFT JOIN especialidades e ON m.especialidad_id = e.id;

-- ==============================================================================
-- 6. VALIDACIÓN DE FECHAS
-- ==============================================================================

-- 6.1 Verificar fechas con formato inválido
SELECT id, fecha_visita
FROM visitas
WHERE fecha_visita NOT REGEXP '^[0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4}';

-- 6.2 Verificar fechas futuras
SELECT id, fecha_visita
FROM visitas
WHERE STR_TO_DATE(fecha_visita, '%d/%m/%Y') > CURDATE();

-- ==============================================================================
-- 7. CHECKS ACTIVOS EN LA BASE DE DATOS
-- ==============================================================================

-- 7.1 Listar todas las restricciones CHECK
SELECT 
    CONSTRAINT_NAME,
    CHECK_CLAUSE
FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS
WHERE TABLE_SCHEMA = 'gha_analytics';

-- 7.2 Listar todas las FOREIGN KEYs
SELECT 
    CONSTRAINT_NAME,
    TABLE_NAME,
    COLUMN_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'gha_analytics'
  AND REFERENCED_TABLE_NAME IS NOT NULL;

-- ==============================================================================
-- 8. RESUMEN ESTADÍSTICO
-- ==============================================================================

SELECT 'Pacientes' AS tabla, COUNT(*) AS registros FROM pacientes
UNION ALL
SELECT 'Médicos', COUNT(*) FROM medicos
UNION ALL
SELECT 'Visitas', COUNT(*) FROM visitas
UNION ALL
SELECT 'Especialidades', COUNT(*) FROM especialidades
UNION ALL
SELECT 'Seguros', COUNT(*) FROM seguros_pacientes;

-- ==============================================================================