package VALIDARCONTRASEÑA;
import java.util.Scanner ;
public class ValidadorContraseña {
    public static void main (String[] args ){
        Scanner sc = new Scanner(System.in);

        System.out.println("introduce la contrasena");
        String contrasena = sc.nextLine();

        
         
    }

    public void validarCaracteres(String cont ) throws NumeroCaracter {
         
         if(cont.length() != 8 ){
             throw new NumeroCaracter("Tinene que tener 8 caracteres");
         }

    }

    public void validarNumeros(String cont ) throws TieneNumero{
        
    }
    
}
