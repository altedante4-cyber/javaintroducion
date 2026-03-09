// Generar número secreto aleatorio
const numeroSecreto = Math.floor(Math.random() * 100) + 1;

// Obtener referencias al DOM
const input = document.getElementById("numero");
const boton = document.getElementById("boton");
const resultado = document.getElementById("resultado");

boton.addEventListener("click", enviarNumero);

let contador = 0;

function enviarNumero() {
    const usuario = parseInt(input.value);

    if (isNaN(usuario) || usuario < 1 || usuario > 100) {
        alert("Ingresa un número válido entre 1 y 100");
        input.value = "";
        input.focus();
        return;
    }

    contador += 1;

    const p = document.createElement("p");

    if (usuario < numeroSecreto) {
        p.textContent = usuario + " es menor que el número secreto 🔽";
        p.style.color = "blue";
    } else if (usuario > numeroSecreto) {
        p.textContent = usuario + " es mayor que el número secreto 🔼";
        p.style.color = "red";
    } else {
        p.textContent = "🎉 ¡Correcto! El número secreto era " + numeroSecreto + " 🎉";
        p.style.color = "green";
        input.disabled = true;
        boton.disabled = true;
    }

    // mostrar resultado del intento
    resultado.appendChild(p);

    // mostrar número de intentos
    const conta = document.createElement("p");
    conta.textContent = "Número de intentos: " + contador;
    conta.style.fontWeight = "bold";

    resultado.appendChild(conta);

    input.value = "";
    input.focus();
}