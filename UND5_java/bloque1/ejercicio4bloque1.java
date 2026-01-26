package bloque1;
import java.util.Scanner ; 
public class ejercicio4bloque1 {
    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();
        int contador_palabras = 0 ;

        String cadena_separada [] = cadena.split(" ");


        int contador = cadena_separada.length;

        for(int i = 0 ; i < cadena_separada.length ; i++ ){

             String palabras = cadena_separada[i];

             contador_palabras ++;
        }


        System.out.println(contador_palabras);
    }
    
}
