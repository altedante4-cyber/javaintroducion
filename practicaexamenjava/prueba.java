import java.util.Random;
public class prueba {

    public static void main(String[] args){


        Random rand = new Random() ;



        String n = "asdfghjklewqrjtjkggakkfa142349856930690";



        String clave = "";

        for (int i = 0 ; i < 8 ;  i++ ){
            int p = rand.nextInt(n.length());

            for (int j = 0 ; j < n.length() ; j++ ){

                 char q  = n.charAt(j);

                 if ( p == j ){

                     clave += q ;
                     break;
                 }
            }

        }

        System.err.println(clave);


    }
    
}
