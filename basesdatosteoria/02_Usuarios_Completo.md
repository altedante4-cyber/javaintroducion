# Guía COMPLETA: Usuarios, Privilegios y Roles en Oracle

> **Objetivo:** Dominar este tema para sacar un 10 en el examen

---

## 1. USUARIOS: Concepto Fundamental

### ¿Qué es un usuario en Oracle?

Un **usuario** es una cuenta de seguridad que permite acceder a una base de datos Oracle. Cada usuario:
- Tiene un **nombre único** en la base de datos
- Puede tener una **contraseña** (autenticación)
- Puede tener **cuotas de espacio** en tablespaces
- Tiene **privilegios** que determinan qué puede hacer

### Diferencia entre USER y SCHEMA

| Concepto | Descripción |
|----------|-------------|
| **USER** | Cuenta de acceso a la BD (login) |
| **SCHEMA** | Colección de objetos (tablas, vistas, etc.) que pertenecen a un usuario |

> **Nota:** En Oracle, cada usuario tiene un esquema con el mismo nombre. Cuando creas un usuario, automáticamente se crea un esquema vacío con ese nombre.

---

## 2. CREAR USUARIOS (CREATE USER)

### Sintaxis Completa

```sql
CREATE USER nombre_usuario
IDENTIFIED BY contraseña
[DEFAULT TABLESPACE nombre_tablespace]
[QUOTA {tamaño [K|M|G] | UNLIMITED} ON nombre_tablespace]
[TEMPORARY TABLESPACE nombre_tablespace]
[PASSWORD EXPIRE]
[ACCOUNT {LOCK | UNLOCK}]
[PROFILE nombre_perfil];
```

### Parámetros Explicados

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `IDENTIFIED BY` | Define la contraseña del usuario | `IDENTIFIED BY "miPass123"` |
| `DEFAULT TABLESPACE` | Tablespace donde se almacenarán los objetos por defecto | `DEFAULT TABLESPACE USERS` |
| `QUOTA` | Espacio máximo que puede usar en el tablespace | `QUOTA 10M ON USERS` |
| `TEMPORARY TABLESPACE` | Tablespace para operaciones temporales (ordenaciones) | `TEMPORARY TABLESPACE TEMP` |
| `PASSWORD EXPIRE` | Fuerza al usuario a cambiar contraseña al primer login | `PASSWORD EXPIRE` |
| `ACCOUNT LOCK/UNLOCK` | Bloquea/desbloquea la cuenta | `ACCOUNT LOCK` |
| `PROFILE` | Perfil de recursos y políticas de contraseña | `PROFILE default` |

### Ejemplos Prácticos

**Ejemplo 1: Usuario básico**
```sql
CREATE USER julia IDENTIFIED BY "julia123";
```
> Solo crea el usuario. No puede hacer nada hasta que le den privilegios.

**Ejemplo 2: Usuario con espacio en disco**
```sql
CREATE USER programador 
IDENTIFIED BY "prog123" 
DEFAULT TABLESPACE USERS 
QUOTA 20M ON USERS;
```

**Ejemplo 3: Usuario completo (como en exámenes)**
```sql
CREATE USER adminbd 
IDENTIFIED BY "admin123" 
DEFAULT TABLESPACE USERS 
QUOTA 10M ON USERS
TEMPORARY TABLESPACE TEMP
PASSWORD EXPIRE
ACCOUNT UNLOCK;
```

### Error Común
Si intentas crear un usuario sin darle `CREATE SESSION`, NO podrá conectarse:
```sql
-- Esto no basta para que el usuario se conecte:
CREATE USER pepe IDENTIFIED BY "123";

-- Necesitas también:
GRANT CREATE SESSION TO pepe;
```

---

## 3. MODIFICAR USUARIOS (ALTER USER)

### Cambiar Contraseña
```sql
ALTER USER julia IDENTIFIED BY "nuevaPass456";
```

### Cambiar Quota (espacio)
```sql
ALTER USER programador QUOTA 50M ON USERS;
ALTER USER programador QUOTA UNLIMITED ON USERS;  -- Sin límite
```

### Cambiar Tablespace por defecto
```sql
ALTER USER programador DEFAULT TABLESPACE SYSTEM;
```

### Forzar cambio de contraseña
```sql
ALTER USER julia PASSWORD EXPIRE;
```

### Bloquear/Desbloquear cuenta
```sql
ALTER USER julia ACCOUNT LOCK;    -- Bloquea
ALTER USER julia ACCOUNT UNLOCK;  -- Desbloquea
```

