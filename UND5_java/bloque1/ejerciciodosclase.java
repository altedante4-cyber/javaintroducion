package bloque1;
import java.util.Scanner ; 
public class ejerciciodosclase {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        String palabras [] = new String [10];


        for(int i = 0 ; i < 10 ; i++ ){

             String user = sc.nextLine();

             palabras[i] = user ; 


        }

        int logitudplabrass[] = new int[10];
        int contadorvocales[] = new int [10];
        for(int i = 0 ; i < palabras.length ; i++ ){

             String longitudplabras2 = palabras[i];
             logitudplabrass[i] = longitudplabras2.length();

        }

        int contador_media_palabras = 0 ; 

        for (int i = 0 ; i < logitudplabrass.length ; i++ ){
                
             contador_media_palabras += logitudplabrass[i];
        }

        double media = (double) contador_media_palabras / logitudplabrass.length;


      char vocales [] = {'a','e','i','o','u'};
     for(int i = 0 ; i < palabras.length ; i++ ){
          int contadorvocal = 0;
          String palabraactual = palabras[i];

          for (int j = 0 ; j < palabraactual.length() ; j++){

               char palabra_recorrer = palabraactual.charAt(j);

               for (int q = 0 ; q < vocales.length ; q++ ){

                    if (palabra_recorrer  == vocales[q]){
                         contadorvocal ++;
                         break ; 
                    }
               }

          }

          contadorvocales[i] = contadorvocal;
          
     }

      int palabra_con_mas_vocal = contadorvocales[0];
      int posicion = 0 ; 
      for(int i = 0 ; i < contadorvocales.length ; i++ ){
           System.out.println(contadorvocales[i]);
      }

      for(int i = 0 ; i < contadorvocales.length ; i++ ){

           if (contadorvocales[i] > palabra_con_mas_vocal){
               palabra_con_mas_vocal = contadorvocales[i];
               posicion = i ; 
           }
      }

      // sacar la palabra con mas vocal  de la siguiente manera

      String palabra_con_mas_vocales_str = "";
  

     for (int i = 0 ; i < palabras.length ; i++ ){

           if (i == posicion ){

               palabra_con_mas_vocales_str += palabras[i];
           }
     }
     System.out.println("la palabra es " + palabra_con_mas_vocales_str );
     System.out.println("la longitud de vocales qe tiene es " + palabra_con_mas_vocal );

     int longitudpalabra_mayor = logitudplabrass[0];
     int guardar_posicion_palanbra_mayor = 0 ; 

     for (int i = 0 ; i < logitudplabrass.length ; i++ ){

           if (logitudplabrass[i]> longitudpalabra_mayor){
                longitudpalabra_mayor = logitudplabrass[i];
                guardar_posicion_palanbra_mayor = i ; 
           }

     }

     String palabras_con_mayor_longitud = "";
     for (int i = 0 ; i < palabras.length ; i++ ){

           if ( i == guardar_posicion_palanbra_mayor){
               palabras_con_mayor_longitud += palabras[i];
          }
     }

     System.out.println("la palabra con mayor longitud es " + palabras_con_mayor_longitud);

     //palabras que terminan en consonantes 

     String guardar_palabras = "";
     for (int i = 0 ; i < palabras.length ; i ++ ){

            String palabras_conso = palabras[i];
               boolean termiana_consonante = false ;                    

            for (int j = 0 ; j < palabras_conso.length() ;  j++ ){
               char a = palabras_conso.charAt(palabras_conso.length() - 1 );

                    
                     if ( a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u'  ){

                         termiana_consonante = true ;
                         break;
                    }
            }

             if(!termiana_consonante){
               guardar_palabras += palabras[i] + " ";
          }
          
               
          }

        //mostrarmos las palabras   que termiann en consonantes 
          System.out.println(guardar_palabras);
     
          //eliminancion de duplicados


          String palabras_no_repetidas = "";

          for (int i = 0 ; i < palabras.length ; i++ ){
                String palabra_revisar = palabras[i];
                if(!palabras_no_repetidas.contains(palabra_revisar)){

                     palabras_no_repetidas += palabra_revisar + " ";
                }
          }

          System.out.println("Esto es las palabras sin duplicados  " + palabras_no_repetidas );
     
          // ordenar alfabeticamente las palabras 

          String palabras_no_repetidas_tipo_string [] = palabras_no_repetidas.split(" ");


          int ordenar_palabras [] = new int [palabras_no_repetidas_tipo_string.length];
          
          for(int i = 0 ; i < palabras_no_repetidas_tipo_string.length ; i++ ){

               String palabras_evaluar = palabras_no_repetidas_tipo_string[i];


               for (int j = 0 ; j < palabras_evaluar.length() ; j++ ){
                      char a  = palabras_evaluar.charAt(0)  ; 
                      int b = a;

                      ordenar_palabras[i]= b ; 
                      
               }
          }
     
          for (int i = 0 ; i < ordenar_palabras.length ; i++ ){
                
               for(int j = 0 ; j < ordenar_palabras.length - 1 ; j++ ){

                     if (ordenar_palabras[j] > ordenar_palabras[j+1] ){

                          int temp = ordenar_palabras[j];
                          ordenar_palabras[j] = ordenar_palabras[j+1];
                          ordenar_palabras[j+1] = temp ;
                     }
               }
          }

          char palabras_compar_con_string [] = new char [ordenar_palabras.length];
          for (int i = 0 ; i < ordenar_palabras.length ; i++ ){
                    
                    char a = (char) ordenar_palabras[i];

                    palabras_compar_con_string[i] = a ; 
                   
               }

      // Para cada letra ya ordenada en tu array de caracteres...
for (int i = 0; i < palabras_compar_con_string.length; i++) { // son los caracteres ordenados
    char letraOrdenada = palabras_compar_con_string[i];

    // ...buscamos en el array de palabras cuál empieza por esa letra
    for (int j = 0; j < palabras_no_repetidas_tipo_string.length; j++) {
        String palabraOriginal = palabras_no_repetidas_tipo_string[j];

        // Verificamos si la palabra no está vacía y si su primera letra coincide
        if (palabraOriginal.length() > 0 && palabraOriginal.charAt(0) == letraOrdenada) {
            System.out.println(palabraOriginal);
            
            /* IMPORTANTE: Para evitar que una palabra se repita si hay letras 
               iniciales iguales en tu array de chars, "marcamos" la palabra 
               como ya usada borrándola del array temporal.
            */
            palabras_no_repetidas_tipo_string[j] = ""; // limpia la palabra para que no se vuelva a repetir 

            break; // Saltamos a la siguiente letra del array ordenado
        }
    }
}                  
     }

    }
    

