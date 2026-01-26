package bloquealeatorios;
import java.util.Random;
public class ejercicio1 {

    public static void main(String[] args ){

        Random num = new Random();

        for(int i =0 ; i < 20 ; i++ ){
             
            int numeros = num.nextInt(10);
            
            System.out.println(numeros);
        }
         
    }
    
}
