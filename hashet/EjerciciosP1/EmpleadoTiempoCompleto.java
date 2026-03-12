package EjerciciosP1;

public class EmpleadoTiempoCompleto  extends Empleado {

     public EmpleadoTiempoCompleto(int id , String nombre , String departamento , double salarioBase ){

         super(id,nombre,departamento,salarioBase);

     }


     @Override
     public double calcularSalarioFinal(){
         
        return  salarioBase + (salarioBase * 0.15 );
         
     }

   

    
}
