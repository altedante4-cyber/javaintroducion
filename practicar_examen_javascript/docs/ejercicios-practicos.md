# Ejercicios Prácticos de HTML, CSS y JavaScript

Cada ejercicio incluye el código HTML y la descripción de la funcionalidad a implementar.

---

## 1. innerHTML - Mostrar Datos

### Ejercicio 1: Lista de nombres dinámica

**HTML:**
```html
<ul id="lista-nombres"></ul>
<button id="btn-mostrar">Mostrar Nombres</button>
```

**JS - Funcionalidad:**
- Crear array de nombres
- Al hacer clic en el botón, mostrar los nombres en la lista usando innerHTML
- Cada nombre debe estar dentro de un `<li>`

---

### Ejercicio 2: Tarjetas de productos

**HTML:**
```html
<div id="contenedor-tarjetas" class="grid"></div>
```

**JS - Funcionalidad:**
- Array de productos: `{ nombre, precio, imagen }`
- Crear tarjetas con estilo CSS (border, padding, sombra)
- Mostrar en el contenedor con innerHTML

---

### Ejercicio 3: Tabla de empleados

**HTML:**
```html
<table id="tabla-empleados">
    <thead>
        <tr><th>Nombre</th><th>Puesto</th><th>Salario</th></tr>
    </thead>
    <tbody></tbody>
</table>
```

**JS - Funcionalidad:**
- Array de empleados
- Renderizar en el tbody con innerHTML
- Formatear salario con `$`

---

## 2. Iterar sobre Elementos

### Ejercicio 4: Contar y mostrar total

**HTML:**
```html
<div class="producto">Producto 1</div>
<div class="producto">Producto 2</div>
<div class="producto">Producto 3</div>
<p>Total: <span id="total">0</span></p>
```

**JS - Funcionalidad:**
- Seleccionar todos los elementos con clase `.producto`
- Contarlos y mostrar el total en el span

---

### Ejercicio 5: Aplicar estilo a elementos pares

**HTML:**
```html
<ul id="lista-colores">
    <li>Rojo</li>
    <li>Verde</li>
    <li>Azul</li>
    <li>Amarillo</li>
    <li>Morado</li>
</ul>
```

**JS - Funcionalidad:**
- Iterar sobre todos los `<li>`
- A los que están en posición par, agregar clase `.par` (fondo gris)

---

### Ejercicio 6: Sumar valores de inputs

**HTML:**
```html
<input type="number" class="cantidad" value="10">
<input type="number" class="cantidad" value="20">
<input type="number" class="cantidad" value="30">
<button id="btn-sumar">Sumar</button>
<p>Total: <span id="resultado">0</span></p>
```

**JS - Funcionalidad:**
- Al hacer clic en el botón
- Iterar sobre todos los inputs con clase `.cantidad`
- Sumar sus valores y mostrar el resultado

---

### Ejercicio 7: Obtener valores de checkbox marcados

**HTML:**
```html
<input type="checkbox" name="hobby" value="deporte"> Deporte
<input type="checkbox" name="hobby" value="musica"> Música
<input type="checkbox" name="hobby" value="lectura"> Lectura
<button id="btn-obtener">Obtener seleccionados</button>
<p id="seleccionados"></p>
```

**JS - Funcionalidad:**
- Al hacer clic, obtener todos los checkbox marcados
- Mostrar sus valores separados por coma

---

## 3. classList - Manipular CSS

### Ejercicio 8: Toggle de clase

**HTML:**
```html
<div id="caja" class="caja"></div>
<button id="btn-toggle">Cambiar Color</button>
```

**CSS:**
```css
.caja { width: 100px; height: 100px; background: blue; }
.caja.activa { background: red; }
```

**JS - Funcionalidad:**
- Al hacer clic, usar `classList.toggle('activa')` para cambiar el color

---

### Ejercicio 9: Validación visual de formulario

**HTML:**
```html
<input type="text" id="nombre" placeholder="Nombre">
<span class="error" id="error-nombre">El nombre es requerido</span>
<button id="btn-validar">Validar</button>
```

**CSS:**
```css
.error { color: red; display: none; }
.error.visible { display: block; }
input.error { border: 2px solid red; }
input.success { border: 2px solid green; }
```

**JS - Funcionalidad:**
- Al hacer clic en validar:
  - Si está vacío: agregar clase `.visible` al error y `.error` al input
  - Si tiene valor: agregar `.success` al input

---

### Ejercicio 10: Pestañas (Tabs)