---

## 4. ELIMINAR USUARIOS (DROP USER)

### Sintaxis
```sql
DROP USER nombre_usuario [CASCADE];
```

### Sin CASCADE
```sql
DROP USER julia;
```
> **Solo funciona** si el usuario NO tiene objetos (tablas, índices, etc.)

### Con CASCADE
```sql
DROP USER programador CASCADE;
```
> **Elimina al usuario Y todos sus objetos** (tablas, vistas, secuencias, etc.)
> ⚠️ **PELIGRO:** ¡Cuidado! Esto borra todos los datos.

---

## 5. PRIVILEGIOS: Tipos y Diferencias

### 5.1 Privilegios de Sistema vs Privilegios de Objeto

```
┌─────────────────────────────────────────────────────────────┐
│                    PRIVILEGIOS                              │
├─────────────────────────┬───────────────────────────────────┤
│   PRIVILEGIOS DE SISTEMA│     PRIVILEGIOS DE OBJETO        │
├─────────────────────────┼───────────────────────────────────┤
│  - CREATE SESSION       │  - SELECT                         │
│  - CREATE TABLE         │  - INSERT                         │
│  - CREATE VIEW          │  - UPDATE                         │
│  - CREATE USER          │  - DELETE                         │
│  - CREATE PROCEDURE     │  - REFERENCES                     │
│  - CREATE ROLE          │  - EXECUTE                        │
│  - etc.                 │  - etc.                           │
├─────────────────────────┼───────────────────────────────────┤
│  Afectan a TODA la BD  │  Afectan a OBJETOS específicos    │
└─────────────────────────┴───────────────────────────────────┘
```

### 5.2 Privilegios de Sistema (SYSTEM PRIVILEGES)

| Privilegio | ¿Qué permite? |
|------------|---------------|
| `CREATE SESSION` | Conectarse a la base de datos |
| `CREATE TABLE` | Crear tablas en tu propio esquema |
| `CREATE ANY TABLE` | Crear tablas en cualquier esquema |
| `CREATE VIEW` | Crear vistas |
| `CREATE PROCEDURE` | Crear procedimientos almacenados |
| `CREATE ROLE` | Crear roles |
| `CREATE USER` | Crear usuarios |
| `DROP ANY TABLE` | Eliminar tablas de cualquier esquema |
| `ALTER USER` | Modificar usuarios |
| `DROP USER` | Eliminar usuarios |

### 5.3 Privilegios de Objeto (OBJECT PRIVILEGES)

| Privilegio | ¿Qué permite en una tabla? | ¿Qué permite en un procedimiento? |
|------------|---------------------------|----------------------------------|
| `SELECT` | Consultar datos | - |
| `INSERT` | Insertar datos | - |
| `UPDATE` | Modificar datos | - |
| `DELETE` | Eliminar datos | - |
| `REFERENCES` | Crear claves foráneas | - |
| `EXECUTE` | - | Ejecutar el procedimiento |
| `ALL` | Todos los anteriores | Todos los anteriores |

---

## 6. CONCEDER PRIVILEGIOS (GRANT)

### 6.1 Conceder Privilegio de Sistema

```sql
GRANT privilegio TO usuario [WITH ADMIN OPTION];
GRANT privilegio1, privilegio2 TO usuario [WITH ADMIN OPTION];
```

**Ejemplos:**
```sql
-- Dar permiso para conectarse
GRANT CREATE SESSION TO julia;

-- Dar varios permisos
GRANT CREATE SESSION, CREATE TABLE TO julia;

-- Con WITH ADMIN OPTION (puede otorgar ese privilegio a otros)
GRANT CREATE TABLE TO julia WITH ADMIN OPTION;
```

> **WITH ADMIN OPTION:** El usuario puede conceder ese privilegio a otros usuarios y roles.

### 6.2 Conceder Privilegio de Objeto

```sql
GRANT privilegio ON objeto TO usuario [WITH GRANT OPTION];
GRANT privilegio1, privilegio2 ON objeto TO usuario;
GRANT ALL ON objeto TO usuario;
```

**Ejemplos:**
```sql
-- Permiso de lectura
GRANT SELECT ON empleados TO julia;

-- Permisos de lectura y modificación
GRANT SELECT, INSERT, UPDATE ON departamentos TO julia;

-- Todos los permisos
GRANT ALL ON empleados TO julia;

-- Con WITH GRANT OPTION (puede conceder ese privilegio a otros)
GRANT SELECT ON empleados TO julia WITH GRANT OPTION;
```

