# JavaScript DOM - Guía Completa

## 1. Selección de Elementos

### Por ID (más específico)
```javascript
document.getElementById('miId')
```

### Por clase/etiqueta (retorna colección)
```javascript
document.getElementsByClassName('miClase')
document.getElementsByTagName('div')
```

### Selectores modernos (recomendado)
```javascript
document.querySelector('.miClase')      // Primer elemento
document.querySelectorAll('.miClase')   // Todos los elementos
```

---

## 2. Manipulación de Contenido

### Texto
```javascript
elemento.textContent = 'Nuevo texto'   // Texto plano
elemento.innerText = 'Nuevo texto'     // Texto visible
```

### HTML
```javascript
elemento.innerHTML = '<p>HTML</p>'     // Reemplaza todo
elemento.outerHTML = '<div>Reemplaza el elemento</div>'
```

### Valores (inputs)
```javascript
input.value = 'Valor'
const valor = input.value
```

---

## 3. Creación de Elementos

```javascript
const nuevoElemento = document.createElement('div')
nuevoElemento.textContent = 'Hola'
nuevoElemento.className = 'miClase'
nuevoElemento.id = 'miId'

// Insertar en el DOM
padre.appendChild(nuevoElemento)           // Al final
padre.insertBefore(nuevoElemento, hijo)     // Antes de hijo
padre.insertAdjacentHTML('beforeend', '<p>') // Posiciones variebles
```

### Posiciones de insertAdjacentHTML
- `beforebegin` - Antes del elemento
- `afterbegin` - Dentro, al principio
- `beforeend` - Dentro, al final
- `afterend` - Después del elemento

---

## 4. Atributos y Clases

### Atributos
```javascript
elemento.setAttribute('data-id', '123')
elemento.getAttribute('data-id')
elemento.removeAttribute('data-id')
elemento.hasAttribute('data-id')
```

### Clases (recomendado)
```javascript
elemento.classList.add('miClase')
elemento.classList.remove('miClase')
elemento.classList.toggle('miClase')
elemento.classList.contains('miClase')
```

---

## 5. Estilos (CSS)

```javascript
elemento.style.color = 'red'
elemento.style.display = 'none'
elemento.style.backgroundColor = 'blue'  // camelCase
elemento.style.cssText = 'color: red; font-size: 16px'
```

---

## 6. Eventos

### addEventListener (recomendado)
```javascript
elemento.addEventListener('click', function(e) {
    e.preventDefault()  // Evitar comportamiento por defecto
    e.stopPropagation() // Evitar propagación
})

// Versión arrow
elemento.addEventListener('click', (e) => {
    console.log(e.target)  // Elemento que originó el evento
    console.log(e.currentTarget)  // Elemento con el listener
})
```

### Eventos comunes
- `click`, `dblclick`
- `submit` (formularios)
- `input`, `change` (inputs)
- `keydown`, `keyup`
- `mouseenter`, `mouseleave`
- `load`, `DOMContentLoaded`

### Event delegation (delegación)
```javascript
document.querySelector('ul').addEventListener('click', (e) => {
    if(e.target.tagName === 'LI') {
        console.log(e.target.textContent)
    }
})
```

---

## 7. Formularios

### Obtener botón presionado
```javascript
form.addEventListener('submit', (e) => {
    e.preventDefault()
    const botonPulsado = e.submitter.value
})
```

### Validación
```javascript
input.checkValidity()
input.validity.valid
input.validity.valueMissing
input.setCustomValidity('Mensaje')
```

---

## 8. Arrays - Métodos Útiles

### push/pop (final)
```javascript
array.push(elemento)    // Añadir al final
array.pop()            // Eliminar último
```

### shift/unshift (inicio)
```javascript
array.shift()          // Eliminar primero
array.unshift(elemento) // Añadir al inicio
```

### filter/map/forEach
```javascript
const nuevos = array.filter(item => item.edad > 18)
const textos = array.map(item => item.nombre)
array.forEach(item => console.log(item))
```

### find/findIndex
```javascript
const encontrado = array.find(item => item.id === 5)
const indice = array.findIndex(item => item.id === 5)
```

---

## 9. Buenas Prácticas

