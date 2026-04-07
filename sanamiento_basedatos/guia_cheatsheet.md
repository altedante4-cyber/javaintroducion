# Cheat Sheet: Saneamiento de Bases de Datos

## 1. ESPACIOS EN TEXTO

### Eliminar espacios al inicio y final
```sql
UPDATE tabla SET campo = TRIM(campo);
-- '  texto  ' → 'texto'
```

### Reemplazar espacios múltiples por uno solo
```sql
UPDATE tabla SET campo = REGEXP_REPLACE(campo, ' {2,}', ' ');
-- 'texto   con  espacios' → 'texto con espacios'
```

### Combinar ambos
```sql
UPDATE tabla SET campo = TRIM(REGEXP_REPLACE(campo, ' {2,}', ' '));
```

---

## 2. MAYÚSCULAS Y MINÚSCULAS

### Emails siempre a minúsculas
```sql
UPDATE tabla SET email = LOWER(email);
-- 'Juan@EMAIL.COM' → 'juan@email.com'
```

### Nombres con primera letra mayúscula (Title Case)
```sql
UPDATE tabla SET nombre = CONCAT(
    UPPER(LEFT(nombre, 1)), 
    LOWER(SUBSTRING(nombre, 2))
);
-- 'MARIA GOMEZ' → 'Maria Gomez'
```

---

## 3. FORMATO DE PRECIOS (Coma → Punto)

### Convertir texto con coma decimal a número
```sql
UPDATE productos SET precio = REPLACE(precio, ',', '.');
-- '199,99' → 199.99 (como texto) → luego convertir a decimal
UPDATE productos SET precio = CAST(REPLACE(precio, ',', '.') AS DECIMAL(10,2));
```

---

## 4. FORMATO DE FECHAS

### Normalizar fechas de diferentes formatos
```sql
-- Si el formato es '2023/02/20', convertir a '2023-02-20'
UPDATE tabla SET fecha = REPLACE(fecha, '/', '-');
```

---

## 5. FORMATO DE TELÉFONOS

### Teléfonos españoles: agregar prefijo +34 y formatear
```sql
-- Agregar +34 si no lo tiene
UPDATE tabla SET telefono = CONCAT('+34 ', telefono) 
WHERE telefono NOT LIKE '+34%';

-- Eliminar guiones y agregar espacios
UPDATE tabla SET telefono = TRIM(
    REGEXP_REPLACE(
        REPLACE(REPLACE(telefono, '-', ' '), ' ', ' '), 
        ' {2,}', ' '
    )
);
-- '+34 600-111-222' → '+34 600 111 222'
```

---

## 6. VALIDACIÓN Y LIMPIEZA DE EMAILS

### Detectar emails con doble @
```sql
SELECT * FROM tabla WHERE email LIKE '%@%@%' OR email LIKE '%@@%';
-- Marcar como NULL o corregir
UPDATE tabla SET email = NULL WHERE email LIKE '%@%@%';
```

### Corregir comas en lugar de puntos en emails
```sql
UPDATE tabla SET email = REPLACE(email, ',', '.');
-- 'maria@gmail,com' → 'maria@gmail.com'
```

### Eliminar puntos dobles en emails
```sql
UPDATE tabla SET email = REPLACE(email, '..', '.');
-- 'email..@domain.com' → 'email.@domain.com' (还需处理)
```

---

## 7. FORMATO IBAN

### Normalizar IBAN: mayúsculas y espacios cada 4 dígitos
```sql
-- Primero: quitar espacios y guiones, pasar a mayúsculas
UPDATE cuentas SET iban = REGEXP_REPLACE(iban, '[\\s-]', '');
UPDATE cuentas SET iban = UPPER(iban);

-- Segundo: agregar espacios cada 4 caracteres
UPDATE cuentas SET iban = INSERT(
    UPPER(TRIM(REGEXP_REPLACE(iban, '[\\s-]', ''))),
    5, 0, ' '
);

-- Más espacios si es necesario
UPDATE cuentas SET iban = CONCAT_WS(' ', 
    SUBSTRING(iban, 1, 4),
    SUBSTRING(iban, 5, 4),
    SUBSTRING(iban, 9, 4),
    SUBSTRING(iban, 13, 4),
    SUBSTRING(iban, 17, 4),
    SUBSTRING(iban, 21, 4)
);
```

