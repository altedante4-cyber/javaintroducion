package bloque2cadenas;
import java.util.Scanner  ;
public class ejercicio27 {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();

        String cadena_split [] = cadena.split(" ");

        for(int i = 0 ; i < cadena_split.length -1 ; i++ ){

            System.out.println(cadena_split[i]);
             
        }
        

    }
    
}
