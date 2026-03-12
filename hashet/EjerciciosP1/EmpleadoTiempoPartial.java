package EjerciciosP1;

public class EmpleadoTiempoPartial extends Empleado {

    public EmpleadoTiempoPartial(int id , String nombre , String departamento , double salarioBase ){
         super(id, nombre, departamento, salarioBase);

    }

      @Override
     public double calcularSalarioFinal(){
         
        return  salarioBase + (salarioBase * 0.05 );
         
     }

    
}
