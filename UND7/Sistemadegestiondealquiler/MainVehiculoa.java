package Sistemadegestiondealquiler;

import java.util.Scanner ; 
public class MainVehiculoa {

        static Scanner sc = new Scanner(System.in);
        static Flota flota = new Flota();
    public static void main(String[] args) {

     int opcion = 0 ; 

     do{
            System.out.println("\n--- SISTEMA DE ALQUILER ---");
            System.out.println("1. Registrar Coche");
            System.out.println("2. Registrar Moto");
            System.out.println("3. Registrar Furgoneta");
            System.out.println("4. Ver Vehículos y Ganancias");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");

            opcion = sc.nextInt();
            sc.nextLine() ; 

     switch (opcion) {
                case 1: case 2: case 3:
                    registrarVehiculo(opcion);
                    break;
                case 4:
                    flota.mostrarFlota();
                    break;
                case 5:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }

     }while(opcion != 5 );

     //metodo Auxiliar para evitar repetir codigio

   

    }

    // aqui aprendi a como con solo un parametro digamos si de vehiculo deciendo moto , coche   , furgoneta declaramos al padre y ya 
    // y segun digamo el usuario el tipo es 1 que es coche entonces  coche deciende de vehiculo  sabiendo el padre podemos contruir a los hijos 

      public static void registrarVehiculo(int tipo ){
        System.out.print("Ingrese la matrícula: ");
        String mat = sc.nextLine();
        System.out.print("Ingrese el modelo: ");
        String mod = sc.nextLine();
        System.out.print("Ingrese la tarifa base: ");
        double tar = sc.nextDouble();

        Vehiculo v ;  // declaramos el padre (Polimorfismo)

        if(tipo == 1 ) v = new Cochae(mat, mod, tar);
        else if (tipo == 2 ) v = new Mato(mod, mat, tar);
        else v = new Furgoneta(mat, mod, tar);

        if(flota.agregarVehiculo(v)){
             System.out.println("Vehiculo registrao con existo");
             System.out.println("Cuantos dias desea simular de alquiler ? ");
             int dias = sc.nextInt();
             System.out.println("El precio estimado es : " + v.calcularAlquiler(dias));

        }else{
            System.out.println("Error: No se pudo agregar(FLota llena ");
        }

     }


    
}
