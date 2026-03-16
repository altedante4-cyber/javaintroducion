# Documentación JavaScript: Formularios y Eventos

## Obtener Inputs de un Formulario e Iterar

### Método 1: querySelectorAll

```javascript
const form = document.getElementById('formulario-contacto');
const inputs = form.querySelectorAll('input, select, textarea');

inputs.forEach(input => {
  console.log(input.name, input.value);
});
```

### Método 2: FormData (Recomendado)

`FormData` es una API nativa que facilita obtener todos los datos de un formulario.

```javascript
const form = document.getElementById('formulario-contacto');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Evita el envío tradicional
  
  const formData = new FormData(form);
  
  // Iterar con for...of
  for (const [name, value] of formData.entries()) {
    console.log(name, value);
  }
  
  // Obtener un valor específico
  const email = formData.get('email');
  
  // Convertir a objeto plano
  const data = Object.fromEntries(formData);
});
```

### Método 3: elements del formulario

```javascript
const form = document.getElementById('formulario-contacto');

form.addEventListener('submit', function(event) {
  const elements = form.elements; // HTMLFormControlsCollection
  
  for (let i = 0; i < elements.length; i++) {
    const el = elements[i];
    if (el.name) {
      console.log(el.name, el.value);
    }
  }
});
```

**Nota**: Solo los elementos con atributo `name` serán incluidos en FormData.

---

## Eventos en JavaScript

### addEventListener

```javascript
elemento.addEventListener('evento', callback, opciones);
```

| Parámetro | Descripción |
|-----------|-------------|
| evento | Tipo de evento ('click', 'submit', 'input', etc.) |
| callback | Funión que se ejecuta cuando ocurre el evento |
| opciones | Objeto o boolean para capturar/bubbling |

### Tercer Parámetro: Bubbling vs Capturing

Cuando ocurre un evento, este pasa por **3 fases**:

```
1. Capturing (bajar)    → window → document → body → ... → target
2. Target (objetivo)     → el elemento donde ocurrió el evento
3. Bubbling (subir)      → target → ... → body → document → window
```

```javascript
// Bubbling (default) - el más común
elemento.addEventListener('click', handler, false);
// o simplemente
elemento.addEventListener('click', handler);

// Capturing - el evento se maneja bajando
elemento.addEventListener('click', handler, true);
// o
elemento.addEventListener('click', handler, { capture: true });
```

### Ejemplo Práctico

```html
<div id="padre">
  <div id="hijo">
    <button id="boton">Click</button>
  </div>
</div>
```

```javascript
document.getElementById('padre').addEventListener('click', () => {
  console.log('Padre - Bubbling');
});

document.getElementById('hijo').addEventListener('click', () => {
  console.log('Hijo - Bubbling');
});

document.getElementById('boton').addEventListener('click', () => {
  console.log('Botón clickeado');
});
```

Al hacer click en el botón, la consola muestra:
```
Botón clickeado
Hijo - Bubbling
Padre - Bubbling
```

### Controlar Propagación

```javascript
boton.addEventListener('click', function(event) {
  // Detiene la propagación (no llega a padre)
  event.stopPropagation();
  
  // Evita el comportamiento por defecto (ej: submit de form)
  event.preventDefault();
});
```

### Objeto Event

```javascript
elemento.addEventListener('click', function(event) {
  event.target;        // Elemento que originó el evento
  event.currentTarget; // Elemento donde está asignado el listener
  event.type;          // Tipo de evento ('click')
  event.preventDefault(); // Cancela acción por defecto
  event.stopPropagation(); // Detiene propagación
});
```

### Eventos Comunes en Formularios

| Evento | Descripción |
|--------|-------------|
| submit | Se dispara al enviar el formulario |
| input | Se dispara al cambiar el valor (en tiempo real) |
| change | Se dispara al perder foco después de un cambio |
| blur | Se dispara al perder foco |
| focus | Se dispara al obtener foco |
| invalid | Se dispara cuando un campo es inválido |

```javascript
// Validación en tiempo real
input.addEventListener('input', function(event) {
  console.log('Valor actual:', event.target.value);
});

// Validación al perder foco
input.addEventListener('blur', function(event) {
  if (!event.target.value) {
    mostrarError('Campo requerido');
  }
});
```

### Event Delegation (Delegación de Eventos)

En lugar de agregar un listener a cada input, agregas uno al formulario:

```javascript
const form = document.getElementById('formulario-contacto');

form.addEventListener('input', function(event) {
  // event.target es el input específico que cambió
  console.log('Input cambiado:', event.target.name, event.target.value);
});
```

Esto es más eficiente que agregar listeners individuales a cada campo.

---

## Recursos

- [MDN: FormData](https://developer.mozilla.org/es/docs/Web/API/FormData)
- [MDN: addEventListener](https://developer.mozilla.org/es/docs/Web/API/EventTarget/addEventListener)
- [MDN: Event bubbling y capturing](https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/Events#Event_bubbling_and_capture)
