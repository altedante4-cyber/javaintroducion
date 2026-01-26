package bloque2cadenas;
import java.util.Scanner;
public class ejercicio25 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String cadena1 = sc.nextLine();
        String cadena2 = sc.nextLine();
        String jutarcadena = "";


        if(cadena1.length() == cadena2.length() ){

        for(int i = 0 ; i < cadena1.length() ; i++ ){
                char a = cadena1.charAt(i) ;
                char p =  cadena2.charAt(i);
                 jutarcadena += a;
                 jutarcadena += p;
                }

        }

        System.out.println(jutarcadena);       
        }

       
    }
    
