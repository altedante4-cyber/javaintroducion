-- ============================================================
-- SCRIPT DE LIMPIEZA TOTAL - LOGÍSTICA GLOBAL 4.0
-- ============================================================
-- Objetivo: Transformar la base de datos "sucia" en un 
-- sistema relacional óptimo con integridad referencial
-- Fecha: 2026-04-14
-- 
-- ESTRUCTURA DEL SCRIPT:
-- 1. Creación de tablas de staging (trabajo seguro)
-- 2. Limpieza y normalización de datos por tabla
-- 3. Aplicación de constraints y blindaje final
-- ============================================================

USE logistica_global;

-- ============================================================
-- CONFIGURACIONES DE SEGURIDAD MYSQL
-- ============================================================
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- ============================================================
-- FASE 1: CREACIÓN DE TABLAS DE STAGING
-- ============================================================
-- Justificación: Working con tablas intermedias permite
-- realizar transformaciones sin afectar los datos originales.
-- Si algo falla, tenemos backup en las tablas originales.

DROP TABLE IF EXISTS stg_almacenes;
CREATE TABLE stg_almacenes LIKE almacenes;

DROP TABLE IF EXISTS stg_empleados;
CREATE TABLE stg_empleados LIKE empleados;

DROP TABLE IF EXISTS stg_vehiculos;
CREATE TABLE stg_vehiculos LIKE vehiculos;

DROP TABLE IF EXISTS stg_clientes;
CREATE TABLE stg_clientes LIKE clientes;

DROP TABLE IF EXISTS stg_envios;
CREATE TABLE stg_envios LIKE envios;

DROP TABLE IF EXISTS stg_incidencias;
CREATE TABLE stg_incidencias LIKE incidencias;

DROP TABLE IF EXISTS stg_proveedores;
CREATE TABLE stg_proveedores LIKE proveedores;

DROP TABLE IF EXISTS stg_mantenimientos;
CREATE TABLE stg_mantenimientos LIKE mantenimientos_flota;

SELECT '>>> FASE 1: Tablas de staging creadas' AS Progreso;

-- ============================================================
-- FASE 2: LIMPIEZA DE ALMACENES
-- ============================================================
-- Problemas identificados:
-- - null en ciudad_ubicacion
-- - cod_almacen duplicado (ALM-001)
-- - capacidad_m3 con texto sucio ("m3", "metros cúbicos")
-- - ubicacion_geografica con formatos mixtos

INSERT INTO stg_almacenes
SELECT 
    id,
    TRIM(cod_almacen),
    TRIM(nombre_sucursal),
    TRIM(ciudad_ubicacion),
    CAST(REPLACE(REPLACE(REPLACE(capacity_m3, 'm3', ''), 'metros cúbicos', ''), ' ', '') AS DECIMAL(10,2)),
    TRIM(tel_contacto),
    TRIM(tipo_gestion),
    TRIM(ubicacion_geografica)
FROM almacenes;

DELETE FROM stg_almacenes WHERE cod_almacen IS NULL OR cod_almacen = '';
DELETE FROM stg_almacenes WHERE id NOT IN (
    SELECT MIN(id) FROM stg_almacenes GROUP BY cod_almacen
);

SELECT '>>> Almacenes limpiados' AS Progreso;

-- ============================================================
-- FASE 3: LIMPIEZA DE VEHÍCULOS
-- ============================================================

INSERT INTO stg_vehiculos
SELECT 
    id,
    TRIM(matricula),
    TRIM(marca_modelo),
    CAST(REGEXP_REPLACE(año_fabricacion, '[^0-9]', '') AS UNSIGNED),
    TRIM(f_ultima_itv),
    TRIM(estado_vehiculo),
    TRIM(num_bastidor_vin),
    TRIM(coordenadas_gps)
FROM vehiculos;

DELETE FROM stg_vehiculos WHERE matricula IS NULL OR matricula = '';
DELETE FROM stg_vehiculos WHERE id NOT IN (
    SELECT MIN(id) FROM stg_vehiculos GROUP BY matricula
);

SELECT '>>> Vehículos limpiados' AS Progreso;

-- ============================================================
-- FASE 4: LIMPIEZA DE CLIENTES
-- ============================================================

