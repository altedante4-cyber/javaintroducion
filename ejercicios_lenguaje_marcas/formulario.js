// 1. Seleccionamos el botón por su atributo type
const boton = document.querySelector('input[type="button"]');

boton.addEventListener('click', () => {
    const inputs = document.querySelectorAll('.container input');
    const select = document.querySelector('select');
    
    // Variable para acumular todos los mensajes
    let mensajeFinal = "--- VALORES CAPTURADOS ---\n\n";

    // Iteramos por los inputs
    for (const input of inputs) {
        // Saltamos el botón para que no aparezca en el reporte
        if (input.type === 'button') continue;

        let valor;
        
        // Lógica para Checkbox y Radio
        if (input.type === 'checkbox' || input.type === 'radio') {
             
        } else {
            // Lógica para texto, fecha, hora, etc.
            valor = input.value || "(Vacío)";
        }

        // Acumulamos en el string con un salto de línea (\n)
        mensajeFinal += `• ${input.type.toUpperCase()}: ${valor}\n`;
    }

    // Añadimos el valor del select al final
    mensajeFinal += `• SELECT: ${select.value || "Sin selección"}`;

    // Mostramos la alerta única con toda la información
    alert(mensajeFinal);
});