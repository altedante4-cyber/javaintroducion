package poo_ejerccios2_repasoss;

import java.util.Scanner ; 
public class PruebaEmpleados {
    

    public static void main (String [] args  ){
         Scanner sc  = new Scanner(System.in);
         Empleado listaempleado [] = new Empleado[4];
         int contador = 0 ;
         for (int i = 0 ; i < 2 ; i++ ) {

                System.out.println("Ingrese el nombre del empleado ");
                String nombre = sc.nextLine();
                System.out.println("Ingrese el apelldio del empleado ");
                String apellido = sc.nextLine() ;
                System.out.println("Ingrese el numero de la seguridad social  ");
                String numero_seguridad_social = sc.nextLine() ;
                System.out.println("Ingresee su salario base ");
                double salario_base = sc.nextDouble();
                System.out.println("Ingrese la comision numero de ventas ");
                double ventas = sc.nextDouble() ;
                System.out.println("Numero por comision por ventas ");
                double comision_ventas = sc.nextDouble() ; 

                sc.nextLine();
                listaempleado[i] = new EmpleadoPorComision(nombre, apellido, numero_seguridad_social, salario_base, ventas, comision_ventas);
                contador ++ ; 
            }

            for (int j = 0 ; j < 2 ; j++ ){
  System.out.println("Ingrese el nombre del empleado ");
                String nombre = sc.nextLine();
                System.out.println("Ingrese el apelldio del empleado ");
                String apellido = sc.nextLine() ;
                System.out.println("Ingrese el numero de la seguridad social  ");
                String numero_seguridad_social = sc.nextLine() ;
                System.out.println("Ingresee su salario base ");
                double salario_base = sc.nextDouble();
                System.out.println("Ingrese la comision numero de ventas ");
                double ventas = sc.nextDouble() ;
                System.out.println("Numero por comision por ventas ");
                double comision_ventas = sc.nextDouble() ; 
                sc.nextLine();
                // cuando pasas de un String a un double tienes que limpiar el buffer  

               

                listaempleado[contador] = new EmpleadoBaseMasComision(nombre, apellido, numero_seguridad_social, salario_base, ventas, comision_ventas);
                contador ++ ;

                
            }

            for (int i = 0 ; i < listaempleado.length ; i++ ){

                if(listaempleado[i] != null ){
                System.out.println(listaempleado[i].toString());

                }
            }

                System.out.println("==========ESTOS SON LOS EMPLEADOS EMPELADO POR COMISION ===============  ");

                for (int i = 0 ; i < listaempleado.length ; i++ ){

                    if(listaempleado[i] != null && listaempleado[i] instanceof EmpleadoPorComision ){

                         EmpleadoPorComision e = (EmpleadoPorComision) listaempleado[i];

                            System.out.println(e.toString());
                        }
                            
                
            }



      


   

    }
}
