package bloque2cadenas;
import java.util.Scanner ; 
public class ejercicio23 {
    
    public static void main(String[] args) {
         
         Scanner sc = new Scanner(System.in);

         char vocales [] = {'a','e','i','o','u'};
         String cadena = sc.nextLine();
         String cadena_array [] = cadena.split(" ");
         int contador_vocales [] = new int[cadena_array.length];

         for(int i = 0 ; i < cadena_array.length ; i++ ){

              String palabra = cadena_array[i];

              for(int j = 0 ; j < palabra.length(); j++ ){
                      char c = palabra.charAt(j);
                      boolean encontrado = false ; 

                  for (int k = 0 ; k < vocales.length ; k++ ){
                        
                         if(c == vocales[k]){
                             encontrado = true;
                             break;
                         }
                       
                  }
                  if(encontrado){
                     contador_vocales[i] ++;
                  }
              }
         }
            
         int contador_vo = 0 ; 
         for(int i =0 ; i < contador_vocales.length ; i++ ){
                if(contador_vocales[i] > 3 ){
                    contador_vo ++ ; 
                }
        }
         System.out.println(contador_vo);
         
    }
}
