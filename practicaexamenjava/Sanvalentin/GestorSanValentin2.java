
package Sanvalentin;
import java.util.Scanner ; 
public class GestorSanValentin2 {
    static Scanner sc = new Scanner(System.in);
    static Pareja [] parejas = new Pareja[10];
    static int contador = 0 ; 
    public static void main(String[] args) {

        int opcion ; 

        do{

            System.out.println("1.Agregar pareja y sus regalos ");
            System.out.println("2.Mostrar detalles de las parajas y sus regalos ");
            System.out.println("3.Salir del programa ");
            opcion = sc.nextInt();

            sc.nextLine();
            switch (opcion) {
                case 1:
                    agregarPareja();
                    
                    break;
                case 2 :
                    mostrarDetallesParejas();
                    break ;
            
                default:
                    break;
            }
        }while(opcion != 3 );
    }


    public static  void agregarPareja(){

        System.out.println("Ingrese el dni ");
        String dni  = sc.nextLine();
        System.out.println("Ingrese el nombre ");
        String nombre = sc.nextLine();
        Persona p1 = new Persona(dni, nombre);

        System.out.println("Ingrese el dni ");
        String dni2  = sc.nextLine();
        System.out.println("Ingrese el nombre ");
        String nombre2 = sc.nextLine();
        Persona p2 = new Persona(dni2, nombre2);


        System.out.println("Introduce  el nombre del regalo ");
        String nombre_regalo = sc.nextLine() ;
        System.out.println("Introduce la descripcion del regalo ");
        String descripcion = sc.nextLine() ;
        System.out.println("Introduce el precio del regalo ");
        double precio_regalo = sc.nextDouble() ; 

        Regalo regalo_nuevo1 = new Regalo(nombre_regalo, descripcion, precio_regalo);

        sc.nextLine();

        System.out.println("Introduce  el nombre del regalo ");
        String nombre_regalo2 = sc.nextLine() ;
        System.out.println("Introduce la descripcion del regalo ");
        String descripcion2 = sc.nextLine() ;
        System.out.println("Introduce el precio del regalo ");
        double precio_regalo2 = sc.nextDouble() ; 

        Regalo regalo_nuevo2 = new Regalo(nombre_regalo2, descripcion2, precio_regalo2);


        Pareja parejanueva = new Pareja(p1, p2);
        parejanueva.setRegaloPersona1(regalo_nuevo1);
        parejanueva.setRegaloPersona2(regalo_nuevo2);


        if(contador < parejas.length ){
            parejas[contador++ ] = parejanueva ; 
            System.out.println("Se agrego correctamente a la pareja ");
        }else{
            System.out.println("No se pudo agregar a la pareja ");
        }



    }

    
        public static void mostrarDetallesParejas(){
            for(int i = 0 ; i < contador  ; i++ ){
                 System.out.println( parejas[i].toString());
            }

        }
}
