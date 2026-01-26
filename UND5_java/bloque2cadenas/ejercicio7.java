package bloque2cadenas;
import java.util.Scanner;
public class ejercicio7 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();
        char c = sc.nextLine().charAt(0);

        int posicion = 0 ;
        boolean encontrado = false ;

        for(int i = 0 ; i < cadena.length() ; i++ ){

             char p = cadena.charAt(i);

             if (p == c ){
                encontrado = true ;
                posicion = i ;
                break;
             }
        }

        if(encontrado){

            System.out.println("Se encuentra en la poscion " + posicion);
        }else{
            System.out.println("No se encuentro el caracter");
        }

        // ahora usando el index of 

        int poscion_caracter = cadena.indexOf(c);
        
        if (poscion_caracter != -1 ){
             System.out.println("Utilizando indexof la posicion es la siguiente " + poscion_caracter);
        }else{
            System.out.println("posicion no encontrado utilizando index of");
        }


    }
    
}
