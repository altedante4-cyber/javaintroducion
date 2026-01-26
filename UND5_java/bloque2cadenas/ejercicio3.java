package bloque2cadenas;
import java.util.Scanner;
public class ejercicio3 {

    public static void main(String [] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();

        if (cadena.substring(0,1).equalsIgnoreCase("h")) {
            System.out.println("Correcto");
        }else{
            System.out.println("Incorrecto");
        }
         
    }
    
}
