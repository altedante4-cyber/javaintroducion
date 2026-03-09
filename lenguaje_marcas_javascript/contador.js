let contador = 0;

const display = document.getElementById('display');
const btnIncrementar = document.getElementById('btnIncrementar');
const btnDecrementar = document.getElementById('btnDecrementar');
const btnReiniciar = document.getElementById('btnReiniciar');

btnIncrementar.addEventListener('click', function() {
    contador++;
    actualizarDisplay();
});

btnDecrementar.addEventListener('click', function() {
    contador--;
    actualizarDisplay();
});

btnReiniciar.addEventListener('click', function() {
    contador = 0;
    actualizarDisplay();
});

function actualizarDisplay() {
    display.textContent = contador;
    
    if (contador > 0) {
        display.style.color = '#27ae60';
    } else if (contador < 0) {
        display.style.color = '#e74c3c';
    } else {
        display.style.color = '#2c3e50';
    }
}
