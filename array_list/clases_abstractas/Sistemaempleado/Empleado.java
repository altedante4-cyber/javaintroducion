package Sistemaempleado;

public abstract class  Empleado {
    
    protected String nombre ;
    protected double salarioBase ;
    

    public Empleado(String nombre , double salarioBase){

         this.nombre = nombre ;
         this.salarioBase = salarioBase;
    }

    public abstract double calcularSalario();
    

    public void mostrarInfo(){
         System.out.println("nombre " + nombre  + " el salario base es de  " + calcularSalario() );
    }



}