**HTML:**
```html
<div class="tabs">
    <button class="tab active" data-tab="uno">Tab 1</button>
    <button class="tab" data-tab="dos">Tab 2</button>
    <button class="tab" data-tab="tres">Tab 3</button>
</div>
<div id="uno" class="contenido-tab">Contenido 1</div>
<div id="dos"class="contenido-tab"style="display:none">Contenido 2</div>
<div id="tres" class="contenido-tab" style="display:none">Contenido 3</div>
```

**JS - Funcionalidad:**
- Al hacer clic en un tab:
  - Quitar clase `.active` de todos los tabs
  - Agregar `.active` al tab clickeado
  - Ocultar todos los contenidos
  - Mostrar el contenido correspondiente

---

### Ejercicio 11: Menú desplegable

**HTML:**
```html
<nav>
    <button id="btn-menu">☰ Menú</button>
    <ul id="menu" class="menu oculto">
        <li>Inicio</li>
        <li>Productos</li>
        <li>Contacto</li>
    </ul>
</nav>
```

**CSS:**
```css
.menu { list-style: none; padding: 10px; background: #eee; }
.menu.oculto { display: none; }
.menu.mostrar { display: block; }
```

**JS - Funcionalidad:**
- Al hacer clic en el botón, usar `classList.toggle('oculto')` y `classList.toggle('mostrar')`

---

## 4. Agregar Elementos

### Ejercicio 12: Agregar item a lista

**HTML:**
```html
<input type="text" id="nuevo-item" placeholder="Nuevo item">
<button id="btn-agregar">Agregar</button>
<ul id="lista"></ul>
```

**JS - Funcionalidad:**
- Al hacer clic en agregar:
  - Crear nuevo elemento `<li>`
  - Poner el texto del input
  - Agregar a la lista con `appendChild`

---

### Ejercicio 13: Agregar producto al carrito

**HTML:**
```html
<div id="productos">
    <button class="btn-producto" data-nombre="Camisa" data-precio="25">Camisa - $25</button>
    <button class="btn-producto" data-nombre="Pantalón" data-precio="40">Pantalón - $40</button>
</div>
<h3>Carrito</h3>
<div id="carrito"></div>
<p>Total: $<span id="total-carrito">0</span></p>
```

**JS - Funcionalidad:**
- Al hacer clic en un producto:
  - Crear elemento con nombre y precio
  - Agregar al carrito
  - Actualizar total

---

### Ejercicio 14: Crear elementos con DocumentFragment

**HTML:**
```html
<div id="contenedor-lista"></div>
<button id="btn-crear">Crear 100 elementos</button>
```

**JS - Funcionalidad:**
- Al hacer clic, crear 100 elementos usando DocumentFragment
- Esto es más eficiente que agregar uno por uno

---

## 5. Eliminar Elementos

### Ejercicio 15: Eliminar item de lista

**HTML:**
```html
<ul id="lista-tareas">
    <li>Tarea 1 <button class="btn-eliminar">X</button></li>
    <li>Tarea 2 <button class="btn-eliminar">X</button></li>
    <li>Tarea 3 <button class="btn-eliminar">X</button></li>
</ul>
```

**JS - Funcionalidad:**
- Agregar event listener a cada botón
- Al hacer clic, eliminar el elemento padre (`<li>`)

---

### Ejercicio 16: Eliminar productos del carrito

**HTML:**
```html
<div id="carrito">
    <div class="item-carrito">
        <span>Producto 1</span>
        <button class="eliminar">Eliminar</button>
    </div>
</div>
```

**JS - Funcionalidad:**
- Usar event delegation en el contenedor del carrito
- Al hacer clic en eliminar, remover el elemento del DOM

---

### Ejercicio 17: Limpiar formulario

**HTML:**
```html
<form id="mi-formulario">
    <input type="text" value="Hola">
    <select>
        <option selected>Opción 1</option>
    </select>
    <textarea>Texto</textarea>
</form>
<button id="btn-limpiar">Limpiar</button>
```

**JS - Funcionalidad:**
- Al hacer clic, recorrer todos los inputs, selects, textareas
- Resetear sus valores a vacío o primer opción

---

## 6. Validar

### Ejercicio 18: Validar email

**HTML:**
```html
<input type="text" id="email" placeholder="correo@ejemplo.com">
<button id="btn-validar">Validar Email</button>
<p id="resultado-email"></p>
```

**JS - Funcionalidad:**
- Regex: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
- Mostrar mensaje de válido o inválido

---

