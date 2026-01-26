package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio14 {

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine() ;
        char c = sc.nextLine().charAt(0);

        String auxiliar_string = "";

        for(int  i = 0 ; i < cadena.length() ; i++ ){
              char p = cadena.charAt(i);

              if (p == ' '){
                  auxiliar_string += '*';

              }else{
                 auxiliar_string += p ; 
              }
        }

        System.out.println(auxiliar_string);

         for(int i = 0 ; i < cadena.length() ; i++ ){

              char p = cadena.charAt(i);

              if (p == c ){
                break ;
              }else{
                System.out.print(p);
              }


         }
    }
    
}
