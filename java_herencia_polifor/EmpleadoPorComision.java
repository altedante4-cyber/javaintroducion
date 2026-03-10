public class EmpleadoPorComision extends Empleado {
  
    private double num_ventas   ; 
    private double num_comision_por_ventas ; 

    public EmpleadoPorComision(String nombre , String apellido , String numero_seguridad_social , double salario_base , double num_ventas , double num_comision_por_ventas ){
        super(nombre , apellido , numero_seguridad_social , 0 );
        this.num_ventas = num_ventas ;
        this.num_comision_por_ventas =num_comision_por_ventas ;
    }


    @Override 

    // salario que cobra el trabajador 
    public double SalarioCombrarEmpleado(){

        return super.SalarioCombrarEmpleado() + num_ventas * num_comision_por_ventas ;
    }





     public String toString(){

        return "El empleadoPorComision " + super.toString() + " el numero de ventas " + num_ventas + " numero comision por ventas " + num_comision_por_ventas ;  
     }




    
}
