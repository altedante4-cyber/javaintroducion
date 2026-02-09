const leer = document.getElementById("tarea")
const inputleer = document.getElementById("tareainput")
const lista = document.getElementById("lista");
const generar_color = "0123456789ABCDEF";

let tareas = []
function escribirdocumento(){

    if(inputleer.value == ""){
        alert("El input no puede estar vacio ingrese letras ");
        return 
    }

    alert("entrada exitosa")

    tareas.push(inputleer.value);
    inputleer.value ="";

    mostrartareas();

}


function mostrartareas(){
    lista.innerHTML =""; //limpiar antes

    tareas.forEach((tarea,index) => {
        const li = document.createElement("li");
        li.textContent = `${index + 1}. ${tarea}`; // textcontent ponetexto dentor de innerHTML
        lista.appendChild(li);
    })

}
document.getElementById("tarea").addEventListener("click", escribirdocumento);



function elegircolor(){
     
    let resultado ="";




    for(let i = 0 ; i < 6 ; i++ ){
         
         const indice = Math.floor(Math.random() * generar_color.length  ) ; //math.floor redondea hacia abajo  y math.random eligi numeros entre 1 y 0  para abajo 

         resultado += generar_color[indice];
    }

    return document.body.style.backgroundColor="#"+resultado;
}
document.getElementById("color").addEventListener("click",elegircolor);
