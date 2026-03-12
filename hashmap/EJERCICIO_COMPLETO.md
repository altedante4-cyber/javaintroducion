# Ejercicio Nivel Medio: Sistema de Gestión de Tienda Online

## Descripción del Ejercicio

Desarrollar un **sistema de gestión de una tienda online** que implemente conceptos avanzados de Programación Orientada a Objetos (POO), incluyendo herencia, polimorfismo, clases abstractas y colecciones de datos complejas.

---

## Requisitos del Sistema

### 1. Estructura de Clases y Herencia

Debes crear una jerarquía de clases que represente diferentes tipos de productos con características comunes y específicas.

```
Producto (Clase Abstracta)
├── ProductoFisico
├── ProductoDigital
└── ProductoServicio
```

### 2. Colecciones a Utilizar

El sistema debe usar las siguientes colecciones:

- **HashMap**: Almacenar productos por ID
- **HashSet**: Almacenar clientes únicos (sin duplicados)
- **ArrayList**: Almacenar items del carrito
- **Array normal**: Almacenar categorías fijas de productos

### 3. Características Requeridas

- Gestión de productos con polimorfismo
- Carrito de compras con descuentos
- Sistema de clientes
- Cálculo de precios con IVA
- Búsqueda y filtrado de productos

---

## Tareas a Realizar

### 1. Crea la clase abstracta **Producto**
- Atributos: `id`, `nombre`, `precio`, `categoria`
- Métodos abstractos: `calcularPrecioFinal()` y `obtenerDescripcion()`
- Implementa `toString()` y getters

### 2. Crea tres clases que hereden de **Producto**

**ProductoFisico:**
- Atributos adicionales: `peso` y `costoEnvio`
- `calcularPrecioFinal()`: Aplica IVA del 21% + costo de envío

**ProductoDigital:**
- Atributo adicional: `tamanoMB`
- `calcularPrecioFinal()`: Aplica IVA del 21% (sin costo de envío)

**ProductoServicio:**
- Atributo adicional: `duracionDias`
- `calcularPrecioFinal()`: Aplica IVA del 21% con descuento del 5%

### 3. Crea la clase **Cliente**
- Atributos: `id`, `nombre`, `email`
- Implementa `equals()` y `hashCode()` para evitar duplicados
- Sobrescribe `toString()`

### 4. Crea la clase **ItemCarrito**
- Atributos: `producto` (Producto) y `cantidad`
- Método: `calcularSubtotal()` que retorne precio final × cantidad

### 5. Crea la clase **TiendaOnline** con las siguientes características:

**Atributos:**
- `HashMap<Integer, Producto> productos` - almacena productos por ID
- `HashSet<Cliente> clientes` - almacena clientes únicos
- `ArrayList<ItemCarrito> carrito` - items del carrito
- `String[] categorias` - categorías fijas (Electrónica, Ropa, Software, Consultoría, Libros)

**Métodos requeridos:**
- `agregarProducto(Producto)` - añade producto al HashMap
- `obtenerProducto(int id)` - busca producto por ID
- `listarProductos()` - muestra todos los productos con su precio final
- `listarProductosPorCategoria(String categoria)` - filtra por categoría
- `registrarCliente(Cliente)` - añade cliente al HashSet (evita duplicados)
- `listarClientes()` - muestra todos los clientes
- `agregarAlCarrito(int idProducto, int cantidad)` - añade items al carrito
- `listarCarrito()` - muestra contenido del carrito
- `vaciarCarrito()` - limpia el carrito
- `calcularTotal()` - suma todos los subtotales
- `aplicarDescuento(double porcentaje)` - aplica descuento al total
- `mostrarCategorias()` - lista las categorías disponibles

### 6. Crea una clase **Main** que demuestre:
- Agregar 6 productos de diferentes tipos
- Registrar 3 clientes (incluyendo un intento de duplicate)
- Mostrar categorías disponibles
- Listar todos los productos
- Filtrar productos por categoría
- Agregar items al carrito
- Mostrar carrito completo con totales y descuentos

---

## Requisitos Adicionales

✅ Usa **polimorfismo** para que cada tipo de producto calcule precios diferente  
✅ Aplica **herencia** correctamente en la jerarquía de productos  
✅ Implementa **métodos abstractos** en la clase Producto  
✅ Usa **encapsulamiento** (atributos privados, getters públicos)  
✅ Demuestra el funcionamiento de cada colección en el programa principal  
✅ El código debe compilar y ejecutarse sin errores
