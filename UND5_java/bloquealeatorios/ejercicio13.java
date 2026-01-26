package bloquealeatorios;
import java.util.Scanner ;
import java.util.Random;
public class ejercicio13 {
    
    public static void main(String[] args){

         Random num = new Random();
         Scanner sc = new Scanner(System.in);

         boolean acertado = false;
            int minimo = 0 ; 
            int maximo = 100 ; 
         do{

            int numero = num.nextInt(maximo - minimo + 1 ) + minimo ;

            System.out.println("el numero que esta pensando es " + numero);

            String opcion = sc.nextLine();
            if(opcion.equals("si")){
                 acertado = true;
            }else{
                 System.out.println("Tu numero es mayor o menor ");
                 opcion = sc.nextLine();
                 if(opcion.equals("mayor")){
                    minimo = numero + 1;                      
                 }else if(opcion.equals("menor")){
                    maximo = numero - 1 ; 


                 }else{
                    acertado = true ; 
                 }
            }

         }while(!acertado);
    }
}
