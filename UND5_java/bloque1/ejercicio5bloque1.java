package bloque1;
import java.util.Scanner ; 
public class ejercicio5bloque1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String cadena = sc.nextLine();

        String cadena_separada [] = cadena.split(" ");
        String cadena_mayuscula = "";
        for (int i = 0 ; i < cadena_separada.length ; i++ ){

              String palabra = cadena_separada[i];
              String primera_palabra = palabra.substring(0,1);
              String palabras_restantes = palabra.substring(1);
              cadena_mayuscula += primera_palabra.toUpperCase();
              cadena_mayuscula += palabras_restantes + " ";

        }

        System.out.println(cadena_mayuscula);

    }
    
}
