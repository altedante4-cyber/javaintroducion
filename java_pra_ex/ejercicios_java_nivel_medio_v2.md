# Ejercicios de Programación Java - Nivel Intermedio

**Profesor:** [Nombre del Profesor]  
**Asignatura:** Programación Orientada a Objetos  
**Duración:** 90 minutos

---

## INSTRUCCIONES GENERALES

- Lea cuidadosamente cada enunciado antes de resolver.
- Cada ejercicio tiene un valor de 10 puntos (total 100 puntos).
- Se permite usar cualquier estructura de datos vista en clase.
- Justifique sus respuestas con comentarios en el código.
- Los输出的 esperados son modelos de referencia; su código debe producir resultados similares.

---

## EJERCICIO 1: Gestión de Tienda Online con ArrayList (10 puntos)

### Enunciado

Una tienda online necesita gestionar productos en un carrito de compras. Cada producto tiene:
- Código (String)
- Nombre (String)
- Precio (double)
- Cantidad (int)

**Se pide:**
1. Crear una clase `Producto` con los atributos mencionados y constructores get/set.
2. Implementar una clase `CarritoCompras` que contenga un `ArrayList<Producto>`.
3. La clase debe permitir:
   - Agregar producto al carrito
   - Calcular el total de la compra
   - Aplicar descuento porcentual al total
   - Mostrar el contenido del carrito

**Salida esperada:**
```
=== CARRITO DE COMPRAS ===

1. Agregando productos al carrito:
   ✓ Laptop - $999.99 x 2 unidades
   ✓ Mouse - $25.50 x 3 unidades
   ✓ Teclado - $45.00 x 1 unidad

2. Total sin descuento: $2,140.48

3. Aplicando descuento del 15%...
   ✓ Descuento aplicado: $321.07
   → TOTAL A PAGAR: $1,819.41
```

---

## EJERCICIO 2: Sistema de Envío de Paquetes con HashMap (10 puntos)

### Enunciado

Una empresa de mensajería necesita rastrear paquetes. Cada paquete tiene:
- ID de seguimiento (String, clave única)
- Destinatario (String)
- Peso en kg (double)
- Estado (String: "En tránsito", "Entregado", "Pendiente")

**Se pide:**
1. Crear la clase `Paquete` con los atributos correspondientes.
2. Implementar una clase `Mensajeria` que use `HashMap<String, Paquete>`.
3. La clase debe permitir:
   - Registrar un paquete nuevo
   - Cambiar el estado de un paquete
   - Listar paquetes por estado
   - Calcular el peso total de todos los paquetes

**Salida esperada:**
```
=== SISTEMA DE MENSAJERÍA ===

1. Registrando paquetes:
   ✓ PKG001 → Juan Pérez - 2.5 kg - En tránsito
   ✓ PKG002 → María López - 1.2 kg - Pendiente
   ✓ PKG003 → Carlos Ruiz - 5.0 kg - Entregado

2. Cambiando estado de PKG002 a "En tránsito":
   ✓ Estado actualizado

3. Paquetes en tránsito:
   → PKG001: Juan Pérez (2.5 kg)
   → PKG002: María López (1.2 kg)

4. Peso total de todos los paquetes: 8.7 kg
```

---

## EJERCICIO 3: Gestión de Playlist Musical con HashSet (10 puntos)

### Enunciado

Desarrollar un programa que gestione una playlist de música. Cada canción tiene:
- Título (String)
- Artista (String)
- Duración en segundos (int)

**Se pide:**
1. Crear una clase `Cancion` que contenga título, artista y duración.
2. Implementar una clase `Playlist` que gestione un `HashSet<Cancion>`.
3. Funcionalidades requeridas:
   - Agregar canciones (sin duplicados por título)
   - Buscar canciones por artista
   - Calcular la duración total de la playlist
   - Mostrar todas las canciones ordenadas por duración

**Consideraciones:**
- Usar HashSet para evitar canciones duplicadas
- Implementar equals() y hashCode() correctamente

