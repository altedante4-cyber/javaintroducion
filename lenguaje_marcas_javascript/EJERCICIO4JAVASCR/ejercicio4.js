const num1 = document.getElementById('num1')
const num2 = document.getElementById('num2')
//ojo esos dos numeros hay que convertirlos a enteros por que vienene en texxto
const botones = document.querySelectorAll('button')
const div_mostrarcontenido = document.getElementById('resultado')
const  p = document.getElementById('resul-p')



for(let i = 0 ; i < botones.length ; i++){

     botones[i].addEventListener("click",function() {
        let entero1 = parseInt(num1.value)
        let entero2 = parseInt(num2.value)              
        switch(this.id){
                
             case 'btn1':
                const resultado = entero1 + entero2
                
                p.textContent =resultado
              
              break ;
             case 'btn2':
                    const resultado2 = entero1 - entero2
                   p.textContent = resultado2

             break ; 

             case 'btn3':

                const resultado3 = entero1 % entero2
                p.textContent = resultado3

            break ; 

            case 'btn4': 
                const resultado4 = entero1 / entero2 
                p.textContent = resultado4
            break ; 

            case 'btn5':
                num1.value = ""
                num2.value = ""
            break ; 
        
        
        }



     })
}