// Array para almacenar las tareas
let tareas = [];

// Referencias al DOM
const input = document.getElementById('tareaInput');
const botonAgregar = document.getElementById('agregarBtn');
const listaTareas = document.getElementById('listaTareas');
const contador = document.getElementById('contador');

// Función para agregar tarea
function agregarTarea() {
    const texto = input.value.trim();
    
    if (texto === "") {
        alert("Escribe una tarea");
        return;
    }

    tareas.push(texto);
    input.value = "";
    renderizarTareas();
}

// Función para eliminar tarea
function eliminarTarea(indice) {
    tareas.splice(indice, 1);
    renderizarTareas();
}

// Función para renderizar la lista
function renderizarTareas() {
    listaTareas.innerHTML = "";
    
    tareas.forEach(function(tarea, indice) {
        const li = document.createElement('li');
        li.textContent = tarea;
        
        const btnEliminar = document.createElement('button');
        btnEliminar.textContent = "Eliminar";
        btnEliminar.className = "btn-eliminar";
        btnEliminar.onclick = function() {
            eliminarTarea(indice);
        };
        
        li.appendChild(btnEliminar);
        listaTareas.appendChild(li);
    });

    contador.textContent = "Total: " + tareas.length + " tareas";
}

// Event listeners
botonAgregar.addEventListener('click', agregarTarea);

input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        agregarTarea();
    }
});
