let numeros = [1, 2, 3, 4, 5];

//agrega un nombre al final

numeros.push(5)

console.log("insertar un elemeto al final de la lista ")
// agrega un nombre al inciio 
numeros.unshift(0)

console.log("insertamo un elemento al inico en este caso el 0 ")

// muestra la cantidad total de nombres
console.log("la cantidad de elementos que hay en el array es de  " + numeros.length)


// mostrar todos los elementos


numeros.forEach(function(numero){

     console.log(numero)
})


