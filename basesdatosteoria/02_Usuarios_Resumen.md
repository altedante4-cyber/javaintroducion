# Guía de Estudio: Usuarios y Privilegios en Bases de Datos

## 1. Concepto de Usuario

Un **usuario** es una entidad de seguridad que permite acceder a una base de datos. Cada usuario tiene:
- **Identificador** (nombre de usuario)
- **Contraseña** (opcional)
- **Privilegios** asignados

---

## 2. Tipos de Usuarios

| Tipo | Descripción |
|------|-------------|
| **Usuario final** | Persona que accede a la BD para consultar/actualizar datos |
| **Usuario de aplicación** | Programa que accede a la BD |
| **Usuario privilegiado** | Administrador con permisos de gestión |

---

## 3. Crear Usuario

```sql
CREATE USER usuario IDENTIFIED BY contraseña;
CREATE USER usuario IDENTIFIED BY contraseña DEFAULT TABLESPACE tablespace;
CREATE USER usuario IDENTIFIED BY contraseña QUOTA 10M ON tablespace;
```

**Ejemplo completo:**
```sql
CREATE USER pepo IDENTIFIED BY "1234" 
DEFAULT TABLESPACE users 
QUOTA 5M ON users;
```

---

## 4. Modificar Usuario

```sql
ALTER USER usuario IDENTIFIED BY nueva_contraseña;
ALTER USER usuario QUOTA 10M ON tablespace;
ALTER USER usuario DEFAULT TABLESPACE tablespace;
```

---

## 5. Eliminar Usuario

```sql
DROP USER usuario;              -- Si no tiene objetos
DROP USER usuario CASCADE;      -- Si tiene objetos (los elimina)
```

---

## 6. Privilegios

### 6.1 Tipos de Privilegios

| Tipo | Descripción |
|------|-------------|
| **Objetos** | Acceso a objetos específicos (SELECT, INSERT, UPDATE, DELETE en tablas/vistas) |
| **Sistema** | Operaciones generales (CREATE SESSION, CREATE TABLE, CREATE USER, etc.) |

### 6.2 Conceder Privilegios (GRANT)

**Privilegios de objeto:**
```sql
GRANT privilegios ON objeto TO usuario [WITH GRANT OPTION];

-- Ejemplos:
GRANT SELECT ON empleados TO pepo;
GRANT INSERT, UPDATE ON departamentos TO pepo;
GRANT ALL ON empleados TO pepo;
```

**Privilegios de sistema:**
```sql
GRANT privilegios TO usuario [WITH ADMIN OPTION];

-- Ejemplos:
GRANT CREATE SESSION TO pepo;
GRANT CREATE TABLE TO pepo;
GRANT CREATE USER TO pepo;
GRANT CONNECT, RESOURCE TO pepo;  -- Roles predefinidos
```

> **WITH GRANT OPTION:** Permite al usuario conceder ese privilegio a otros  
> **WITH ADMIN OPTion:** Permite al usuario conceder privilegios de sistema a otros

### 6.3 Revocar Privilegios (REVOKE)

```sql
REVOKE privilegios ON objeto FROM usuario;
REVOKE privilegios FROM usuario;

-- Ejemplos:
REVOKE SELECT ON empleados FROM pepo;
REVOKE CONNECT, RESOURCE FROM pepo;
```

---

## 7. Roles

Un **rol** es un grupo de privilegios que se asigna a usuarios.

### 7.1 Crear Rol
```sql
CREATE ROLE nombre_rol;
CREATE ROLE nombre_rol NOT IDENTIFIED;  -- Sin contraseña
CREATE ROLE nombre_rol IDENTIFIED BY contraseña;
```

### 7.2 Asignar Privilegios a un Rol
```sql
GRANT privilegio TO rol;
GRANT SELECT ON empleados TO rol_lectura;
GRANT CREATE TABLE TO rol_desarrollador;
```

### 7.3 Asignar Rol a Usuario
```sql
GRANT rol TO usuario;
GRANT rol_lectura TO pepo;
```

### 7.4 Eliminar Rol
```sql
DROP ROLE nombre_rol;
```

---

## 8. Resumen de Comandos

| Operación | Comando |
|-----------|---------|
| Crear usuario | `CREATE USER u IDENTIFIED BY p` |
| Modificar usuario | `ALTER USER u IDENTIFIED BY p` |
| Eliminar usuario | `DROP USER u [CASCADE]` |
| Conceder privilegio | `GRANT priv TO u [WITH GRANT OPTION]` |
| Revocar privilegio | `REVOKE priv FROM u` |
| Crear rol | `CREATE ROLE r` |
| Asignar rol | `GRANT r TO u` |
| Eliminar rol | `DROP ROLE r` |

---

## 9. Ejercicios Típicos de Examen

**Ejercicio 1:** Crear usuario "ana" con contraseña "abc" y quota de 10MB en USERS
```sql
CREATE USER ana IDENTIFIED BY abc QUOTA 10M ON users;
```

**Ejercicio 2:** Dar a "ana" permisos para conectarse y crear tablas
```sql
GRANT CREATE SESSION, CREATE TABLE TO ana;
```

**Ejercicio 3:** Dar a "ana" permiso de SELECT sobre la tabla "empleados"
```sql
GRANT SELECT ON empleados TO ana;
```

**Ejercicio 4:** Crear rol "consultor" con permisos de SELECT sobre "empleados" y "departamentos"
```sql
CREATE ROLE consultor;
GRANT SELECT ON empleados TO consultor;
GRANT SELECT ON departamentos TO consultor;
GRANT consultor TO ana;
```

**Ejercicio 5:** Revocar a "ana" el privilegio de SELECT sobre "empleados"
```sql
REVOKE SELECT ON empleados FROM ana;
```

---

## 10. Errores Comunes a Evitar

- Olvidar `CASCADE` al eliminar usuario con objetos
- Confundir `WITH GRANT OPTION` (para objetos) con `WITH ADMIN OPTION` (para sistema)
- No dar `CREATE SESSION` antes de otros privilegios
- Confundir `TO` con `FROM` en GRANT/REVOKE