### Validar longitud IBAN español (24 caracteres con espacios)
```sql
UPDATE cuentas SET iban = NULL WHERE LENGTH(REPLACE(iban, ' ', '')) != 24;
```

---

## 8. CATEGORÍAS: Title Case con tildes

```sql
UPDATE productos SET categoria = 'Informática' WHERE LOWER(categoria) = 'informatica';
UPDATE productos SET categoria = 'Periféricos' WHERE LOWER(categoria) = 'perifericos';
UPDATE productos SET categoria = 'Redes' WHERE LOWER(categoria) = 'redes';
```

---

## 9. PARSEO DE DATOS RAW (Importación)

### Datos con comillas y separadores mixtos
```sql
-- Para: '"PEDRO MARTINEZ"  "pedro@mail.com"  "+34 666-666-666"'
UPDATE import_temp SET linea_raw = REPLACE(linea_raw, '"', '');
-- Quitar comillas

UPDATE import_temp SET linea_raw = TRIM(linea_raw);
-- Limpiar espacios
```

### Detectar tipo de separador
```sql
-- Si contiene '|' usar pipe, si ',' usar coma, si espacios usar espacios
SELECT 
    CASE 
        WHEN linea_raw LIKE '%|%' THEN 'pipe'
        WHEN linea_raw LIKE '%,%' THEN 'coma'
        ELSE 'espacio'
    END AS tipo_separador
FROM import_temp;
```

---

## 10. NORMALIZACIÓN DE LOGS

### Corregir tildes faltantes
```sql
UPDATE logs SET mensaje = REPLACE(mensaje, 'sesion', 'sesión');
UPDATE logs SET mensaje = REPLACE(mensaje, 'conexion', 'conexión');
UPDATE logs SET mensaje = REPLACE(mensaje, 'Error de conexion', 'Error de conexión');
```

### Formatear excepciones técnicas
```sql
-- 'NULL pointer exception' → 'Null Pointer Exception'
UPDATE logs SET mensaje = CONCAT(
    UPPER(LEFT(mensaje, 1)),
    LOWER(SUBSTRING(mensaje, 2))
);
```

---

## 11. VALIDACIÓN Y LIMPIEZA FINAL

### Query para ver todos los problemas potenciales
```sql
SELECT 
    id,
    nombre,
    email,
    telefono,
    '¿Espacios en nombre?' AS verificacion
FROM clientes
WHERE nombre != TRIM(nombre) OR nombre LIKE '%  %';

SELECT * FROM clientes WHERE email NOT LIKE '%@%.%' OR email LIKE '%@%@%';
SELECT * FROM productos WHERE precio LIKE '%,%';
SELECT * FROM cuentas WHERE LENGTH(REPLACE(iban, ' ', '')) != 24;
```

---

## FLUJO DE TRABAJO RECOMENDADO

1. **Backup** → Siempre hacer backup antes de modificar
2. **Identificar** → SELECT para ver datos problemáticos
3. **Limpiar espacios** → TRIM y REGEXP_REPLACE
4. **Normalizar formatos** → Mayúsculas, fechas, precios
5. **Validar** → Verificar que los cambios son correctos
6. **Confirmar** → COMMIT o verificar resultados

---

## FUNCIONES ÚTILES MySQL

| Función | Uso |
|---------|-----|
| `TRIM()` | Elimina espacios inicio/fin |
| `LTRIM()` / `RTRIM()` | Elimina espacios izquierda/derecha |
| `UPPER()` | Convierte a mayúsculas |
| `LOWER()` | Convierte a minúsculas |
| `REPLACE()` | Reemplaza caracteres |
| `REGEXP_REPLACE()` | Reemplaza con regex |
| `CONCAT()` | Concatena strings |
| `SUBSTRING()` | Extrae parte de string |
| `LENGTH()` | Longitud del string |
| `LEFT()` / `RIGHT()` | Extrae caracteres izquierda/derecha |
| `CAST()` | Convierte tipos de datos |
| `IFNULL()` | Reemplaza NULL con valor |
| `CASE` | Condicionales en consultas |
