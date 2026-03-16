# Guia de Validacion de Formularios en HTML y JavaScript

## 1. Fundamentos de Formularios HTML

### Estructura Basica
```html
<form id="miFormulario" novalidate>
  <div class="campo">
    <label for="nombre">Nombre</label>
    <input 
      type="text" 
      id="nombre" 
      name="nombre" 
      required 
      minlength="2" 
      maxlength="50"
      pattern="[A-Za-z]+"
      placeholder="Ej: Juan"
    >
    <span class="error"></span>
  </div>
</form>
```

### Atributos de Validacion Nativos HTML5
| Atributo | Descripcion |
|----------|-------------|
| `required` | Campo obligatorio |
| `minlength` / `maxlength` | Longitud minima/maxima |
| `min` / `max` | Valor minimo/maximo (numeros, fechas) |
| `pattern` | Expresion regular |
| `type` | Tipo de input (email, tel, url, number, date) |
| `novalidate` | Desactiva validacion nativa |

### Tipos de Input
```html
<input type="text">        <!-- Texto plano -->
<input type="email">       <!-- Correo electronico -->
<input type="password">    <!-- Contrasena (oculta) -->
<input type="tel">         <!-- Telefono -->
<input type="number">      <!-- Numeros -->
<input type="date">        <!-- Fecha -->
<input type="checkbox">    <!-- Casilla verificacion -->
<input type="radio">       <!-- Opcion unica -->
<input type="file">        <!-- Archivos -->
```

---

## 2. Buenas Practicas en HTML

### Semantica y Accesibilidad
```html
<!-- Correcto: Usar label asociado al input -->
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" aria-describedby="nombre-error">

<!-- Incorrecto: Label sin asociacion -->
<label>Nombre:</label>
<input type="text">

<!-- Feedback visual para errores -->
<div class="campo error">
  <input aria-invalid="true" aria-describedby="error-nombre">
  <span id="error-nombre" role="alert"></span>
</div>
```

### Estructura Recomendada
```html
<form id="formulario" novalidate>
  <fieldset>
    <legend>Informacion Personal</legend>
    
    <div class="grupo-campo">
      <label for="campo">Campo</label>
      <input id="campo" name="campo" required>
      <small class="mensaje-error"></small>
    </div>
    
  </fieldset>
  
  <button type="submit">Enviar</button>
</form>
```

---

## 3. Validacion en JavaScript

### Seleccion de Elementos
```javascript
// Formas de seleccionar elementos del DOM
const input = document.getElementById('nombre');
const inputs = document.querySelectorAll('input[type="text"]');
const formulario = document.forms['nombreFormulario'];
const elementos = formulario.elements;

// Seleccionar por atributo data
const campos = document.querySelectorAll('[data-validacion]');
```

### API Constraint Validation
```javascript
function validarCampo(input) {
  const valido = input.checkValidity();
  const mensaje = input.validationMessage;
  
  return { valido, mensaje };
}

// Metodos disponibles
input.checkValidity()      // Retorna true/false
input.validity.valid       // Estado de validez
input.validationMessage    // Mensaje de error nativo
input.setCustomValidity()  // Establecer mensaje personalizado
input.reportValidity()    // Muestra alertas nativas
```

