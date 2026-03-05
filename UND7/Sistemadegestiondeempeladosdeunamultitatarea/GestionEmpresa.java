package Sistemadegestiondeempeladosdeunamultitatarea;

import java.util.Scanner ; 
public class GestionEmpresa {
static Scanner sc = new Scanner(System.in);
    public static void main(String[] args ){


    Empleado [] empleados = new Empleado[6];
    double contador_salario_base_gerentes = 0 ; 
    empleados[0] = new Desarrollador("michael",1,200,"python");
    empleados[1] = new Desarrollador("miki",2,200,"Java");
    empleados[2] = new Desarrollador("axel",3,200,"eclise");
    empleados[3] = new Gerente("loza",4,200,3);
    empleados[4]= new Gerente ("aguilar",5,200,2);
    empleados[5]= new Gerente ("peredo",6,200,4);
  

for (int i = 0 ; i< empleados.length ; i++){

         if(empleados[i] != null && empleados[i] instanceof Gerente  ){
                    Gerente g = (Gerente) empleados[i];
                    System.out.println(g.toString());
                            
         }else if (empleados[i] != null && empleados[i] instanceof Desarrollador   ){
                  Desarrollador d = (Desarrollador) empleados[i];

                  System.out.println(d.toString());
         }else{
            System.out.println("No es ninguno ");
         }
    }


// cacula y muestra cuanto gasta la empresa en total sumando solo los salarios base de los generentes




for (int i = 0 ; i< empleados.length ; i++){

         if(empleados[i] != null && empleados[i] instanceof Gerente  ){
                    Gerente g = (Gerente) empleados[i];
                    contador_salario_base_gerentes += g.calcularBono() ;                                
         }
    }
    
System.out.println("==================== GERENTES BONOS ==================");
System.out.println(contador_salario_base_gerentes);
System.out.println("==================BUSCAR EMPLEADO POR EL ID ===============");
int empleado_id = sc.nextInt();

for (int i = 0 ; i < empleados.length ; i++){

    if(empleados[i] != null && empleados[i].getId() == empleado_id ){
            if (empleados[i] instanceof Gerente ){
                  Gerente g = (Gerente) empleados[i];
                  System.out.println(g.toString());
            }else if (empleados[i] instanceof Desarrollador ){
                  Desarrollador d = (Desarrollador) empleados[i];
                  System.out.println(d.toString());
            }
    }
}
}


    


    
}