### Ejercicio 19: Validar contraseña

**HTML:**
```html
<input type="password" id="password" placeholder="Contraseña">
<input type="password" id="confirmar" placeholder="Confirmar">
<button id="btn-validar">Validar</button>
<p id="resultado"></p>
```

**JS - Funcionalidad:**
- La contraseña debe tener al menos 8 caracteres
- Las dos contraseñas deben coincidir
- Mostrar errores específicos

---

### Ejercicio 20: Validar formulario completo

**HTML:**
```html
<form id="form-registro">
    <input type="text" id="nombre" placeholder="Nombre">
    <span class="error" id="error-nombre"></span>
    
    <input type="email" id="correo" placeholder="Email">
    <span class="error" id="error-correo"></span>
    
    <input type="password" id="pass" placeholder="Password">
    <span class="error" id="error-pass"></span>
    
    <button type="submit">Registrarse</button>
</form>
```

**JS - Funcionalidad:**
- Validar al enviar:
  - Nombre: no vacío, solo letras
  - Email: formato válido
  - Password: mínimo 8 caracteres
- Mostrar errores con classList.add('visible')

---

### Ejercicio 21: Validar número en rango

**HTML:**
```html
<input type="number" id="edad" placeholder="Edad">
<button id="btn-validar">Verificar</button>
<p id="resultado"></p>
```

**JS - Funcionalidad:**
- Validar que la edad esté entre 1 y 120
- Mostrar mensaje apropiado

---

## 7. Random

### Ejercicio 22: Número aleatorio

**HTML:**
```html
<button id="btn-random">Generar Número</button>
<p>Número: <span id="numero">-</span></p>
```

**JS - Funcionalidad:**
- Generar número aleatorio entre 1 y 100
- Mostrarlo al hacer clic

---

### Ejercicio 23: Color aleatorio en caja

**HTML:**
```html
<div id="caja-color"></div>
<button id="btn-color">Cambiar Color</button>
```

**CSS:**
```css
#caja-color { width: 200px; height: 200px; border: 2px solid black; }
```

**JS - Funcionalidad:**
- Generar color aleatorio en formato hex
- Aplicar como background-color

---

### Ejercicio 24: Elegir ganador

**HTML:**
```html
<input type="text" id="participante" placeholder="Nombre">
<button id="btn-agregar">Agregar Participante</button>
<button id="btn-sorteo">¡Sorteo!</button>
<p>Ganador: <span id="ganador">-</span></p>
<ul id="lista-participantes"></ul>
```

**JS - Funcionalidad:**
- Agregar participantes a una lista
- Al hacer clic en sorteo, elegir uno al azar
- Mostrar el ganador

---

### Ejercicio 25: Barajar y mostrar orden

**HTML:**
```html
<button id="btn-barajar">Barajar</button>
<div id="cartas"></div>
```

**JS - Funcionalidad:**
- Array de naipes: ['A♠', 'K♠', 'Q♠', 'J♠', '10♠']
- Barajarlos aleatoriamente
- Mostrar el nuevo orden en el div

---

### Ejercicio 26: Dado virtual

**HTML:**
```html
<div id="dado">🎲</div>
<button id="btn-tirar">Tirar Dado</button>
<p>Resultado: <span id="resultado-dado">-</span></p>
```

**JS - Funcionalidad:**
- Generar número del 1 al 6
- Mostrar el resultado
- (Opcional) Cambiar el emoji del dado

---

### Ejercicio 27: Frase aleatoria

**HTML:**
```html
<button id="btn-frase">Nueva Frase</button>
<blockquote id="frase"></blockquote>
```

**JS - Funcionalidad:**
- Array de frases célebres
- Mostrar una al azar cada vez que se hace clic

---

## 8. Ejercicios Combinados

### Ejercicio 28: Lista de tareas (To-Do)

**HTML:**
```html
<input type="text" id="tarea-input" placeholder="Nueva tarea">
<button id="btn-agregar">Agregar</button>
<ul id="lista-tareas"></ul>
<p>Pendientes: <span id="contador">0</span></p>
```

**JS - Funcionalidad:**
- Agregar tareas nuevas
- Marcar como completada (agregar clase .completada)
- Eliminar tareas
- Contar pendientes

---

### Ejercicio 29: Contador con botones

**HTML:**
```html
<button id="btn-menos">-</button>
<span id="contador">0</span>
<button id="btn-mas">+</button>
<button id="btn-reset">Reset</button>
```

**JS - Funcionalidad:**
- Incrementar, decrementar y resetear
- Cambiar color si es negativo (rojo)

