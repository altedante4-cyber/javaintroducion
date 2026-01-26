package bloquealeatorios;
import java.util.Random;
public class ejercicio9 {

    public static void main(String[] args) {

        Random numeros = new Random();
        int num =0 ;
        int contador = 0 ; 
        while(num != 24){
            num = (numeros.nextInt(101)*2);
            contador ++;
            System.out.println(num);
        }

        System.out.println("Se tuvieron que generar " + contador + "numeros");

    }
    
}
