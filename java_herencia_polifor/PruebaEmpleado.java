import java.util.Scanner ; 
public class PruebaEmpleado {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args ){
            Empleado empleados [] = new Empleado[10];

        int opcion;
        int contador = 0 ; 

        do{ 
            System.out.println("1.REGISTRAR EMPLEADO");
            System.out.println("2.CONSULTAR EMPLEADOS EN LA PLANTILLA");
            System.out.println("3.ELIMINAR UN EMPLEADO DE LA  PLANTILLA ");
            System.out.println("4.Salir");

            opcion = sc.nextInt(); 

            sc.nextLine();

            switch (opcion) {
                case 1:
                    RegistrarEmpleado(); 
                    
                    break;
            
                default:
                    break;
            }

        }while(opcion != 4 );
         
    }

    public static void RegistrarEmpleado(){
          System.out.println("INGRESE EL TIPO DE EMPLEADO QUE DESEA REGISTRAR 1.EMPLEADO-BASE-MAS-COMISION , 2.EMPELADO-POR-COMISION ");
          int op = sc.nextInt() ;

          
    }
}
