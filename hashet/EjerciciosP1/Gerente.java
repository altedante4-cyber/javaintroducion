package EjerciciosP1;

public class Gerente extends EmpleadoTiempoCompleto {

    public Gerente(int id , String nombre , String departamento , double salarioBase ){

         super(id, nombre, departamento, salarioBase);

    }
    

      @Override
     public double calcularSalarioFinal(){
         
        return  salarioBase + (salarioBase * 0.20 );
         
     }

     
}
