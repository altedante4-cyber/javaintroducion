const pantallmostrar = document.getElementById("pantalla");
const numeros = document.getElementsByClassName("numero");
const operadores = document.getElementsByClassName("operador")
const calcularnumeros = document.getElementById("calcular")


// Recorrer todos los botones de números
for (let i = 0; i < numeros.length; i++) {
    numeros[i].addEventListener("click", function() {
        // Concatenar el número a la pantalla
        pantalla.value += this.textContent;
    });
}


// mostrar el operador
for(let i = 0 ; i < operadores.length ; i++ ){

       operadores[i].addEventListener("click",function(){

           pantalla.value += this.textContent;

            
           

        })
}


// Calcular
calcularnumeros.addEventListener("click", function() {
    try {
        pantalla.value = eval(pantalla.value);
    } catch (error) {
        pantalla.value = "Error";
    }
});








