const botones = document.querySelectorAll('button');
const input_text = document.getElementById('textoInput');
const contenedor_parrafo = document.getElementById('parrafosContainer');
const contadorSpan = document.getElementById('contador');

let array_colores = ["red", "blue", "yellow", "green"];
let contador = 0;
let array_parrafos = Array.from(document.querySelectorAll('#parrafosContainer p '))
for (let i = 0; i < botones.length; i++) {
    botones[i].addEventListener('click', function() {
        const elegir_aleatoria_color = Math.floor(Math.random() * array_colores.length);
        const p = document.createElement('p');

        switch(botones[i].id){
            case 'cambiarColorBtn':
                document.body.style.backgroundColor = array_colores[elegir_aleatoria_color];
                break;

            case 'agregarParrafoBtn':
                const texto = input_text.value.trim();
                if(texto === "") return;
                
                p.textContent = texto;

                array_parrafos.push(p);
                contenedor_parrafo.appendChild(p);
                input_text.value = "";
                input_text.focus();

                contador++;
                contadorSpan.textContent = contador;
                break;

            case 'reordenarBtn':

    // Mezclar el array de párrafos
    array_parrafos.sort(() => Math.random() - 0.5);

    // Limpiar el contenedor
    contenedor_parrafo.innerHTML = "";

    // Agregar los párrafos mezclados con color verde
    array_parrafos.forEach(elemento => {
        const copia = elemento.cloneNode(true); // true en minúscula
        copia.style.color = "green";            // asignar color correctamente
        contenedor_parrafo.appendChild(copia);  // agregar al contenedor
    });

    break;
            case 'eliminarUltimoBtn':
                
                break;
        }
    });
}