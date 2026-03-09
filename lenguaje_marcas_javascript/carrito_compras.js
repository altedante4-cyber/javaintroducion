let frutas = ["melocoton","sandia","naranja","frutilla"];

let carrito = []
let frutasDisponibles = [...frutas]; // copia del array 

for (let i =  0 ; i < 3; i++ ){

      let indicealeatorio_frutas = Math.floor(Math.random () * frutasDisponibles.length);

      carrito.push( frutasDisponibles[indicealeatorio_frutas]);
      frutasDisponibles.splice(indicealeatorio_frutas,1);  // eliminar para no repetir 

}


carrito.forEach(function(elemento) {

     console.log(elemento);
})
