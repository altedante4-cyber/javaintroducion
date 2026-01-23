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

        for(int i = 0 ; i < palabras.length ; i++ ){

             String longitudplabras2 = palabras[i];
             logitudplabrass[i] = longitudplabras2.length();

        }

        int contador_media_palabras = 0 ; 

        for (int i = 0 ; i < logitudplabrass.length ; i++ ){
                
             contador_media_palabras += logitudplabrass[i];
        }

        double media = (double) contador_media_palabras / logitudplabrass.length;

        


    }
    
}