**Salida esperada:**
```
=== PLAYLIST MUSICAL ===

1. Agregando canciones:
   ✓ "Bohemian Rhapsody" - Queen (354 seg)
   ✓ "Stairway to Heaven" - Led Zeppelin (482 seg)
   ✓ "Hotel California" - Eagles (391 seg)

2. Canciones de Queen:
   → Bohemian Rhapsody (354 seg)

3. Duración total de la playlist: 1,227 seg (20 min 27 seg)

4. Playlist ordenada por duración:
   → Bohemian Rhapsody - Queen (354 seg)
   → Hotel California - Eagles (391 seg)
   → Stairway to Heaven - Led Zeppelin (482 seg)
```

---

## EJERCICIO 4: Sistema de Reservas de Hotel con Herencia (10 puntos)

### Enunciado

Un hotel tiene diferentes tipos de habitaciones. Se requiere implementar:

1. **Clase base `Habitacion`:**
   - Número de habitación (String)
   - Precio por noche (double)
   - Boolean disponible

2. **Clases derivadas:**
   - `HabitacionEstandar`: número de camas (int)
   - `HabitacionSuite`: tiene jacuzzi (boolean), precio adicional por servicios
   - `HabitacionDeluxe`: vista al mar (boolean), precio adicional

3. Método abstracto `calcularPrecioTotal(int noches)` en la clase base.

4. Una clase `Hotel` que contenga un `ArrayList<Habitacion>` y permita:
   - Listar habitaciones disponibles
   - Reservar una habitación
   - Calcular ingresos totales por reservas

**Salida esperada:**
```
=== SISTEMA DE RESERVAS DE HOTEL ===

1. Habitaciones disponibles:
   → [Estándar] Hab. 101 - 2 camas - $80/noche
   → [Suite] Hab. 201 - Jacuzzi sí - $150/noche
   → [Deluxe] Hab. 301 - Vista al mar - $200/noche

2. Reservando Suite 201 por 3 noches:
   ✓ Reserva exitosa
   → Total: $450 (incluye servicio)

3. Reservando Estándar 101 por 2 noches:
   ✓ Reserva exitosa
   → Total: $160

4. Ingresos totales por reservas: $610
```

---

## EJERCICIO 5: Figuras Geométricas 3D con Polimorfismo (10 puntos)

### Enunciado

Diseñar un sistema de figuras geométricas tridimensionales:

1. **Clase abstracta `Figura3D`:**
   - Atributo: nombre (String)
   - Métodos abstractos: `calcularVolumen()` y `calcularAreaSuperficial()`

2. **Clases concretas:**
   - `Esfera`: radio (double)
   - `Cubo`: lado (double)
   - `Cilindro`: radio y altura (double)

3. Crear una clase `Deposito` con un `ArrayList<Figura3D>` que:
   - Agregue figuras de diferentes tipos
   - Calcule el volumen total
   - Muestre la información usando polimorfismo

**Salida esperada:**
```
=== DEPÓSITO DE FIGURAS 3D ===

1. Figuras almacenadas:
   ┌─────────────────────────────────────────┐
   │ Esfera "Bola de demolición"            │
   │   Radio: 3.0                            │
   │   Volumen: 113.10 u³                    │
   │   Área superficial: 113.10 u²           │
   ├─────────────────────────────────────────┤
   │ Cubo "Caja de almacenamiento"           │
   │   Lado: 5.0                             │
   │   Volumen: 125.00 u³                    │
   │   Área superficial: 150.00 u²           │
   ├─────────────────────────────────────────┤
   │ Cilindro "Tanque de agua"              │
   │   Radio: 2.0 | Altura: 8.0              │
   │   Volumen: 100.53 u³                    │
   │   Área superficial: 125.66 u²           │
   └─────────────────────────────────────────┘

2. === VOLUMEN TOTAL: 338.63 u³ ===
```

---

## EJERCICIO 6: Clases Abstractas - Sistema de Cuentas Bancarias (10 puntos)

### Enunciado

Implementar un sistema bancario utilizando clases abstractas:

1. **Clase abstracta `CuentaBancaria`:**
   - Número de cuenta (String)
   - Titular (String)
   - Saldo (double)
   - Método abstracto: `calcularInteres()`
   - Método abstracto: `getTipo()`

