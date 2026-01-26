package bloque1;
import java.util.Scanner;
public class ejercicio8bloque1 {
     public static void main(String[] args) {

         Scanner sc = new Scanner(System.in);

         String cadena = sc.nextLine();

         String cadena_invertirda = "";

 // ESTO ES UN MANERA DE HACERLO PERO HAY OTRA MAS SIMPLE DE HACERLO
      /*
         for (int i = 0 ; i < cadena.length() ; i++ ){

             char c = cadena.charAt(i);
             int rango = c ;

             if ( rango >= 65 &&rango <= 90 ){
                  cadena_invertirda += (char)(c + 32);
             }else{
                cadena_invertirda += (char)(c - 32);
             }
             
         }
         System.out.println(cadena_invertirda);
      */

 // OTRA MANERA DE HACERLO MAS SIMPLE 

    for (int i = 0 ; i < cadena.length() ; i++ ){

             char c = cadena.charAt(i);

             if ( c >= 'A' && c <= 'Z'){
                 
                  cadena_invertirda += (char) (c + 32);
             }else{
                cadena_invertirda += (char) (c - 32);
             }
             
         }

         System.out.println(cadena_invertirda);
     
    
    }


    
}
