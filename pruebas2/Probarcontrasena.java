package pruebas2;
import java.util.Scanner ;
public class Probarcontrasena {
    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el tamno de la contrasena");
        int tamano = sc.nextInt();
        System.out.println("Ingrese el tamno que quire para las password");
        int tamno_password = sc.nextInt();
        Password [] contrasena = new Password[tamano]; 

        boolean [] contrasena_valida = new boolean[tamano];

        System.out.println("La longitud del passwrod es  " +  tamano );
        for (int i = 0 ; i < tamano ; i++ ){

              contrasena[i]=new Password(tamno_password);  
              
              contrasena_valida[i]=contrasena[i].esFuerte();
        }



        for (int i = 0 ; i < tamano ;i++ ){
            
            System.out.println(contrasena[i] + "es" + contrasena_valida[i]);
        }

    }
    
}