---

### Ejercicio 30: Calculadora simple

**HTML:**
```html
<input type="number" id="num1">
<select id="operador">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">×</option>
    <option value="/">÷</option>
</select>
<input type="number" id="num2">
<button id="btn-calcular">=</button>
<p>Resultado: <span id="resultado">0</span></p>
```

**JS - Funcionalidad:**
- Realizar la operación seleccionada
- Manejar división por cero

---

### Ejercicio 31: Galería de imágenes

**HTML:**
```html
<div id="galeria">
    <img src="img1.jpg" class="img-galeria">
    <img src="img2.jpg" class="img-galeria">
    <img src="img3.jpg" class="img-galeria">
</div>
<div id="visor">
    <img id="imagen-grande">
    <button id="btn-cerrar">X</button>
</div>
```

**CSS:**
```css
#visor { position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
         background: rgba(0,0,0,0.8); display: none; justify-content: center; 
         align-items: center; }
#visor.mostrar { display: flex; }
```

**JS - Funcionalidad:**
- Al hacer clic en imagen, mostrarla en visor grande
- Agregar clase .mostrar al visor
- Cerrar con botón o fuera de la imagen

---

### Ejercicio 32: Quiz interactivo

**HTML:**
```html
<div id="pregunta"></div>
<div id="opciones"></div>
<p>Puntos: <span id="puntos">0</span></p>
```

**JS - Funcionalidad:**
- Array de preguntas con opciones
- Al seleccionar respuesta, verificar si es correcta
- Sumar puntos
- Pasar a siguiente pregunta

---

### Ejercicio 33: Generador de contraseñas

**HTML:**
```html
<input type="text" id="password-generada" readonly>
<button id="btn-generar">Generar</button>
<label>
    <input type="checkbox" id="incluir-numeros"> Incluir números
</label>
<label>
    <input type="checkbox" id="incluir-simbolos"> Incluir símbolos
</label>
```

**JS - Funcionalidad:**
- Generar contraseña aleatoria
- Longitud: 12 caracteres
- Opcional: incluir números y/o símbolos

---

### Ejercicio 34: Reloj digital

**HTML:**
```html
<div id="reloj">00:00:00</div>
<button id="btn-iniciar">Iniciar</button>
<button id="btn-detener">Detener</button>
```

**JS - Funcionalidad:**
- Mostrar hora actual en formato HH:MM:SS
- Actualizar cada segundo con setInterval
- Botones para iniciar y detener

---

### Ejercicio 35: Buscador en tiempo real

**HTML:**
```html
<input type="text" id="buscador" placeholder="Buscar...">
<ul id="lista-items">
    <li>Manzana</li>
    <li>Banano</li>
    <li>Naranja</li>
    <li>Uva</li>
    <li>Papaya</li>
</ul>
```

**JS - Funcionalidad:**
- Al escribir en el input, filtrar la lista
- Ocultar elementos que no coincidan
- Búsqueda sin distinción de mayúsculas

---

### Ejercicio 36: Carrito de compras completo

**HTML:**
```html
<div id="productos"></div>
<h3>Carrito</h3>
<div id="carrito"></div>
<p>Subtotal: $<span id="subtotal">0</span></p>
<p>IVA (16%): $<span id="iva">0</span></p>
<p>Total: $<span id="total">0</span></p>
```

**JS - Funcionalidad:**
- Lista de productos con precios
- Agregar al carrito
- Eliminar del carrito
- Calcular subtotal, IVA y total

---

## Tabla de Referencia Rápida

| Necesidad | Código |
|-----------|--------|
| Seleccionar ID | `document.getElementById('id')` |
| Seleccionar clase | `document.querySelectorAll('.clase')` |
| Crear elemento | `document.createElement('div')` |
| Agregar hijo | `padre.appendChild(hijo)` |
| Eliminar | `elemento.remove()` |
| Agregar clase | `elemento.classList.add('clase')` |
| Quitar clase | `elemento.classList.remove('clase')` |
| Toggle clase | `elemento.classList.toggle('clase')` |
| Tiene clase | `elemento.classList.contains('clase')` |
| Texto | `elemento.textContent = 'texto'` |
| HTML | `elemento.innerHTML = '<div>html</div>'` |
| Valor input | `input.value` |
| Random 0-1 | `Math.random()` |
| Random entero | `Math.floor(Math.random() * max) + min` |
| Array aleatorio | `array.sort(() => Math.random() - 0.5)` |
