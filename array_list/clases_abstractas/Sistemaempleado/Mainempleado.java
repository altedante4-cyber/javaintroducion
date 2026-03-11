package Sistemaempleado;

public class Mainempleado {

    public static void main(String[] args ){

         Empleado emp1  = new EmpleadoTiempoCompleto("Michael", 4000, 1);
         Empleado emp2 = new EmpleadoMedioTiempo("mika", 2000);

         emp1.calcularSalario();
         emp2.calcularSalario();

         emp1.mostrarInfo();
         emp2.mostrarInfo();
        }
    
}