2. **Clases derivadas:**
   - `CuentaAhorro`: tiene tasa de interés (double)
   - `CuentaCorriente`: tiene límite de sobregiro (double)
   - `PlazoFijo`: tiene duración en meses y tasa especial

3. Una clase `Banco` que gestione un ArrayList y calcule:
   - Total de intereses generados
   - Cuenta con mayor saldo

**Salida esperada:**
```
=== SISTEMA BANCARIO ===

1. Cuentas registradas:
   ✓ CA-001: Juan Pérez - Ahorro - Saldo: $5,000
   ✓ CC-001: María López - Corriente - Saldo: $3,000 (Sobregiro: $500)
   ✓ PF-001: Carlos Ruiz - Plazo Fijo 12 meses - Saldo: $10,000

2. Intereses generados:
   → Cuenta Ahorro CA-001: $250 (5%)
   → Cuenta Corriente CC-001: $30 (1%)
   → Plazo Fijo PF-001: $1,200 (12%)
   === TOTAL INTERESES: $1,480 ===

3. Cuenta con mayor saldo:
   → PF-001 - Carlos Ruiz - $10,000
```

---

## EJERCICIO 7: Arrays y Wrappers - Sistema de Temperaturas (10 puntos)

### Enunciado

Desarrollar un programa para analizar datos de temperatura:

1. Crear una clase `RegistroTemperatura` con:
   - Ciudad (String)
   - Temperaturas diarias (Array de Double[] - 7 días)
   - Usar tipos wrapper (Double) para las temperaturas

2. Crear una clase `Clima` que gestione:
   - Un array de `RegistroTemperatura[]` (tamaño fijo de 5 ciudades)
   - Un método para calcular el promedio de cada ciudad
   - Un método para encontrar la ciudad más caliente
   - Un método para encontrar la temperatura más baja registrada

**Consideraciones:**
- Usar tipos wrapper (Double) en lugar de double primitivo
- Manejar valores nulos en el array

**Salida esperada:**
```
=== SISTEMA DE ANÁLISIS DE CLIMA ===

1. Registro de temperaturas (7 días):
   Ciudad: Nueva York
   → [18.5, 20.1, 19.8, 22.0, 21.5, 23.0, 20.5] °C
   → Promedio: 20.77 °C

   Ciudad: Los Ángeles
   → [25.0, 26.5, 28.0, 27.2, 29.1, 30.0, 28.5] °C
   → Promedio: 27.76 °C

2. Ciudad más caliente (promedio):
   → Los Ángeles: 27.76 °C

3. Temperatura más baja registrada:
   → 18.5 °C en Nueva York (día 1)
```

---

## EJERCICIO 8: HashMap Avanzado - Sistema de multicitaciones (10 puntos)

### Enunciado

Implementar un sistema de votación para un concurso:

1. **Clase `Candidato`:**
   - Nombre (String)
   - Partido (String)
   - Votos (Integer - wrapper)

2. **Clase `SistemaVotacion`:**
   - Usar `HashMap<String, Candidato>` donde la clave es el nombre
   - Usar `HashMap<String, Integer>` para contar votos por partido

3. Funcionalidades:
   - Registrar candidato
   - Emitir voto por candidato
   - Mostrar resultados ordenado por votos
   - Determinar ganador

**Salida esperada:**
```
=== SISTEMA DE VOTACIÓN ===

1. Candidatos registrados:
   ✓ Ana López - Partido Verde
   ✓ Juan García - Partido Azul
   ✓ María Pérez - Partido Rojo

2. Resultados de la votación:
   ┌─────────────────────────────────────────┐
   │ 1° lugar: Ana López (Partido Verde)    │
   │            Votos: 1500                   │
   ├─────────────────────────────────────────┤
   │ 2° lugar: Juan García (Partido Azul)   │
   │            Votos: 1200                   │
   ├─────────────────────────────────────────┤
   │ 3° lugar: María Pérez (Partido Rojo)    │
   │            Votos: 800                   │
   └─────────────────────────────────────────┘

3. Votos por partido:
   → Verde: 1500
   → Azul: 1200
   → Rojo: 800
   === TOTAL: 3,500 votos ===

4. Ganador: Ana López con 1,500 votos
```

---

## EJERCICIO 9: Herencia y Polimorfismo - Restaurante (10 puntos)