> **WITH GRANT OPTION:** El usuario puede conceder ese privilegio a otros usuarios y roles.

### 6.3 Diferencia CRITICAL: WITH GRANT OPTION vs WITH ADMIN OPTION

```
┌─────────────────────────────────────────────────────────────┐
│  WITH GRANT OPTION (para privilegios de OBJETO)            │
├─────────────────────────────────────────────────────────────┤
│  - Solo se aplica a privilegios de objeto (SELECT, INSERT) │
│  - El usuario puede conceder ese privilegio específico     │
│    a otros usuarios                                        │
│  - Ejemplo:                                                 │
│    GRANT SELECT ON tabla TO usuario WITH GRANT OPTION;     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  WITH ADMIN OPTION (para privilegios de SISTEMA)           │
├─────────────────────────────────────────────────────────────┤
│  - Solo se aplica a privilegios de sistema                  │
│  - El usuario puede conceder CUALQUIER privilegio de       │
│    sistema que tenga a otros usuarios                       │
│  - Ejemplo:                                                 │
│    GRANT CREATE TABLE TO usuario WITH ADMIN OPTION;        │
└─────────────────────────────────────────────────────────────┘
```

### 6.4 Conceder Roles

```sql
GRANT nombre_rol TO usuario [WITH ADMIN OPTION];
```

```sql
-- Asignar rol predefinido
GRANT CONNECT, RESOURCE TO julia;

-- Asignar rol personalizado
GRANT rol_consultor TO julia;
```

---

## 7. REVOCAR PRIVILEGIOS (REVOKE)

### 7.1 Revocar Privilegio de Objeto

```sql
REVOKE privilegio ON objeto FROM usuario;
REVOKE privilegio1, privilegio2 ON objeto FROM usuario;
REVOKE ALL ON objeto FROM usuario;
```

**Ejemplos:**
```sql
-- Quitar permiso de lectura
REVOKE SELECT ON empleados FROM julia;

-- Quitar todos los permisos
REVOKE ALL ON departamentos FROM julia;
```

### 7.2 Revocar Privilegio de Sistema

```sql
REVOKE privilegio FROM usuario;
REVOKE privilegio1, privilegio2 FROM usuario;
```

```sql
REVOKE CREATE TABLE FROM julia;
REVOKE CREATE SESSION, CREATE TABLE FROM julia;
```

### 7.3 Revocar Roles

```sql
REVOKE nombre_rol FROM usuario;
```

```sql
REVOKE CONNECT FROM julia;
REVOKE rol_consultor FROM julia;
```

### 7.4 Cómo funciona la revocación con GRANT OPTION

**Caso problemático:**
```
1. Admin concede: GRANT SELECT ON empleados TO A WITH GRANT OPTION
2. A concede:     GRANT SELECT ON empleados TO B
3. Admin revoca: REVOKE SELECT ON empleados FROM A
```

**Resultado:** También se le quita el acceso a B (y a cualquier otro al que A haya concedido el privilegio).

---

## 8. ROLES: Agrupación de Privilegios

### ¿Qué es un Rol?

Un **rol** es un grupo de privilegios que se asigna a usuarios. Es como un "perfil" o "cargo".

**Ventajas de usar roles:**
- Facilita la administración
- Un cambio en el rol afecta a todos los usuarios con ese rol
- Puedo crear roles como "DEPENDIENTE", "JEFE", "CONSULTOR", etc.

### 8.1 Crear un Rol

```sql
CREATE ROLE nombre_rol [NOT IDENTIFIED];
CREATE ROLE nombre_rol IDENTIFIED BY contraseña;
```

**Ejemplos:**
```sql
-- Rol sin contraseña
CREATE ROLE consultores;

-- Rol con contraseña
CREATE ROLE admins IDENTIFIED BY "adminpass";
```

### 8.2 Asignar Privilegios a un Rol

```sql
-- Privilegios de sistema
GRANT CREATE SESSION TO consultores;
GRANT CREATE TABLE TO consultores;

-- Privilegios de objeto
GRANT SELECT ON empleados TO consultores;
GRANT SELECT, INSERT ON departamentos TO consultores;
```

### 8.3 Asignar Rol a Usuario

```sql
GRANT consultores TO julia;
GRANT consultores TO pedro;
GRANT consultores TO maria;
```