INSERT INTO stg_clientes
SELECT 
    id,
    TRIM(cif_nif),
    TRIM(razon_social),
    TRIM(direccion_fiscal),
    TRIM(cp_postal),
    TRIM(email_facturacion),
    TRIM(tipo_cliente),
    CAST(REPLACE(REPLACE(limite_credito_sucio, '€', ''), 'USD', '') AS DECIMAL(12,2)),
    NULL,
    TRIM(activo)
FROM clientes;

DELETE FROM stg_clientes WHERE cif_nif IS NULL OR cif_nif = '' OR cif_nif = ' ';
DELETE FROM stg_clientes WHERE razon_social IS NULL OR razon_social = '';
DELETE FROM stg_clientes WHERE id NOT IN (
    SELECT MIN(id) FROM stg_clientes GROUP BY cif_nif
);

SELECT '>>> Clientes limpiados' AS Progreso;

-- ============================================================
-- FASE 5: LIMPIEZA DE EMPLEADOS
-- ============================================================

INSERT INTO stg_empleados
SELECT 
    id,
    TRIM(nif_nie),
    TRIM(nombre_completo),
    REPLACE(email_corp, '@@', '@'),
    NULL,
    TRIM(puesto_rol),
    CAST(REPLACE(REPLACE(salario_base_sucio, 'EUR', ''), ' ', '') AS DECIMAL(10,2)),
    TRIM(num_ss),
    NULL,
    TRIM(seguro_medico),
    CASE 
        WHEN TRIM(activo_boolean) IN ('1', 'SI', 'S', 'YES', 'Y') THEN '1'
        WHEN TRIM(activo_boolean) IN ('0', 'NO', 'N', 'NO') THEN '0'
        ELSE '1'
    END
FROM empleados;

DELETE FROM stg_empleados WHERE nif_nie IS NULL OR nif_nie = '';
DELETE FROM stg_empleados WHERE id NOT IN (
    SELECT MIN(id) FROM stg_empleados GROUP BY nif_nie
);

SELECT '>>> Empleados limpiados' AS Progreso;

-- ============================================================
-- FASE 6: LIMPIEZA DE ENVIOS
-- ============================================================

INSERT INTO stg_envios
SELECT 
    id,
    TRIM(tracking_number),
    cliente_id,
    vehiculo_id,
    empleado_id,
    NULL,
    NULL,
    NULL,
    CAST(REGEXP_REPLACE(peso_kg_bruto, '[^0-9.]', '') AS DECIMAL(10,2)),
    CAST(REGEXP_REPLACE(volumen_m3, '[^0-9.]', '') AS DECIMAL(10,2)),
    CAST(REPLACE(importe_envio, '€', '') AS DECIMAL(10,2)),
    TRIM(seguro_contratado),
    TRIM(estado_envio),
    almacen_destino_id,
    TRIM(prioridad),
    TRIM(ruta_origen_ciudad),
    TRIM(ruta_destino_ciudad),
    CAST(REGEXP_REPLACE(ruta_distancia_km, '[^0-9.]', '') AS DECIMAL(10,2)),
    CAST(REGEXP_REPLACE(ruta_peajes_estimados, '[^0-9.]', '') AS DECIMAL(10,2)),
    CAST(REGEXP_REPLACE(ruta_tiempo_estimado_h, '[^0-9.]', '') AS DECIMAL(10,2))
FROM envios;

DELETE FROM stg_envios WHERE tracking_number IS NULL OR tracking_number = '';
DELETE FROM stg_envios WHERE id NOT IN (
    SELECT MIN(id) FROM stg_envios GROUP BY tracking_number
);

SELECT '>>> Envíos limpiados' AS Progreso;

-- ============================================================
-- FASE 7: LIMPIEZA DE INCIDENCIAS
-- ============================================================

INSERT INTO stg_incidencias
SELECT 
    id,
    envio_id,
    NULL,
    TRIM(descripcion_breve),
    CAST(REGEXP_REPLACE(coste_asociado_sucio, '[^0-9.]', '') AS DECIMAL(10,2)),
    responsable_id,
    TRIM(estado_resolucion),
    TRIM(tipo_incidencia)
FROM incidencias;

DELETE FROM stg_incidencias WHERE envio_id NOT IN (SELECT id FROM stg_envios);