### Validacion Personalizada Completa
```javascript
class ValidadorFormulario {
  constructor(formId) {
    this.form = document.getElementById(formId);
    this.campos = this.form.querySelectorAll('[data-validate]');
    this.errores = new Map();
    
    this.inicializar();
  }

  inicializar() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    
    this.campos.forEach(campo => {
      campo.addEventListener('blur', () => this.validarCampo(campo));
      campo.addEventListener('input', () => this.limpiarError(campo));
    });
  }

  validarCampo(campo) {
    const reglas = campo.dataset.validate.split(',');
    let valido = true;
    let mensaje = '';

    for (const regla of reglas) {
      const resultado = this.aplicarRegla(campo, regla.trim());
      if (!resultado.valido) {
        valido = false;
        mensaje = resultado.mensaje;
        break;
      }
    }

    this.actualizarUI(campo, valido, mensaje);
    return valido;
  }

  aplicarRegla(campo, regla) {
    const valores = {
      required: () => ({
        valido: campo.value.trim() !== '',
        mensaje: 'Este campo es obligatorio'
      }),
      email: () => ({
        valido: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(campo.value),
        mensaje: 'Ingrese un correo valido'
      }),
      minlength: (n) => ({
        valido: campo.value.length >= parseInt(n),
        mensaje: `Minimo ${n} caracteres`
      }),
      maxlength: (n) => ({
        valido: campo.value.length <= parseInt(n),
        mensaje: `Maximo ${n} caracteres`
      }),
      numeric: () => ({
        valido: /^\d+$/.test(campo.value),
        mensaje: 'Solo se permiten numeros'
      }),
      alphabetic: () => ({
        valido: /^[a-zA-Z\s]+$/.test(campo.value),
        mensaje: 'Solo se permiten letras'
      })
    };

    const [nombre, param] = regla.split(':');
    return valores[nombre] ? valores[nombre](param) : { valido: true, mensaje: '' };
  }

  actualizarUI(campo, valido, mensaje) {
    const grupo = campo.closest('.grupo-campo');
    const errorEl = grupo?.querySelector('.mensaje-error');
    
    if (!valido) {
      grupo?.classList.add('error');
      campo.setAttribute('aria-invalid', 'true');
      if (errorEl) errorEl.textContent = mensaje;
      this.errores.set(campo.name, mensaje);
    } else {
      grupo?.classList.remove('error');
      campo.setAttribute('aria-invalid', 'false');
      if (errorEl) errorEl.textContent = '';
      this.errores.delete(campo.name);
    }
  }

  limpiarError(campo) {
    const grupo = campo.closest('.grupo-campo');
    const errorEl = grupo?.querySelector('.mensaje-error');
    
    grupo?.classList.remove('error');
    if (errorEl) errorEl.textContent = '';
    this.errores.delete(campo.name);
  }

  handleSubmit(e) {
    e.preventDefault();
    
    let todosValidos = true;
    this.campos.forEach(campo => {
      if (!this.validarCampo(campo)) {
        todosValidos = false;
      }
    });

    if (todosValidos && this.errores.size === 0) {
      this.enviarFormulario();
    }
  }

  enviarFormulario() {
    const datos = new FormData(this.form);
    const objeto = Object.fromEntries(datos.entries());
    console.log('Datos a enviar:', objeto);
  }
}

// Uso
const validador = new ValidadorFormulario('miFormulario');
```

---

## 4. Funciones Utiles de Validacion

### Validaciones Comunes
```javascript
const Validadores = {
  requerido: (valor) => valor?.trim() !== '',
  
  email: (valor) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor),
  
  url: (valor) => /^https?:\/\/.+/.test(valor),
  
  telefono: (valor) => /^\+?[\d\s\-()]{9,}$/.test(valor),
  
  dni: (valor) => /^\d{8}[A-Z]$/.test(valor),
  
 nie: (valor) => /^[XYZ]\d{7}[A-Z]$/.test(valor),
  
  codigoPostal: (valor) => /^\d{5}$/.test(valor),
  
  password: (valor) => {
    const tieneMin = /[a-z]/.test(valor);
    const tieneMay = /[A-Z]/.test(valor);
    const tieneNum = /\d/.test(valor);
    const tieneEsp = /[!@#$%^&*]/.test(valor);
    return valor.length >= 8 && tieneMin && tieneMay && tieneNum;
  },
  
  fecha: (valor) => !isNaN(Date.parse(valor)),
  
  rango: (valor, min, max) => {
    const num = parseFloat(valor);
    return num >= min && num <= max;
  },
  
  extensionArchivo: (nombre, extensiones) => {
    const ext = nombre.split('.').pop().toLowerCase();
    return extensiones.includes(ext);
  },
  
  tamanhoArchivo: (archivo, tamanhoMaxMB) => {
    return archivo.size <= tamanhoMaxMB * 1024 * 1024;
  }
};
```

