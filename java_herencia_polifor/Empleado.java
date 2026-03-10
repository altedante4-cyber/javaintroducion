public class Empleado{

    private String nombre ,apellido , numero_seguridad_social ;
    private double saliro_base  ; 

    public Empleado(String nombre , String apellido , String numero_seguridad_social , double salario_base) {

            this.nombre = nombre ; 
            this.apellido = apellido ; 
            this.numero_seguridad_social = numero_seguridad_social; 

    }


    // crea losmetodos habitulaes y uno

    public double SalarioCombrarEmpleado(){

        return saliro_base ; 
    }


    
    public String toString(){

        return "el nombre  " + nombre + " el apellido  " + apellido + " el numero de la seguridad social " + numero_seguridad_social + " su salario es " + SalarioCombrarEmpleado()  ; 
    }

    
}

