package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio17 {
    public static void main (String[] args){

        Scanner sc = new Scanner(System.in);
        String cadena = sc.nextLine();
      // manera mas rapida es la siguiente
      // ojoooooooooooooooooooooooooooooooo
      String resultado = cadena.replaceAll("[aeiou]", "");

      System.out.println(resultado);

    }
    
}
