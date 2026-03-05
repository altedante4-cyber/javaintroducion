package poo_ejerccios2_repasoss;

public class Empleado {
    
    private String nombre , apellido,numero_seguridad_social;
    private double  salario_base; //protected para que los hijos lo vean pero como no  lo vimos no lo poneamos 


    public Empleado(String nombre , String apellido , String numero_seguridad_social , double salario_base ) {

        this.nombre = nombre ;
        this.apellido = apellido ;
        this.numero_seguridad_social = numero_seguridad_social ;
        this.salario_base = salario_base  ;
    }


// nombre mas generico los hijos no siempre calcaular solo la "base"
    public double calcularSalario(){

        return salario_base ; 
    }

    public double getSalarioBase(){
        return  salario_base ; 
    }

    @Override

    public String toString(){

        return nombre + " " + apellido  + " ( NSS: " + numero_seguridad_social + ")";

    }



}
