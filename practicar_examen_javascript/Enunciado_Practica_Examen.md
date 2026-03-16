# PRÁCTICA EXAMEN JAVASCRIPT - Comercial Nieves

## Empresa: Comercial Nieves C.A.

**Descripción del proyecto:**  
Crear una página web para una empresa dedicada a la compra y venta de cereales y granos como: chia, sésamo blanco, sésamo negro, soya, maní, maíz, entre otros.

---

## Requisitos técnicos obligatorios:

### 1. Estructura HTML
- Página principal con navegación (inicio, productos, contacto, nosotros)
- Formulario de contacto con los siguientes campos:
  - Nombre (requerido, solo letras)
  - Email (requerido, formato válido de email)
  - Teléfono (requerido, solo números, 10 dígitos)
  - Producto de interés (select con opciones de cereales)
  - Cantidad en kilogramos (number, mínimo 1)
  - Mensaje (textarea)
- Tabla de productos con información (nombre, precio, stock)
- Sección con array de productos (manipulación con JavaScript)

### 2. CSS (Estilos)
- Diseño responsive (adaptable a móviles)
- Paleta de colores relacionada con cereales/tierra (verdes, marrones, dorados)
- Estilos para formulario (inputs, botones, mensajes de error)
- Estilos para tabla de productos
- Animaciones simples en botones y elementos
- Menú de navegación

### 3. JavaScript (Funcionalidad)
- **Validación de formulario:**
  - Validar que campos requeridos no estén vacíos
  - Validar formato de email con expresión regular
  - Validar teléfono (solo números, cantidad exacta de dígitos)
  - Validar cantidad (número positivo mayor a 0)
  - Mostrar mensajes de error específicos
  - Prevenir envío si hay errores
  
- **Arrays y Funciones:**
  - Crear array con productos disponibles
  - Función para buscar producto por nombre
  - Función para filtrar productos por precio
  - Función para agregar productos al array
  - Función para calcular total de compra
  - Función random para mostrar "producto destacado" o "oferta del día"

- **DOM:**
  - Manipular elementos del DOM
  - Actualizar contenido dinámicamente
  - Manejar eventos (click, submit, change)

---

## Estructura de productos (ejemplo):

| Producto | Precio x Kg ($) | Stock (Kg) |
|----------|-----------------|------------|
| Chia | 8.50 | 500 |
| Sésamo Blanco | 6.00 | 300 |
| Sésamo Negro | 7.50 | 200 |
| Soya | 4.00 | 1000 |
| Maní | 5.50 | 400 |
| Maíz | 3.00 | 2000 |

---

## Restricciones:

1. **No usar librerías externas** (sin Bootstrap, jQuery, etc.)
2. **Todo el código JavaScript debe ser propio** (no copiar de internet)
3. **El código debe ser funcional** (nofake)
4. **Validaciones deben mostrar mensajes de error visibles** al usuario
5. **El diseño debe ser coherente** con el tema de cereales/granos

---

## Entregables:

1. Archivo HTML con estructura completa
2. Archivo CSS con estilos
3. Archivo JavaScript con todas las funcionalidades
4. Todo en archivos separados (no todo en un solo HTML)

---

## Evaluación:

- Validación de formulario: 30%
- Uso correcto de arrays y funciones: 30%
- Manipulación del DOM: 20%
- Diseño CSS y responsividad: 20%