### 1. Usar querySelector/querySelectorAll
```javascript
// ❌ Evitar
document.getElementsByClassName('clase')

// ✅ Preferir
document.querySelectorAll('.clase')
```

### 2. Cachear elementos
```javascript
// ❌ Mal: buscar en cada click
boton.addEventListener('click', () => {
    document.getElementById('menu').style.display = 'block'
})

// ✅ Bien: buscar una vez
const menu = document.getElementById('menu')
boton.addEventListener('click', () => {
    menu.style.display = 'block'
})
```

### 3. Usar event delegation
```javascript
// ❌ Mal: listener en cada item
items.forEach(item => item.addEventListener('click', handler))

// ✅ Bien: un solo listener
lista.addEventListener('click', (e) => {
    if(e.target.matches('.item')) handler()
})
```

### 4. Prevenir XSS
```javascript
// ✅ Usar textContent, no innerHTML con datos de usuarios
elemento.textContent = datosDelUsuario

// ⚠️ Si necesitas innerHTML, sanitiza
elemento.innerHTML = sanitizar(datosDelUsuario)
```

### 5. Usar const/let, evitar var
```javascript
const elemento = document.getElementById('id')  // No cambiará
let contador = 0  // Cambiará
```

### 6. Nombres descriptivos
```javascript
// ❌ Mal
const d = document.getElementById('c')
const arr = []

// ✅ Bien
const contenedor = document.getElementById('citas')
const historialCitas = []
```

---

## 10. Errores Comunes

### 1. Olvidar paréntesis en funciones
```javascript
// ❌ Error
e.preventDefault

// ✅ Correcto
e.preventDefault()
```

### 2. Confundir textContent con elementos
```javascript
// ❌ Error: guarda objeto, no texto
array.push(elementoDOM)

// ✅ Correcto
array.push(elementoDOM.textContent)
// o
array.push(elementoDOM.outerHTML)
```

### 3. Reutilizar el mismo elemento
```javascript
// ❌ Error: mismo elemento en varios lugares
const p = document.createElement('p')
array.forEach(item => {
    p.textContent = item
    contenedor.appendChild(p)
})

// ✅ Correcto: crear nuevo en cada iteración
array.forEach(item => {
    const p = document.createElement('p')
    p.textContent = item
    contenedor.appendChild(p)
})
```

### 4. No limpiar contenedores antes de actualizar
```javascript
// ❌ Error: acumula contenido
contenedor.appendChild(nuevo)

// ✅ Correcto: limpiar primero
contenedor.innerHTML = ''
contenedor.appendChild(nuevo)
```

---

## 11. Objeto Event (e)

### Propiedades útiles
```javascript
e.target           // Elemento que originó el evento
e.currentTarget    // Elemento con el listener
e.preventDefault() // Cancela acción por defecto
e.stopPropagation() // Detiene propagación
e.type             // Tipo de evento ('click', 'submit', etc.)
```

---

## 12. LocalStorage (datos persistentes)

```javascript
// Guardar
localStorage.setItem('clave', 'valor')
localStorage.setItem('usuario', JSON.stringify(objeto))

// Leer
localStorage.getItem('clave')
JSON.parse(localStorage.getItem('usuario'))

// Eliminar
localStorage.removeItem('clave')
localStorage.clear()  // Todo
```

---

## 13. setTimeout / setInterval

```javascript
// Ejecutar después de delay
setTimeout(() => {
    console.log('Después de 1 segundo')
}, 1000)

// Ejecutar repetidamente
const intervalo = setInterval(() => {
    console.log('Cada segundo')
}, 1000)

// Detener
clearInterval(intervalo)
```

---

## 14. Convertir Colecciones a Arrays

```javascript
// HTMLCollection o NodeList a Array
const array = Array.from(elementos)
const array = [...elementos]

// Útil para usar métodos de array
document.querySelectorAll('div').forEach(...)
```

---

## 15. Debugging

```console.log()``` para inspección básica
```javascript
console.log(elemento)
console.log('Texto:', elemento.textContent)
console.dir(elemento)  // Ver todas las propiedades
```

---

## 16. Recursos Adicionales

- [MDN DOM](https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model)
- [MDN Eventos](https://developer.mozilla.org/es/docs/Web/Events)
- [Can I Use](https://caniuse.com/) - Compatibilidad navegadores
