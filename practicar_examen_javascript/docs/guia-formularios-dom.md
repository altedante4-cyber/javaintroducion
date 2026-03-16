# Guía de Formularios y Manipulación DOM en JavaScript

## Elementos de Formulario: Valores por Defecto

### `<select>` - Combo box

```html
<select id="pais">
  <option value="">-- Selecciona --</option>
  <option value="es">España</option>
  <option value="mx">México</option>
</select>
```

| Escenario | Valor devuelto |
|-----------|----------------|
| Ninguna selección válida | `""` (string vacío) |
| Si el primer `<option>` no tiene `value=""` | Valor del primer `<option>` |
| Con selección | Valor del `<option>` seleccionado |

```javascript
const select = document.getElementById('pais');

// Obtener valor
select.value;  // "es"

// Obtener texto de la opción seleccionada
select.options[select.selectedIndex].text;  // "España"

// Verificar si hay selección válida
if (select.value === "") {
  console.log("No hay selección");
}
```

**Consejo**: Siempre incluir `<option value="">-- Selecciona --</option>` como primera opción.

### `<textarea>`

```javascript
const textarea = document.getElementById('comentario');

textarea.value;  // "" (string vacío si está vacío)
textarea.value.length;  // 0
```

**Importante**: Usar `.value`, NO `.innerHTML` (a diferencia de otros elementos).

---

## Acceso a Elementos del DOM

### Selección de Elementos (de más a menos eficiente)

```javascript
// ✅ MÁS EFICIENTE: Por ID (uso único)
document.getElementById('miId');

// ✅ FLEXIBLE: querySelector (un elemento)
document.querySelector('.miClase');
document.querySelector('#miId');
document.querySelector('div.contenedor .btn');

// ✅ TODOS: querySelectorAll (NodeList estático)
document.querySelectorAll('.items li');
```

### Propiedades de Navegación

```javascript
const elemento = document.querySelector('.miElemento');

// PADRES
elemento.parentElement;           // Elemento padre
elemento.parentNode;             // Nodo padre (incluye nodos de texto)

// HIJOS
elemento.children;                // HTMLCollection de elementos hijos
elemento.childNodes;             // Todos los nodos (incluye texto, comentarios)
elemento.firstElementChild;      // Primer hijo elemento
elemento.lastElementChild;       // Último hijo elemento
elemento.childElementCount;      // Cantidad de hijos elementos

// HERMANOS
elemento.nextElementSibling;     // Hermano siguiente
elemento.previousElementSibling; // Hermano anterior
elemento.nextSibling;           // Nodo siguiente (incluye texto)
elemento.previousSibling;        // Nodo anterior (incluye texto)
```

### Recorrer Hijos de un Select

```javascript
const select = document.getElementById('pais');

// Método 1: Iterar sobre options
for (let option of select.options) {
  console.log(option.value, option.text);
}

// Método 2: Array de valores
const valores = Array.from(select.options).map(opt => opt.value);
const textos = Array.from(select.options).map(opt => opt.text);

// Método 3: Obtener índice seleccionado
const indice = select.selectedIndex;
const opcionSeleccionada = select.options[indice];
```

---

## Mejores Prácticas

### 1. Cachear Elementos

```javascript
// ❌ MAL: Consultar el DOM repetidamente
function handleClick() {
  document.getElementById('btn').addEventListener('click', () => {
    document.getElementById('output').textContent = '...';
  });
}

// ✅ BIEN: Cachear referencias
const btn = document.getElementById('btn');
const output = document.getElementById('output');

btn.addEventListener('click', () => {
  output.textContent = '...';
});
```

### 2. Delegación de Eventos

```javascript
// ❌ MAL: Un listener por cada elemento
document.querySelectorAll('.item').forEach(item => {
  item.addEventListener('click', handleClick);
});

// ✅ BIEN: Un listener en el padre
document.getElementById('lista').addEventListener('click', (e) => {
  const item = e.target.closest('.item');
  if (item) {
    handleClick.call(item, e);
  }
});
```

### 3. closest() - Buscar Ancestros

```javascript
// Busca hacia arriba en el árbol hasta encontrar el selector
const boton = document.querySelector('.btn');
const card = boton.closest('.card');
const container = boton.closest('.container');
```

### 4. batch Updates con DocumentFragment

```javascript
// ❌ MAL: Múltiples reflows
const lista = document.getElementById('lista');
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item;
  lista.appendChild(li);
});

// ✅ BIEN: Un solo reflow
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item;
  fragment.appendChild(li);
});
lista.appendChild(fragment);
```

### 5. Usar classList en vez de className

```javascript
const elemento = document.querySelector('.box');

// ❌ MAL
elemento.className = 'box active';

// ✅ BIEN
elemento.classList.add('active');
elemento.classList.remove('active');
elemento.classList.toggle('active');
elemento.classList.contains('active'); // true/false
```

---

## Métodos Modernos de Inserción

```javascript
const nuevo = document.createElement('div');
nuevo.textContent = 'Hola';

// Antigua escuela
parent.appendChild(nuevo);

// Moderna
parent.append(nuevo);           // Añadir al final
parent.prepend(nuevo);         // Añadir al inicio
hermano.before(nuevo);         // Antes del elemento
hermano.after(nuevo);          // Después del elemento
hermano.replaceWith(nuevo);    // Reemplazar elemento

// Eliminar (antes había que llegar al padre)
elemento.remove();              // Moderno
elemento.parentNode.removeChild(elemento); // Antiguo
```

---

## Resumen de Selecores

| Método | Uso |
|--------|-----|
| `getElementById` | Un elemento por ID (más rápido) |
| `getElementsByClassName` | Colección viva por clase |
| `getElementsByTagName` | Colección viva por etiqueta |
| `querySelector` | Primer elemento que coincida |
| `querySelectorAll` | Todos los elementos (NodeList) |
| `closest` | Ancestro que coincida |
| `matches` | Verificar si elemento coincide |

**Nota**: `querySelector` y `querySelectorAll` son los más flexibles y suficientes para la mayoría de casos. Solo usar `getElementById` cuando el rendimiento sea crítico (millones de elementos).
