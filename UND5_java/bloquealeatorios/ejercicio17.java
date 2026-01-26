package bloquealeatorios;
import java.util.Scanner ;
import java.util.Random; 
public class ejercicio17 {
    public static void main(String[] args ){
 
         Random num = new Random();
        Scanner sc = new Scanner(System.in);

        int intentos = 3  ;
        boolean acertado = false ;
        int namber = num.nextInt(10) + 1 ;
        System.out.println(namber);
        while(intentos > 0 ){
              System.out.println("Ingrese el numero "); 
                int opcion = sc.nextInt();

                if(namber == opcion){
                    acertado = true;
                    break;
                }else{
                     System.out.println("Vuelva a intentarlo");
                     intentos -- ;
                }

            }

            if(acertado){
                System.out.println("Ha ganado la partida");
            }else{
                System.out.println("Ha perdido la patidad") ;
            }


    }
    
}
