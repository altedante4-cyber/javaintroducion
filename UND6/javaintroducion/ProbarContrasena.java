package javaintroducion;
import java.util.Scanner ; 
public class ProbarContrasena {
    
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el numero del array");
        int num = sc.nextInt();
        System.out.println("INgrese la longitud de la contrasena ");
        int longitud_contrasena = sc.nextInt(); 


        Password [] mio = new Password[num];
        boolean password_fuerte [] = new boolean[mio.length];


        

        // para que no cree el mismo objeto en las mismas poscionees 
        // tengo que crear el objeto dentro del bucle haci cada objeto ocupa una posicion en la memoria 
         

        // buenas praciticas mantener un contador aparte para los objetos para que no nosde el error de nullpointer el length en los objetos es peligros o 

        for ( int i = 0 ; i < mio.length ; i++ ){

             mio[i] = new Password(longitud_contrasena); // a esto se le llama instanciar el  objeto
             password_fuerte[i] = mio[i].esFuerte();
        }


        // mostrarmos el array de objetos 

        for(int i= 0 ; i < mio.length  ; i++ ){
            System.out.println(mio[i] + "es" + password_fuerte[i]);
        }








    }
    
}
