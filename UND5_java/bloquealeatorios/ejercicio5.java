package bloquealeatorios;
import java.util.Random;
public class ejercicio5 {
    public static void main(String[] args ){
         
        Random num = new Random();

        int maximo = 100 ;
        int minimo = 199 ; 
        int sumar = 0 ; 
        for (int i = 0 ; i < 50 ; i ++ ){

                int numero = num.nextInt(100) + 100 ;
                
                if ( numero > maximo ){
                      maximo  = numero ; 
                }else if ( numero < minimo ){

                      minimo = numero ; 
                }

                sumar += numero ; 

        }
        double media = (double) sumar / 50;

        System.out.println("la media es la siguietne" + media );

        System.out.println("maximo es " + maximo);
        System.out.println("el minimo es "+ minimo );

    }
}
