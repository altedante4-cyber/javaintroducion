package poo_ejerccios2_repasoss;

public class EmpleadoPorComision extends Empleado {

    private double numero_ventas  , comision_ventas ; 


    public EmpleadoPorComision(String nombre , String apellido , String numero_seguridad_social , double salario_base, double numero_ventas , double comision_ventas ){
        super(nombre, apellido, numero_seguridad_social, 0); // pasamos 0 al salariobase del padre segun el enunciado
        this.numero_ventas = numero_ventas;
        this.comision_ventas = comision_ventas ; 
    }



    @Override


    public double calcularSalario(){

        return numero_ventas * comision_ventas  ;
    }



    // redefiniir para ambas clases la forma en la que se  devuele el salario que cobra cada uno

    public String toString(){
        
        return super.toString() + " | Sueldo por Comision " + calcularSalario() ; 
    }



    
}
