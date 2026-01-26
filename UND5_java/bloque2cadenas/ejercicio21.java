package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio21 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        String cadena = sc.nextLine();
        String limpiar_cadena = cadena.trim();
        int separar_cadena = limpiar_cadena.split("( |\\.|\\,|;|:|\\\")+").length;
        System.out.println(separar_cadena);
    }
    
}