### Funciones de Interfaz
```javascript
const UI = {
  mostrarError: (input, mensaje) => {
    const grupo = input.closest('.grupo-campo');
    const errorSpan = grupo?.querySelector('.error-message');
    
    if (grupo) grupo.classList.add('has-error');
    if (errorSpan) errorSpan.textContent = mensaje;
    input.setAttribute('aria-invalid', 'true');
  },
  
  limpiarError: (input) => {
    const grupo = input.closest('.grupo-campo');
    const errorSpan = grupo?.querySelector('.error-message');
    
    if (grupo) grupo.classList.remove('has-error');
    if (errorSpan) errorSpan.textContent = '';
    input.setAttribute('aria-invalid', 'false');
  },
  
  mostrarExito: (input, mensaje = 'Correcto') => {
    const grupo = input.closest('.grupo-campo');
    const successSpan = grupo?.querySelector('.success-message');
    
    if (grupo) grupo.classList.add('has-success');
    if (successSpan) successSpan.textContent = mensaje;
  },
  
  togglePassword: (inputId, botonId) => {
    const input = document.getElementById(inputId);
    const boton = document.getElementById(botonId);
    
    boton.addEventListener('click', () => {
      const tipo = input.type === 'password' ? 'text' : 'password';
      input.type = tipo;
      boton.textContent = tipo === 'password' ? 'Mostrar' : 'Ocultar';
    });
  }
};
```

---

## 5. Iteracion sobre Formularios

### Recorrer Todos los Campos
```javascript
function obtenerDatosFormulario(form) {
  const datos = {};
  
  // Metodo 1: FormData (recomendado)
  new FormData(form).forEach((valor, clave) => {
    datos[clave] = valor;
  });
  
  // Metodo 2: querySelectorAll
  form.querySelectorAll('input, select, textarea').forEach(el => {
    if (el.name) datos[el.name] = el.value;
  });
  
  return datos;
}

// Recorrer solo inputs marcados
function validarCamposRequeridos(form) {
  const errores = [];
  
  form.querySelectorAll('[required]').forEach(campo => {
    if (!campo.value.trim()) {
      errores.push({
        campo: campo.name,
        mensaje: 'Campo requerido'
      });
      UI.mostrarError(campo, 'Campo requerido');
    }
  });
  
  return errores;
}
```

---

## 6. Eventos de Formulario

### Eventos Clave
```javascript
form.addEventListener('submit', (e) => {
  // Ocurre al enviar (validar aqui)
  e.preventDefault(); // Prevenir envio si hay errores
});

input.addEventListener('input', (e) => {
  // Ocurre en cada cambio (validacion en tiempo real)
});

input.addEventListener('blur', (e) => {
  // Ocurre al perder foco (validacion al salir del campo)
});

input.addEventListener('change', (e) => {
  // Ocurre cuando cambia el valor
});
```

---

## 7. Ejemplo: Mejorando tu Codigo Actual

Tu codigo actual tiene algunos puntos a mejorar:

```javascript
// Mejor version de tu funcion validar()
function validar() {
  const formulario = document.form1;
  const campos = formulario.querySelectorAll('input, select');
  const errorSpan = document.getElementById('error');
  let hayError = false;
  let mensajes = [];

  campos.forEach(campo => {
    // Ignorar checkbox para validacion de vacio
    if (campo.type === 'checkbox') return;
    
    if (campo.value.trim() === '') {
      hayError = true;
      campo.classList.add('input-error');
      mensajes.push(`${campo.name} es requerido`);
    } else {
      campo.classList.remove('input-error');
    }
  });

  // Validar checkbox
  const acepto = document.getElementById('acepto');
  if (!acepto.checked) {
    hayError = true;
    mensajes.push('Debe aceptar las condiciones');
  }

  // Validar edad (numero)
  const edad = document.getElementById('edad');
  if (edad.value && isNaN(edad.value)) {
    hayError = true;
    mensajes.push('La edad debe ser un numero');
  }

  if (hayError) {
    errorSpan.style.display = 'block';
    alert(mensajes.join('\n'));
  } else {
    errorSpan.style.display = 'none';
    alert('Formulario correcto');
  }
}
```

---

## 8. Resumen de Buenas Practicas

1. **Siempre usar `novalidate` en el form** para controlar validacion via JS
2. **Validar en tiempo real** con evento `input` o `blur`
3. **Mostrar errores cerca del campo** no solo con alert()
4. **Proporcionar feedback visual** (bordes rojos, iconos)
5. **Usar atributos ARIA** para accesibilidad
6. **No confiar solo en validacion cliente** (siempre validar en servidor)
7. **Limpiar errores** cuando el usuario corrige
8. **Evitar mensajes de error genericos** -ser especifico
9. **Ordenar tabindex** correctamente para navegacion
10. **Manejar el evento `submit`** -no solo el click del boton
