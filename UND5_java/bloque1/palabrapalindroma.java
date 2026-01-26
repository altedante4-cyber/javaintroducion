package bloque1;
import java.util.Scanner ; 
public class palabrapalindroma {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese la cadeena");
        String cadena = sc.nextLine();
        String cadena_auxiliar  = "";
        String cadena_sin_espacio = cadena.replace(" ","");

        for (int i = cadena_sin_espacio.length() - 1  ; i >= 0 ; i-- ){
                char c = cadena_sin_espacio.charAt(i);

                cadena_auxiliar += c ; 
            

        }

        if(cadena_sin_espacio.equals(cadena_auxiliar)){
            System.out.println("Es palindroma");
        }else{
            System.out.println("No es palindroma ");
        }

    }
    
}
