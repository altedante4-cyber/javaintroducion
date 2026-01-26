package bloque1;
import java.util.Scanner ; 
public class ejercicio6bloque1 {
    public static void main(String[] args ){

        Scanner  sc = new Scanner(System.in);

        String cadena = sc.nextLine();
        String cadena_invertida = "";

        for (int i = cadena.length() - 1 ; i >= 0 ; i-- ){

             char c = cadena.charAt(i);

             cadena_invertida += c ; 
        }

        System.out.println(cadena_invertida);

    }
    
}