### 8.4 Modificar un Rol

```sql
-- Cambiar contraseña
ALTER ROLE consultores IDENTIFIED BY "nuevaPass";

-- Quitar contraseña
ALTER ROLE consultores NOT IDENTIFIED;
```

### 8.5 Eliminar un Rol

```sql
DROP ROLE nombre_rol;
```

```sql
DROP ROLE consultores;
```

---

## 9. ROLES PREDEFINIDOS EN ORACLE

Oracle viene con roles predefinidos:

| Rol | Descripción |
|-----|-------------|
| `CONNECT` | Privilegios básicos para conectarse (CREATE SESSION) |
| `RESOURCE` | Privilegios para crear objetos (CREATE TABLE, PROCEDURE, etc.) |
| `DBA` | Administrador de base de datos (casi todos los privilegios) |
| `EXP_FULL_DATABASE` | Exportar base de datos completa |
| `IMP_FULL_DATABASE` | Importar base de datos completa |

**Ejemplo de uso:**
```sql
GRANT CONNECT, RESOURCE TO julia;
```

> **Nota:** En versiones modernas de Oracle, `CONNECT` y `RESOURCE` están obsoletos, pero siguen funcionando.

---

## 10. CONSULTAR PRIVILEGIOS (Vistas del Sistema)

En exámenes te pueden preguntar cómo ver qué tiene un usuario:

### ¿Qué privilegios de sistema tiene un usuario?
```sql
SELECT * FROM USER_SYS_PRIVS;        -- Privilegios del usuario actual
SELECT * FROM DBA_SYS_PRIVS;         -- Todos los privilegios (necesitas DBA)
SELECT * FROM USER_ROLE_PRIVS;       -- Roles del usuario actual
```

### ¿Qué privilegios de objeto tiene un usuario?
```sql
SELECT * FROM USER_TAB_PRIVS_MADE;   -- Privilegios que YO concedí a otros
SELECT * FROM USER_TAB_PRIVS_RECD;  -- Privilegios que me concedieron
```

### ¿Qué objetos tiene un usuario?
```sql
SELECT * FROM USER_OBJECTS;
```

---

## 11. EJERCICIOS COMPLETOS DE EXAMEN

### Ejercicio 1: Crear usuario básico
**Crear usuario "maria" con contraseña "mar123" y quota de 5MB en el tablespace USERS**

```sql
CREATE USER maria 
IDENTIFIED BY "mar123" 
DEFAULT TABLESPACE USERS 
QUOTA 5M ON USERS;
```

### Ejercicio 2: Dar permisos de conexión y creación
**Conceder a "maria" permisos para conectarse y crear tablas**

```sql
GRANT CREATE SESSION, CREATE TABLE TO maria;
```

### Ejercicio 3: Dar acceso a tablas existentes
**Conceder a "maria" permisos de SELECT e INSERT sobre la tabla "empleados"**

```sql
GRANT SELECT, INSERT ON empleados TO maria;
```

### Ejercicio 4: Crear rol personalizado
**Crear rol "lectura_total" con permisos de SELECT sobre "empleados" y "departamentos" y asignarlo a "maria"**

```sql
CREATE ROLE lectura_total;
GRANT SELECT ON empleados TO lectura_total;
GRANT SELECT ON departamentos TO lectura_total;
GRANT lectura_total TO maria;
```

### Ejercicio 5: Conceder con opción de cesión
**Conceder a "maria" permiso de SELECT sobre "empleados" de forma que pueda cedérselo a otros**

```sql
GRANT SELECT ON empleados TO maria WITH GRANT OPTION;
```

### Ejercicio 6: Revocar privilegio
**Revocar a "maria" el permiso de SELECT sobre "empleados"**

```sql
REVOKE SELECT ON empleados FROM maria;
```

### Ejercicio 7: Eliminar usuario con objetos
**Eliminar usuario "programador" que tiene tablas creadas**

```sql
DROP USER programador CASCADE;
```

### Ejercicio 8: Escenario completo
**Crear el siguiente esquema de usuarios:**
- Usuario "jefe" con contraseña "jefe123", quota 10MB
- Usuario "empleado" con contraseña "emp123", quota 5MB
- Rol "gestor_empleados" con SELECT, INSERT, UPDATE sobre tabla "personal"
- Asignar rol a "jefe" (con admin option) y "empleado"

