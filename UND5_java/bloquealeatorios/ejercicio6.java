package bloquealeatorios;
import java.util.Random ; 
import java.util.Scanner;
public class ejercicio6 {

    public static void main(String[] args ){
         
        Random num = new Random();
       Scanner sc = new Scanner(System.in);
        int contador = 5 ; 
        //generamos el numero azar

        int numero = num.nextInt(101);

        System.out.println(numero);
        while (contador != 0 ){

            System.out.println("Ingrese el numero ");
            int namber = sc.nextInt();

            if (namber != numero){
                System.out.println("vuelva a intentarlo");
                contador -- ;
            }else if(namber == numero){
                  break ;
            }

              
        }

        if ( contador == 0 ){
             System.out.println("ha perdido ");
        }else{
            System.out.println("ha ganado ");
        }


    }
    
}
