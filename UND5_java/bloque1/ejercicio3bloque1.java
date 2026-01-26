package bloque1;
import java.util.Scanner ; 
public class ejercicio3bloque1 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        String cadena = sc.nextLine() ;
        String caracter = sc.nextLine();


        if(esuncaracter(caracter)){

            char b = caracter.charAt(0);

            int resultado = encontradocaracter(cadena, b) ;

            System.out.println(resultado );

            
        }else{
            System.out.println("No es un caracter ");
        }


    }

    public static boolean esuncaracter(String b){

        if (b.length() != 1 ){

            return false ;
        }                 

    return true ; 
    }

    public static int encontradocaracter(String a , char p ){

        int contadorcarateres = 0 ;

        for(int i = 0 ; i < a.length() ; i++ ){
             
             char k = a.charAt(i);

             if ( k==  p ){

                contadorcarateres ++;
             }
        }

        return contadorcarateres ; 
    }
    
}
