# Examen Model - Programación Orientada a Objetos

---

## Ejercicio A: Sistema de Biblioteca Digital

### Descripción

Implementar un sistema de gestión de biblioteca digital con préstamo de libros.

### Clase Libro

| Atributo | Tipo | Validación |
|----------|------|------------|
| isbn | String | Formato: "XXX-XXXXXXXXXX" (13 dígitos con guión) |
| título | String | No vacío |
| autor | String | No vacío |
| año_publicacion | Entero | Entre 1450 y año actual |
| género | String |枚举: "ficción", "no-ficción", "ciencia", "historia", "otro" |
| ejemplares | Entero | Mínimo 1 |

### Clase Lector

| Atributo | Tipo | Validación |
|----------|------|------------|
| dni | String | Formato: 8 dígitos + 1 letra |
| nombre | String | No vacío |
| email | String | Debe contener "@" |
| prestamos_activos | Lista | Máximo 3 libros |

### Clase Préstamo

- fecha_inicio: fecha del sistema
- fecha_fin: 14 días después (calculado)
- libro: referencia al Libro
- lector: referencia al Lector

### Reglas de Negocio

1. No se puede prestar si el lector tiene 3 préstamos activos
2. No se puede prestar si no hay ejemplares disponibles
3. Al prestar, decrementar ejemplares; al devolver, incrementar

### Métodos Requeridos

```
prestamo(libro, lector)
- Si éxito: "Préstamo realizado: 'El Quijote' a Juan García. Devolver antes del 25/03/2026"
- Si error: "Error: El lector tiene 3 préstamos activos" o "Error: No hay ejemplares disponibles"

devolucion(prestamo)
- Si éxito: "Devolución aceptada: 'El Quijote'"
- Si error: "Error: Préstamo no encontrado"

listar_prestamos_vencidos()
- Mostrar todos los préstamos cuya fecha_fin < fecha_actual

listar_ejemplares_disponibles()
- Mostrar libros con ejemplares > 0
```

---

## Ejercicio B: Sistema de Ventas con Herencia Múltiple

### Descripción

Sistema de ventas con diferentes tipos de productos y descuentos.

### Clase Producto (Abstracta)

- código: string único
- nombre: string
- precio_base: float > 0
- stock: entero >= 0

### Clase Electronica (hereda de Producto)

- garantía_meses: 12, 24 o 36
- marca: string

**Descuento por stock:**
- stock > 50: 15%
- stock > 20: 10%
- stock > 0: 5%
- stock == 0: 20%

### Clase Alimentacion (hereda de Producto)

- fecha_caducidad: date
- es_ecologico: boolean

**Descuento por proximidad:**
- caduca en 3+ días: 0%
- caduca en 1-2 días: 30%
- caduca hoy: 50%
- caduca ya: 70%

### Clase Ropa (hereda de Producto)

- talla: "XS", "S", "M", "L", "XL"
- temporada: "primavera", "verano", "otoño", "invierno"

**Descuento por temporada:**
- Temporada actual: 0%
- Temporada pasada: 25%
- Otra: 15%

### Clase Carrito

- productos: lista de (producto, cantidad)
- aplicar_descuentos(): calcula precio final con todos los descuentos

### Método: calcular_precio(producto, cantidad)

Debe aplicar el descuento correspondiente al tipo de producto.

### Ejemplo de Salida

```
Producto: Teléfono X2000 (Electrónica)
Precio base: 500.00€
Stock: 25 unidades
Descuento: 10%
Precio final: 450.00€

Producto: Leche Semidesnatada (Alimentación)
Precio base: 1.50€
Fecha caducidad: 15/03/2026 (hoy)
Descuento: 50%
Precio final: 0.75€

Total carrito: 450.75€
```

---

## Ejercicio C: Gestor de Excepciones Personalizadas

### Descripción

Sistema de empleados con manejo de errores personalizado.

### Excepciones Personalizadas (crear módulo exceptions.py)

```python
class EmpleadoError(Exception): pass
class DniInvalidoError(EmpleadoError): pass
class EmailInvalidoError(EmpleadoError): pass
class SalarioInvalidoError(EmpleadoError): pass
class DepartamentoError(EmpleadoError): pass
```

### Clase Empleado

- dni: string (validar formato)
- nombre: string
- email: string (validar formato)
- salario: float (entre 1100 y 10000)
- departamento: string

### Clase Departamento

- nombre: string único
- presupuesto: float
- empleados: lista

**Presupuesto dinámico:**
- Si empleados > 10: presupuesto * 0.95
- Si empleados > 20: presupuesto * 0.90

### Métodos con manejo de excepciones

```
alta_empleado(dni, nombre, email, salario, departamento)
- Lanzar DniInvalidoError si formato incorrecto
- Lanzar EmailInvalidoError si no contiene @
- Lanzar SalarioInvalidoError si fuera de rango
- Lanzar DepartamentoError si el departamento no existe
- Añadir al departamento y recalcular presupuesto

baja_empleado(dni)
- Si no existe: raise EmpleadoError("Empleado no encontrado")

trasladar_empleado(dni, nuevo_departamento)
- Validar ambos departamentos
- Calcular nueva distribución presupuestaria
```

### Restricciones

- Usar try/except en el programa principal
- Mostrar mensajes claros de error según el tipo de excepción

---

## Ejercicio D: Iteradores y Generadores

### Descripción

Sistema para gestionar una playlist musical con iteradores personalizados.

### Clase Cancion

- título: string
- artista: string
- duración_segundos: int (> 0)
- género: string

### Clase Playlist

- nombre: string
- canciones: lista

**Iterator personalizado:**
- Iterar por género
- Iterar por duración (canciones de más de X segundos)
- Iterar en orden aleatorio (shuffle sin modificar lista original)

### Generadores

```python
def reproduccion_circular(playlist):
    # Reproduce infinitamente en ciclo
    while True:
        for cancion in playlist.canciones:
            yield cancion

def buscar_por_artista(playlist, artista):
    for cancion in playlist.canciones:
        if cancion.artista.lower() == artista.lower():
            yield cancion
```

### Métodos Requeridos

```
iter() - Iterador por defecto (orden de inserción)
iter_por_genero(genero) - Generador filtrado
ordenar_por_duracion() - Devuelve lista ordenada
mezclar() - Devuelve iterador con orden aleatorio
```

### Ejemplo

```
Playlist: "Lo Mejor de los 80"
Canciones:
- Take On Me (a-ha) - 225s - Pop
- Sweet Child O' Mine (Guns N' Roses) - 356s - Rock
- Every Breath You Take (The Police) - 253s - Pop

# Iterar por Pop:
Take On Me - a-ha (3:45)
Every Breath You Take - The Police (4:13)

# Duración > 250s:
Sweet Child O' Mine - Guns N' Roses (5:56)
Every Breath You Take - The Police (4:13)
```

---

## Temas del Examen

- Clases, objetos y atributos
- Herencia simple y múltiple
- Clases abstractas
- Propiedades (@property, @setter)
- Excepciones personalizadas
- Iteradores y generadores
- Composición de objetos
- Validación de datos
- Métodos especiales (__str__, __eq__, etc.)
