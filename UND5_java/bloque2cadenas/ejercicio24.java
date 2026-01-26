package bloque2cadenas;
import java.util.Scanner;
public class ejercicio24 {
    public static void main(String[] args){

         Scanner sc = new Scanner(System.in);
         String cadena = sc.nextLine() ; 

         String cadena_sin_espacios [] = cadena.split(" ");
            // ojo con este ejercicio 

            
         for (int i = 0 ; i < cadena_sin_espacios.length ; i++ ){

                    String palabra = cadena_sin_espacios[i];
                    String primera_letra = palabra.substring(0 ,1).toUpperCase();
                    String letra_restante = palabra.substring(1);
                    String pe = primera_letra + letra_restante ; 
                    System.out.println(pe);

                    


         }
    }
    
}
