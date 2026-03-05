package poo_ejerccios2_repasoss;

public class EmpleadoBaseMasComision extends Empleado {


    // que incluya tanto un salario base como unas ventas y una comision como salario 
    // que inclay tanto un salario base como unas ventas y una comsion como salario 
    private double ventas , comision ; 

    // entiendo que la comision es el salario 

    public EmpleadoBaseMasComision(String nombre , String apellido , String numero_seguridad_social , double salario_base , double ventas , double comision ){

        super(nombre, apellido, numero_seguridad_social, salario_base);
        this.ventas = ventas;
        this.comision = comision ; 
    }

    @Override

    public double calcularSalario(){

        return super.calcularSalario() + (ventas * comision) ; 
    }


    public String toString(){

        return super.toString() + " | Sueldo Base + Comision " + calcularSalario()   ;  
    }
}
