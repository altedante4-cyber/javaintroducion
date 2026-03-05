package Sistemadegestiondeempeladosdeunamultitatarea;

public class Desarrollador extends Empleado {
    private String lenguajePrincipal ; 
    public Desarrollador(String nombre , int id , double salarioBase , String lenguaPrincipal ){
        super(nombre, id, salarioBase);
        this.lenguajePrincipal = lenguaPrincipal; 
    }


    @Override

    public double calcularBono(){

        if (lenguajePrincipal.equals("Java")){
            return super.calcularBono() + 500 ; 

        }
             return super.calcularBono() + (super.calcularBono() * 0.10 );


    }


    public String toString(){

        return " El Desarrollador " + super.toString() + " tiene un salario " + calcularBono() + " practica el lenguaje " + lenguajePrincipal ; 
    }


    
    
}
