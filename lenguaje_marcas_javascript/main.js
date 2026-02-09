document.writeln("pATAT<br>")
document.write("Boniato")

// codififco mis funciones chachis

function saludo(nombre){
     
    return "Hola" + nombre + "!";
}

//var  y let

let virginia  = saludo("Virginia");


for(let index = 0; index < virginia.length ; index++ ){

    document.writeln(virginia[index] + "<br>");
    
};


for(const letra in virginia){
     document.writeln(virginia[letra] + " ");
}

document.writeln(1+"5"+"<br>")
document.writeln(1+5+"<br>")
document.writeln(saludo("Felix"));

document.writeln(111 == "111"); // esto devuelve true por que no es un comparador estrictor
document.writeln(111 === "111") ; // esto devuelv false por que es un comparador estricto 


let numero ="Fin";

switch (numero.toLowerCase()){

    case "continua":

    break;

    case "Fin":

    break;

    default :


}

let evalue = "";

if(!evalue){
    document.writeln("prueba2 no puede estar vacia <br>");
}