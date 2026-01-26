package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio11 {
    public static void main(String[] args){

         Scanner sc = new Scanner(System.in);

         String cadena = "";
         boolean caracterencontrado = false ;
         do{
            String leercadena = sc.nextLine();
            boolean encontrado = false;
            for (int i = 0 ; i < leercadena.length() ; i++ ){
                  char p = leercadena.charAt(i);
                  if ( p == '#'){
                     encontrado = true ;
                     break;
                  }else{
                      cadena += p ; 
                  }

            }

            if(encontrado){
                caracterencontrado = true ; 
            }

         }while(!caracterencontrado);
 
        System.out.println(cadena);


    }
    
}
