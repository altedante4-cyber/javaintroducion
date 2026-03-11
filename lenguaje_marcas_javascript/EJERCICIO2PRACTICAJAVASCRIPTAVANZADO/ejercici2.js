const botones = document.querySelectorAll('button')
const input1 = document.getElementById('input1')
const input2 = document.getElementById('input2')
for (let i = 0 ; i < botones.length ; i++ ){

      botones[i].addEventListener("click",function() {

            switch(this.id){

                 case 'btn1-1':
                    input1.value=""
                    break;

                case 'btn3-1':
                    input2.value=""
                    break ; 

                case 'btn2-1':
                      const a = input1.value 
                     if (a != "" ){
                          
                          input2.value=a
                     }
                     break;
                case 'btn2-2':
                    const b = input2.value 

                    if (b != ""){
                         input1.value=b 
                    }

            }
      })
}