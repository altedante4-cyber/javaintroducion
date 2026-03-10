public class EmpleadoBaseMasComision extends Empleado {

    private double num_ventas , comision ;
    public EmpleadoBaseMasComision(String nombre , String apellido , String numero_seguridad_social , double salario_base , double num_ventas , double comision ){

         super(nombre, apellido, numero_seguridad_social, salario_base);
            this.num_ventas  = num_ventas;
            this.comision = comision;
        }


        @Override

        public double SalarioCombrarEmpleado(){

            return super.SalarioCombrarEmpleado() +  num_ventas + comision ; 
        }



        public String toString(){

            return "El empleadoBaseMascomision " + super.toString() + " tienne un numero de ventas " + num_ventas  + " su comision es  " + comision ;  
        }


    }
