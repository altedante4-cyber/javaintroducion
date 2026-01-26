package bloque1;
import java.util.Random ; 
public class DNI {
    public static void main(String[] args ){

        Random num_dni = new Random();

        String letras_dni = "a b c d e f g h i j k m n o p q r s t u w x y z";
        String letras_dni_array [] = letras_dni.split(" ");


        String numeros = "";
        int num = num_dni.nextInt(letras_dni_array.length);

        for (int i = 0 ; i < 8 ; i ++ ){

            int namber = num_dni.nextInt(1,9+1);
            numeros += namber ; 

        }

        numeros += letras_dni_array[num] ;

        System.out.println(numeros);
        



    }
    
}
