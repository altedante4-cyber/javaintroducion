const botones = document.querySelectorAll('button');
const selecionar_texto = document.getElementById('texto');
const escribir_aqui = document.getElementById('mostrar-texto');
for (let i = 0 ; i < botones.length ; i++ ) {

     botones[i].addEventListener("click", function(){
        
      const p = document.createElement('p');
     switch(this.id) {

        case 'cambiar-texto':

        if(selecionar_texto.value == "") return ;

        
        p.textContent = selecionar_texto.value  


        escribir_aqui.appendChild(p);

        break ;
        
        case 'cambiar-color':
        
        const array_colores = ["white","red","blue  "]

        const num_color = Math.floor(Math.random() * array_colores.length );
        escribir_aqui.style.background = array_colores[num_color];

        break ;


        case 'cambiar-color-borde':
            escribir_aqui.style.border = "2px solid  black ";

            break ;
        
        case 'cambiar-color-texto':
            escribir_aqui.style.color = "yellow";

            break;
          


        break ;
    
    }

         

     })
}