# Ejercicios Genéricos de Programación 25

## Instructor

José María Morales Vázquez

---

## Ejercicio 1: Juego de Pokémon

### Descripción

Implementar una clase para gestionar un juego de Pokemon con las siguientes características:

- **Atributos base**: código, nombre, tipos, peso y altura
- Cada pokemon puede ser de **un tipo** o de **dos tipos**. Nunca más
- En el constructor se facilitará:
  - Nombre
  - Código
  - Tipos
  - Dos valores para el peso (menor y mayor)
  - Dos valores para la altura (menor y mayor)
- El peso y la altura se generarán aleatoriamente entre los valores facilitados
- Implementar un método que permita ver todos los datos de un pokemon

### Clase Equipo

- Formar equipos de **tres pokemons**
- El equipo tendrá: **entrenador** y **nombre**
- Implementar un método para ver los datos del equipo

---

## Ejercicio 2: Gestión de Cuentas Corrientes

### Descripción

Programa en Python y POO para gestionar las cuentas corrientes de un banco.

### Clase Sucursal

- **Dirección**: una línea de texto
- **Provincia**
- **Código identificativo**: cuatro dígitos (los primeros pueden ser 0, ej: 0012)

### Clase Cliente

- **Nombre y apellidos**
- **NIF**
- **Teléfono**
- **Sucursal** donde se ha dado de alta inicialmente

### Clase CuentaCorriente

- **Código identificativo**: 12 dígitos (pueden empezar por ceros)
- **Saldo**
- **Titulares**: mínimo 1, máximo 2
- **Sucursal** donde se ha abierto la cuenta
- Un mismo cliente puede tener varias cuentas en la misma o diferentes sucursales

### IBAN

- El código completo será: `"ES68 1234"` + 4 dígitos de sucursal + 12 dígitos de cuenta
- **Importante**: El código inicial del banco debe estar en un único sitio, no repetido en cada objeto
- El IBAN es un dato calculado, no almacenado

### Métodos Requeridos

#### Listar cuentas de un cliente

```
José María Morales. Cliente de la sucursal 0055 (Madrid)
ES68 1234 0055 123456789012 – Saldo: 200.55€
ES68 1234 1234 987654321021 – Saldo 123.40€
ES68 1234 4444 112233445566 – Saldo 21.00€
Saldo total: 344.95€
```

#### Listar cuentas de una sucursal

```
Cuentas de la sucursal 4444 (Sevilla)
ES68 1234 4444 998877665544 – Saldo: 1201.45€
ES68 1234 4444 112233445566 – Saldo: 21.00€
Saldo total: 1222.45€
```

### Restricciones

- Solo tres clases: Sucursal, Cliente, CuentaCorriente
- Sin introducción de datos por teclado
- El IBAN NO debe almacenarse, debe calcularse en el momento de listarlo

---

## Ejercicio 3: Seguro de Vehículos

### Descripción

Programa en Python usando POO para calcular el precio anual de seguros de una compañía.

### Clase Conductor

- Nombre
- NIF
- Año de nacimiento
- Año en que se sacó el carnet
- Puntos del carnet

### Clase Vehiculo (Abstracta)

- Matrícula
- Año de venta
- Conductor asociado

### Clase Coche (hereda de Vehiculo)

#### Seguro a Todo Riesgo

| Antigüedad | Precio |
|------------|--------|
| 1er año | 400€ |
| 2do año | 500€ |
| 3er año | 700€ |
| 4+ años | 250€ × años de antigüedad |

- Se suman **100€** si el conductor tiene **menos de 8 puntos** en el carnet

#### Seguro a Terceros

- **Precio base**: 250€
- **Incrementos**:
  - +100€ si conductor tiene menos de 8 puntos
  - +50€ si conductor tiene menos de 24 años
  - +75€ si conductor tiene menos de 2 años de carnet

### Clase Moto (hereda de Vehiculo)

#### Seguro a Terceros

- **Precio base**: 200€
- **Incrementos**:
  - +150€ si conductor tiene menos de 8 puntos
  - +25€ si conductor tiene menos de 24 años
  - +50€ si conductor tiene menos de 2 años de carnet

#### Restricciones

- **NO** se hacen seguros a todo riesgo de motos

### Cálculos

- La antigüedad se calcula solo por año (sin meses)
- La edad se calcula solo por año
- El año actual se obtiene de forma automática del sistema

### Ejemplo 1

```
Vehículo: coche. Matrícula: 6310NXB. Año de compra: 2024
Conductor: José María Morales. Edad: 57. Años de carnet: 39 . Puntos: 10
Precio del seguro a todo riesgo: 500€
Precio del seguro a teceros: 250€
```

### Ejemplo 2

```
Vehículo: moto. Matrícula: 6309NXB. Año de compra: 2025
Conductor: Inés Perado. Edad: 18. Años de carnet: 1 . Puntos: 8
Precio del seguro a terceros: 275€
No se hacen seguros a todo riesgo a motos
```

---

## Ejercicio 4: Gestor de Tareas

### Descripción

Programa en Python mediante POO para gestionar una lista de tareas usando diccionarios.

### Datos de una Tarea

| Campo | Tipo | Descripción |
|-------|------|-------------|
| identificador | String | ID único de la tarea |
| título | String | Texto de la tarea |
| prioridad | Entero (1-9) | Nivel de prioridad |
| completada | Booleano | Si está realizada o no |

### Constructor

**Entrada:**
- identificador
- título
- prioridad

**Salida (éxito):**
```
Tarea 'Comprar billetes' (ID: P10) añadida.
```

**Salida (ID duplicado):**
```
Error: ID P10 ya existente
```

### Método: eliminarTarea(identificador)

**Salida (éxito):**
```
Tarea con ID P10 ('Comprar billetes') eliminada.
```

**Salida (no encontrado):**
```
Error: No se encontró una tarea con ID X1005.
```

### Método: marcarComoCompletada(identificador)

**Salida (éxito):**
```
Tarea ID D055 'Completar retos de Duolingo' marcada como completada.
```

**Salida (no encontrado):**
```
Error: No se encontró una tarea con ID W088
```

### Método: mostrarTareasCompletadas()

**Salida (con tareas):**
```
- LISTADO DE TAREAS:
[E25] Enviar email al jefe (Prioridad: 5)
[P33] Aprender Python (Prioridad: 2)
[F47] Revisar facturas (Prioridad: 7)
```

**Salida (sin tareas):**
```
- LISTADO DE TAREAS:
No hay tareas completadas.
```

### Método: mostrarTareasNoCompletadas()

**Salida (con tareas):** Mismo formato que mostrarTareasCompletadas

**Salida (sin tareas):**
```
- LISTADO DE TAREAS:
No hay tareas no completadas.
```

---

## Temas a Practicar

- Programación Orientada a Objetos (POO)
- Herencia y clases abstractas
- Composición de objetos
- Métodos estáticos y de clase
- Validación de datos
- Cálculos basados en fechas
