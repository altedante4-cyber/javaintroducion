package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio15 {

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine() ;
        char c = sc.nextLine().charAt(0);
        String cadena_auxiliar = "";

        for (int i = 0 ; i < cadena.length()  ; i++ ){
                int p = cadena.indexOf(" ");
                 char k = cadena.charAt(i);
                if ( p == i ){
                     cadena_auxiliar += '*';

                }else{
                    cadena_auxiliar += k; 
                }
        }
        System.out.println(cadena_auxiliar);

        for (int i = 0 ; i < cadena.length() ; i++ ){

             int primercaracter = cadena.indexOf(c);
            char k = cadena.charAt(i);
             if ( i == primercaracter ){
                break;
             }else{
                 System.out.print(k);
             }
        }

    }
    
}