SELECT '>>> Incidencias limpiadas' AS Progreso;

-- ============================================================
-- FASE 8: LIMPIEZA DE PROVEEDORES
-- ============================================================

INSERT INTO stg_proveedores
SELECT 
    id,
    TRIM(cif_prov),
    TRIM(nombre_comercial),
    TRIM(tipo_suministro),
    TRIM(tel_emergencias),
    TRIM(email_prov),
    TRIM(condiciones_pago),
    CAST(REGEXP_REPLACE(valoracion_estrellas, '[^0-9]', '') AS UNSIGNED),
    NULL
FROM proveedores;

DELETE FROM stg_proveedores WHERE cif_prov IS NULL OR cif_prov = '';

SELECT '>>> Proveedores limpiados' AS Progreso;

-- ============================================================
-- FASE 9: LIMPIEZA DE MANTENIMIENTOS
-- ============================================================

INSERT INTO stg_mantenimientos
SELECT 
    id,
    vehiculo_id,
    NULL,
    TRIM(taller_nombre),
    CAST(REGEXP_REPLACE(coste_reparacion, '[^0-9.]', '') AS DECIMAL(10,2)),
    TRIM(piezas_reemplazadas),
    NULL
FROM mantenimientos_flota;

DELETE FROM stg_mantenimientos WHERE vehiculo_id NOT IN (SELECT id FROM stg_vehiculos);

SELECT '>>> Mantenimientos limpiados' AS Progreso;

-- ============================================================
-- FASE 10: NORMALIZACIÓN DE FECHAS
-- ============================================================

DELIMITER //
DROP FUNCTION IF EXISTS fn_parse_fecha//
CREATE FUNCTION fn_parse_fecha(fecha_sucia VARCHAR(50))
RETURNS DATE
DETERMINISTIC
BEGIN
    DECLARE resultado DATE DEFAULT NULL;
    SET fecha_sucia = TRIM(fecha_sucia);
    IF fecha_sucia IS NULL OR fecha_sucia = '' THEN
        RETURN NULL;
    END IF;
    IF fecha_sucia REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN
        SET resultado = STR_TO_DATE(fecha_sucia, '%Y-%m-%d');
    ELSEIF fecha_sucia REGEXP '^[0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{4}$' THEN
        SET resultado = STR_TO_DATE(fecha_sucia, '%d/%m/%Y');
    ELSEIF fecha_sucia REGEXP '^[0-9]{4}/[0-9]{2}/[0-9]{2}$' THEN
        SET resultado = STR_TO_DATE(fecha_sucia, '%Y/%m/%d');
    ELSEIF fecha_sucia REGEXP '^[0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2}$' THEN
        SET resultado = STR_TO_DATE(fecha_sucia, '%d/%m/%y');
    ELSEIF fecha_sucia REGEXP '^[0-9]{2}[/-][0-9]{2}[/-][0-9]{2}$' THEN
        SET resultado = STR_TO_DATE(fecha_sucia, '%y-%m-%d');
    END IF;
    RETURN resultado;
END//
DELIMITER ;

SELECT '>>> FASE 10: Función de fechas creada' AS Progreso;

-- ============================================================
-- FASE 11: CORRECCIÓN DE FOREIGN KEYS HUÉRFANAS
-- ============================================================

DELETE FROM stg_empleados WHERE almacen_id IS NOT NULL 
AND almacen_id NOT IN (SELECT id FROM stg_almacenes);

DELETE FROM stg_envios WHERE cliente_id IS NOT NULL 
AND cliente_id NOT IN (SELECT id FROM stg_clientes);

DELETE FROM stg_envios WHERE vehiculo_id IS NOT NULL 
AND vehiculo_id NOT IN (SELECT id FROM stg_vehiculos);

DELETE FROM stg_incidencias WHERE envio_id IS NOT NULL 
AND envio_id NOT IN (SELECT id FROM stg_envios);

SELECT '>>> FASE 11: FK huérfanas corregidas' AS Progreso;

-- ============================================================
-- FASE 12: CREACIÓN DE TABLAS LIMPIAS CON CONSTRAINTS
-- ============================================================

