package bloque2cadenas;
import java.util.Scanner ;

public class ejercicio20 {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        String usuario_cadena = sc.nextLine();
        String cadena [] = usuario_cadena.split(" ");

        String palabra_longitud = "";
        for (int i = 0 ; i < cadena.length ; i++ ){

            String palabra = cadena[i];

            if(palabra.length() <= 3 ){
                  palabra_longitud += palabra + " ";
            }

        }

        int cuantas_palabras = palabra_longitud.split(" ").length;
        System.out.println(cuantas_palabras);
    }
    
}
