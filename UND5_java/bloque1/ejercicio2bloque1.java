package bloque1;
import java.util.Scanner ; 
public class ejercicio2bloque1 {

    public static void main(String[] args) {
      
        Scanner sc = new Scanner (System.in);

        String cadena = sc.nextLine();
        String subcadena = sc.nextLine();

        if(subcadenaencontrada(cadena, subcadena)){
            System.out.println("Tiene subcadena");
        }else{
            System.out.println("No tiene subcadena");
        }

    }


    public static boolean subcadenaencontrada(String a , String b ){

        int auxiliar_longitud_b = b.length();
        String auxiliar_a = a.substring(0,auxiliar_longitud_b);

        if (auxiliar_a.equals(b)){
            return true ;
        }

        return false ; 

    }
    
}