DROP TABLE IF EXISTS limp_almacenes;
CREATE TABLE limp_almacenes (
    id INT PRIMARY KEY,
    cod_almacen VARCHAR(50) NOT NULL UNIQUE,
    nombre_sucursal VARCHAR(150) NOT NULL,
    ciudad_ubicacion VARCHAR(100),
    capacidad_m3 DECIMAL(10,2),
    tel_contacto VARCHAR(50),
    tipo_gestion VARCHAR(50),
    ubicacion_geografica VARCHAR(100)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_vehiculos;
CREATE TABLE limp_vehiculos (
    id INT PRIMARY KEY,
    matricula VARCHAR(50) NOT NULL UNIQUE,
    marca_modelo VARCHAR(150),
    año_fabricacion YEAR,
    capacidad_carga_kg DECIMAL(10,2),
    f_ultima_itv DATE,
    estado_vehiculo VARCHAR(30),
    num_bastidor_vin VARCHAR(100),
    coordenadas_gps VARCHAR(100)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_clientes;
CREATE TABLE limp_clientes (
    id INT PRIMARY KEY,
    cif_nif VARCHAR(50) NOT NULL UNIQUE,
    razon_social VARCHAR(200) NOT NULL,
    direccion_fiscal TEXT,
    cp_postal VARCHAR(20),
    email_facturacion VARCHAR(150),
    tipo_cliente VARCHAR(50),
    limite_credito DECIMAL(12,2),
    fecha_alta_cliente DATE,
    activo TINYINT(1) DEFAULT 1
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_empleados;
CREATE TABLE limp_empleados (
    id INT PRIMARY KEY,
    nif_nie VARCHAR(50) NOT NULL UNIQUE,
    nombre_completo VARCHAR(200) NOT NULL,
    email_corp VARCHAR(150),
    f_alta DATE,
    puesto_rol VARCHAR(50),
    salario_base DECIMAL(10,2),
    num_ss VARCHAR(50),
    almacen_id INT,
    seguro_medico VARCHAR(50),
    activo TINYINT(1) DEFAULT 1,
    FOREIGN KEY (almacen_id) REFERENCES limp_almacenes(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_envios;
CREATE TABLE limp_envios (
    id INT PRIMARY KEY,
    tracking_number VARCHAR(100) NOT NULL UNIQUE,
    cliente_id INT NOT NULL,
    vehiculo_id INT,
    empleado_id INT,
    f_salida DATE,
    f_llegada_prevista DATE,
    f_entrega_real DATE,
    peso_kg_bruto DECIMAL(10,2),
    volumen_m3 DECIMAL(10,2),
    importe_envio DECIMAL(10,2),
    seguro_contratado VARCHAR(50),
    estado_envio VARCHAR(50),
    almacen_destino_id INT,
    prioridad VARCHAR(20),
    ruta_origen_ciudad VARCHAR(100),
    ruta_destino_ciudad VARCHAR(100),
    ruta_distancia_km DECIMAL(10,2),
    ruta_peajes_estimados DECIMAL(10,2),
    ruta_tiempo_estimado_h DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES limp_clientes(id),
    FOREIGN KEY (vehiculo_id) REFERENCES limp_vehiculos(id),
    FOREIGN KEY (empleado_id) REFERENCES limp_empleados(id),
    FOREIGN KEY (almacen_destino_id) REFERENCES limp_almacenes(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_incidencias;
CREATE TABLE limp_incidencias (
    id INT PRIMARY KEY,
    envio_id INT NOT NULL,
    f_incidencia DATE,
    descripcion_breve TEXT,
    coste_asociado DECIMAL(10,2),
    responsable_id INT,
    estado_resolucion VARCHAR(50),
    tipo_incidencia VARCHAR(50),
    FOREIGN KEY (envio_id) REFERENCES limp_envios(id),
    FOREIGN KEY (responsable_id) REFERENCES limp_empleados(id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_proveedores;
CREATE TABLE limp_proveedores (
    id INT PRIMARY KEY,
    cif_prov VARCHAR(50) NOT NULL UNIQUE,
    nombre_comercial VARCHAR(150) NOT NULL,
    tipo_suministro VARCHAR(100),
    tel_emergencias VARCHAR(50),
    email_prov VARCHAR(150),
    condiciones_pago VARCHAR(100),
    valoracion_estrellas TINYINT,
    ultimo_pedido DATE
) ENGINE=InnoDB;

DROP TABLE IF EXISTS limp_mantenimientos;
CREATE TABLE limp_mantenimientos (
    id INT PRIMARY KEY,
    vehiculo_id INT NOT NULL,
    f_mantenimiento DATE,
    taller_nombre VARCHAR(150),
    coste_reparacion DECIMAL(10,2),
    piezas_reemplazadas TEXT,
    proxima_revision_estimada DATE,
    FOREIGN KEY (vehiculo_id) REFERENCES limp_vehiculos(id)
) ENGINE=InnoDB;

SELECT '>>> FASE 12: Tablas limpias creadas' AS Progreso;

-- ============================================================
-- FASE 13: CARGA DE DATOS A TABLAS LIMPIAS
-- ============================================================

INSERT INTO limp_almacenes 
SELECT id, cod_almacen, nombre_sucursal, ciudad_ubicacion, 
       capacidad_m3, tel_contacto, tipo_gestion, ubicacion_geografica
FROM stg_almacenes;

INSERT INTO limp_vehiculos
SELECT id, matricula, marca_modelo, año_fabricacion, capacidad_carga_kg,
       f_ultima_itv, estado_vehiculo, num_bastidor_vin, coordenadas_gps
FROM stg_vehiculos;

INSERT INTO limp_clientes
SELECT id, cif_nif, razon_social, direccion_fiscal, cp_postal, 
       email_facturacion, tipo_cliente, limite_credito_sucio, 
       fecha_alta_cliente, 
       CASE WHEN activo = '1' THEN 1 ELSE 0 END
FROM stg_clientes;

INSERT INTO limp_empleados
SELECT id, nif_nie, nombre_completo, email_corp, f_alta, puesto_rol,
       salario_base_sucio, num_ss, almacen_id, seguro_medico,
       CASE WHEN activo_boolean = '1' THEN 1 ELSE 0 END
FROM stg_empleados;

INSERT INTO limp_envios
SELECT id, tracking_number, cliente_id, vehiculo_id, empleado_id,
       f_salida, f_llegada_prevista, f_entrega_real, peso_kg_bruto,
       volumen_m3, importe_envio, seguro_contratado, estado_envio,
       almacen_destino_id, prioridad, ruta_origen_ciudad, ruta_destino_ciudad,
       ruta_distancia_km, ruta_peajes_estimados, ruta_tiempo_estimado_h
FROM stg_envios;

INSERT INTO limp_incidencias
SELECT id, envio_id, f_incidencia, descripcion_breve, 
       coste_asociado_sucio, responsable_id, estado_resolucion, tipo_incidencia
FROM stg_incidencias;

INSERT INTO limp_proveedores
SELECT id, cif_prov, nombre_comercial, tipo_suministro, tel_emergencias,
       email_prov, condiciones_pago, valoracion_estrellas, ultimo_pedido
FROM stg_proveedores;

INSERT INTO limp_mantenimientos
SELECT id, vehiculo_id, f_mantenimiento, taller_nombre, coste_reparacion,
       piezas_reemplazadas, proxima_revision_estimada
FROM stg_mantenimientos;

SELECT '>>> FASE 13: Datos cargados en tablas limpias' AS Progreso;

-- ============================================================
-- FASE 14: RESUMEN ESTADÍSTICO
-- ============================================================

SELECT '=== RESUMEN DE REGISTROS ===' AS '';
SELECT 'Almacenes' AS tabla, COUNT(*) AS registros FROM limp_almacenes
UNION ALL SELECT 'Vehículos', COUNT(*) FROM limp_vehiculos
UNION ALL SELECT 'Clientes', COUNT(*) FROM limp_clientes
UNION ALL SELECT 'Empleados', COUNT(*) FROM limp_empleados
UNION ALL SELECT 'Envíos', COUNT(*) FROM limp_envios
UNION ALL SELECT 'Incidencias', COUNT(*) FROM limp_incidencias
UNION ALL SELECT 'Proveedores', COUNT(*) FROM limp_proveedores
UNION ALL SELECT 'Mantenimientos', COUNT(*) FROM limp_mantenimientos;

SELECT '>>> LIMPIEZA COMPLETADA ===' AS Estado;

-- ============================================================
-- RESTAURAR CONFIGURACIONES DE SEGURIDAD
-- ============================================================
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;
