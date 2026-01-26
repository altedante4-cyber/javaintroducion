package bloque2cadenas;
import java.util.Scanner ; 

public class ejercicio9 {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();
        char c = sc.nextLine().charAt(0);
        int contador = 0 ; 
        boolean encontrado = false ; 
        for (int i = 0 ; i < cadena.length() ; i++ ){
             char  p = cadena.charAt(i);

             if ( p == c ){
                encontrado = true;
                contador ++ ;
             }
        }

        if(!encontrado){
            System.out.println("Letra no encontrada");
        }else{
        System.out.println(contador);

        }


    }
    
}
