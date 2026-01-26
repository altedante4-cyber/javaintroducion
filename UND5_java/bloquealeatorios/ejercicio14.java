package bloquealeatorios;
import java.util.Random;
public class ejercicio14 {
    public static void main(String[] args ){

        Random num = new Random();
        String notas [] = {"do","re","mi" , "fa" ,"sol" ,"la","si"};
        int filas = (num.nextInt(28)*2);
        for(int i = 0 ; i < filas ; i++ ){

           for (int j = 0 ; j < 4 ; j++ ){
                int elegir_nota = num.nextInt(notas.length);
                System.out.print(notas[elegir_nota] + " ");
                
           }
             if(i == filas -1 ){
                 System.out.print("||");
             }else{
               System.out.print("|");

             }
              

                           
        }
         
    }
    
}
