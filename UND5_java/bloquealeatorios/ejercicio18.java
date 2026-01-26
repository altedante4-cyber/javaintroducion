package bloquealeatorios;
import java.util.Scanner ;
import java.util.Random; 
public class ejercicio18 {
    public static void main (String[] args ){
 Random num = new Random();
    Scanner sc = new Scanner(System.in);

    int intentos = 3 ; 
    boolean acertaado = false ;
    int number = num.nextInt(51) + 50 ; 
    System.out.println(number);
    while(intentos > 0 ){

         System.out.println("Ingrese el numero ");
         int opcion = sc.nextInt();

         if(opcion == number ){
             acertaado = true;
             break;
         }else{
            System.out.println("Vuelva a intentarlo ");
             intentos -- ;
         }
    }

    if(acertaado) {
        System.out.println("Has acertado");
    }else{
        System.out.println("No has acertado  ");
    }

    }
   


}
