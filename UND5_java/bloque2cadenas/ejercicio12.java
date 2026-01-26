package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio12 {

    public static void main(String[] args ){


    Scanner sc = new Scanner(System.in);

    String cadena = sc.nextLine();
    char vocales [] = {'a','e','i','o','u'};
    String vocales_encontradas = "";


    for (int i = 0 ; i < cadena.length() ; i++ ) {
         
           char p  = cadena.charAt(i);
            boolean encontradovocal = false ;
           for (int j = 0 ;  j < vocales.length ; j++ ){
                    if (p == vocales[j]){
                         encontradovocal = true;
                         break;
                    }                    
             
           }
           if(encontradovocal){
              vocales_encontradas += p ; 
           }




        }

        System.out.println(vocales_encontradas.length());
    }




    
}