```sql
-- Crear usuarios
CREATE USER jefe IDENTIFIED BY "jefe123" DEFAULT TABLESPACE USERS QUOTA 10M ON USERS;
CREATE USER empleado IDENTIFIED BY "emp123" DEFAULT TABLESPACE USERS QUOTA 5M ON USERS;

-- Darles conexión
GRANT CREATE SESSION TO jefe;
GRANT CREATE SESSION TO empleado;

-- Crear rol y darle privilegios
CREATE ROLE gestor_empleados;
GRANT SELECT, INSERT, UPDATE ON personal TO gestor_empleados;

-- Asignar rol
GRANT gestor_empleados TO jefe WITH ADMIN OPTION;
GRANT gestor_empleados TO empleado;
```

---

## 12. ERRORES FRECUENTES Y CÓMO EVITARLOS

| Error | Causa | Solución |
|-------|-------|----------|
| `ORA-01045: user X lacks CREATE SESSION privilege` | Usuario no tiene permiso de conexión | `GRANT CREATE SESSION TO usuario` |
| `ORA-01950: no privileges on tablespace 'USERS'` | Usuario no tiene quota | `ALTER USER usuario QUOTA 10M ON USERS` |
| `ORA-01031: insufficient privileges` | No tiene el privilegio necesario | Conceder el privilegio con GRANT |
| `ORA-01940: cannot drop a user that is currently connected` | Usuario está conectado | Desconectarlo primero o usar CASCADE |
| Confundir TO y FROM | Error de sintaxis | GRANT usa TO, REVOKE usa FROM |
| Confundir WITH GRANT OPTION y WITH ADMIN OPTION | No saber la diferencia | Recordar: objeto = GRANT, sistema = ADMIN |

---

## 13. RESUMEN RÁPIDO DE EXAMEN

```
CREAR USUARIO:
  CREATE USER nombre IDENTIFIED BY pass QUOTA X ON tablespace;

MODIFICAR USUARIO:
  ALTER USER nombre IDENTIFIED BY nueva_pass;
  ALTER USER nombre QUOTA X ON tablespace;

ELIMINAR USUARIO:
  DROP USER nombre;           -- Sin objetos
  DROP USER nombre CASCADE;   -- Con objetos

CONCEDER PRIVILEGIO DE SISTEMA:
  GRANT privilegio TO usuario [WITH ADMIN OPTION];

CONCEDER PRIVILEGIO DE OBJETO:
  GRANT privilegio ON objeto TO usuario [WITH GRANT OPTION];

REVOCAR PRIVILEGIO:
  REVOKE privilegio ON objeto FROM usuario;
  REVOKE privilegio FROM usuario;

CREAR ROL:
  CREATE ROLE nombre;

ASIGNAR PRIVILEGIOS A ROL:
  GRANT privilegio TO rol;

ASIGNAR ROL A USUARIO:
  GRANT rol TO usuario;

ELIMINAR ROL:
  DROP ROLE nombre;
```

---

## 14. PREGUNTAS DE EXAMEN TÍPICAS (Con Respuestas)

**P: ¿Qué comando usas para crear un usuario llamado "pepe" con contraseña "abc"?**
```sql
CREATE USER pepe IDENTIFIED BY "abc";
```

**P: ¿Qué privilegio necesita un usuario para poder conectarse a la BD?**
```sql
CREATE SESSION
```

**P: ¿Cuál es la diferencia entre WITH GRANT OPTION y WITH ADMIN OPTION?**
- `WITH GRANT OPTION`: Para privilegios de OBJETO, permite ceder ese mismo privilegio
- `WITH ADMIN OPTION`: Para privilegios de SISTEMA, permite ceder cualquier privilegio de sistema

**P: ¿Cómo das todos los permisos sobre una tabla a un usuario?**
```sql
GRANT ALL ON nombre_tabla TO usuario;
```

**P: ¿Qué haces para eliminar un usuario que tiene tablas?**
```sql
DROP USER nombre CASCADE;
```

**P: ¿Para qué sirve un rol?**
Para agrupar privilegios y asignarlos de una vez a varios usuarios.

**P: ¿Qué vistas puedes consultar para ver los privilegios de un usuario?**
- `USER_SYS_PRIVS` - Privilegios de sistema
- `USER_TAB_PRIVS_RECD` - Privilegios de objeto recibidos
- `USER_ROLE_PRIVS` - Roles asignados

---

¡Ya tienes todo lo necesario para sacar un 10! 🎉
