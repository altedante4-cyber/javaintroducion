package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio16 {
    
    public static void main(String [] args ){

         Scanner sc = new Scanner(System.in );

         char vocales [] = {'a','e','i','o','u'};
         String cadena = sc.nextLine() ;
        for(int i = 0 ; i < cadena.length() ; i++ ){
               boolean vocal = false ;
               char k = cadena.charAt(i);

             for (int j = 0 ; j < vocales.length ; j++ ){
                 
                   if ( vocales[j] == k ){
                       vocal = true;
                       break;
                   }
             }
             if(!vocal){
                System.out.print(k);
            }
               
        }


    }
    
}
