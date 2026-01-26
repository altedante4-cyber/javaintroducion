package bloque1;
import java.util.Scanner ; 
public class ejercicio45 {

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese la cadena");
        String cadena = sc.nextLine();
        System.out.println("Ingrese el primer caracter");
        char c = sc.nextLine().charAt(0);
        System.out.println("Ingrese el segundo caracter");
        char p = sc.nextLine().charAt(0);


        if(encontrarletra(cadena, c)){
            String cadenanueva = cadena.replace(c, p);
            System.out.println(cadenanueva);
        }else{
            System.out.println("No encontrado");
        }




    }


    public static boolean encontrarletra(String a  , char c){

        for(int i = 0 ; i < a.length() ; i++ ){
            char q = a.charAt(i);

            if (q == c){
                return true ;
            }
            
        }

        return false ; 
    
}
}