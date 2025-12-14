import java.util.Random;

public static void main(String[] args) {

    String notas [] = {"sol","do","re","mi","fa","sol","la","si"};

    // generar numero aleatoria entre el rangoe de la lista d enotas

    Random num = new Random();
    int gen_ale_notas = 0;

    



    String notas_aleatorias [] = new String [16];

    for (int i = 0 ; i < 16 ; i ++ ){

        gen_ale_notas = num.nextInt(notas.length);

        notas_aleatorias[i] = notas[gen_ale_notas];
       
    }


    
    for (int i = 0 ; i < notas_aleatorias.length ; i++ ){
        
         if( i  != 0 && i % 4 == 0 ){

            System.out.print("|");
         }

         if(notas_aleatorias[0] == notas_aleatorias[15] ){
            System.out.print(notas_aleatorias[i] + " ");
         }

            


         //ultima posicion

         if(i == notas_aleatorias.length - 1){

            System.out.print("||");
         }

         
        

        
       
     

    }






    
 
}