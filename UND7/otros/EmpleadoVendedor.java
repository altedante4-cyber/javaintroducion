package otros;
public class EmpleadoVendedor extends Empleado {
    
    private double comision ;

     // esta clase debe tener un atributo adicional comisioon su metod calcularSueldo() debe sumar el sueldoBase mas la comision

     public EmpleadoVendedor(String nombre , double sueldo_base , double comision ){

        super( nombre , sueldo_base );
        this.comision = comision ;
     }


    public double getComision(){
        return comision;
    }


     @Override

     public double calcularSueldo(){

        return getSueldo() + comision ; 
     }

     // PROBLEMA COMUN que tube en la parte de getSueldo estaba poniendo sueldo_base pero no se podia poor que el metodo era privado

     // el problema esta en la vaariable sueldo_basee dentro de la clase hija para que el coidgo funcione correcctamente debemos revisar el accesos
     // de la variabels en la clase padre aqui tienes la corecion depuera y la explicacion de poque falla
     // el error de visibilidad
     // si en la clase empleado (el padre) definiste la varibale ocmo private doubble sueldo_+base
     // la clase hija no  puede verla directamente  aunque la herea
     // solucion a recomendad cambia private por protected en la clase padre esto permite que los hijos usen pero el resto del mundo no 
     // solucin ob usa el metodo getter ( getsueldbase()) para obtener el valor


}