### Enunciado

Crear un sistema de pedidos para un restaurante:

1. **Clase abstracta `ProductoMenu`:**
   - Nombre (String)
   - Precio base (double)
   - Método abstracto: `calcularPrecio()`
   - Método abstracto: `getCategoria()`

2. **Clases derivadas:**
   - `Bebida`: tiene tamaño (String: "pequeño", "mediano", "grande")
   - `PlatoPrincipal`: tiene precio de ingredientes (double)
   - `Postre`: tiene cantidad de azúcar (double), precio adicional

3. **Interfaz `Descuento`:**
   - Método: `aplicarDescuento(double porcentaje)`
   - Implementada por PlatoPrincipal y Postre

4. Una clase `Pedido` con ArrayList que demuestre:
   - Polimorfismo en el cálculo de precios
   - Uso de instanceof y casting

**Salida esperada:**
```
=== SISTEMA DE PEDIDOS ===

1. Agregando productos al pedido:
   → [Bebida] Refresco - Grande - $3.50
   → [Plato] Hamburguesa - $12.00 (15% desc.)
   → [Postre] Flan - Azúcar: 20g - $4.50 (10% desc.)

2. Detalle del pedido (usando polimorfismo):
   → Bebida: Refresco - $3.50
   → Plato Principal: Hamburguesa - $10.20
   → Postre: Flan - $4.05
   === SUBTOTAL: $17.75 ===

3. Productos con descuento (instanceof + casting):
   → Hamburguesa: Descuento aplicado (-$1.80)
   → Flan: Descuento aplicado (-$0.45)
```

---

## EJERCICIO 10: Proyecto Integrador - Gimnasio (10 puntos)

### Enunciado

Desarrollar un sistema completo para un gimnasio:

**Estructura de clases:**

1. **Clase abstracta `Miembro`:**
   - Nombre (String)
   - ID (String)
   - Edad (Integer - wrapper)
   - Método abstracto: `calcularCuota()`
   - Método abstracto: `getTipo()`

2. **Clases derivadas:**
   - `MiembroBasic`: mensualidad básica (double)
   - `MiembroPremium`: tiene acceso a spa (boolean), descuento (double)
   - `MiembroFamiliar`: número de familiares adicionales (int), precio por familiar

3. **Gestión con múltiples colecciones:**
   - `ArrayList<Miembro>` para miembros activos
   - `HashMap<String, Miembro>` para búsqueda por ID
   - `HashSet<String>` para tipos de membresía únicos

4. **Funcionalidades:**
   - Agregar nuevo miembro
   - Buscar miembro por ID
   - Calcular ingresos mensuales totales
   - Contar miembros por tipo
   - Mostrar tipos de membresía disponibles

**Salida esperada:**
```
=== SISTEMA DE GIMNASIO ===

1. Miembros registrados:
   ✓ MB-001: Juan Pérez - Basic - $50/mes
   ✓ MP-001: María López - Premium (Spa: sí) - $100/mes
   ✓ MF-001: Familia García - Familiar (3 adicionales) - $120/mes

2. Buscando miembro MP-001:
   → María López - Premium - Spa: Sí - Cuota: $90 (10% desc.)

3. Ingresos mensuales totales:
   → Basic: $50
   → Premium: $90
   → Familiar: $120
   === TOTAL: $260 ===

4. Miembros por tipo:
   → Basic: 1
   → Premium: 1
   → Familiar: 1

5. Tipos de membresía disponibles:
   → {Basic, Premium, Familiar}
```

---

## CRITERIOS DE EVALUACIÓN

| Criterio | Puntuación |
|----------|------------|
| Compilación sin errores | 2 puntos |
| Uso correcto de estructuras de datos | 3 puntos |
| Implementación de POO (herencia, polimorfismo, abstracción) | 3 puntos |
| Funcionalidad correcta | 2 puntos |

---

**Nota importante:** La salida mostrada es un modelo de referencia. Su implementación puede variar en detalles de formato, pero debe cumplir con la funcionalidad solicitada.

**Fecha de entrega:** [Especificar fecha]  
**Forma de entrega:** Carpeta comprimida con código fuente y archivo README
