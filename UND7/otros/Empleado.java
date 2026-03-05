package otros;
public class Empleado{

    private String nombre ;
    private double sueldo_base;

    public Empleado(String nombre , double suedo_base ){

        this.nombre=nombre;
        this.sueldo_base=suedo_base;
    }







    //este metodo sera sobrreesccriot por los hijos (polimorfismo)
    public double calcularSueldo(){

        return sueldo_base;
    }

    public String getNombre(){
        return nombre ; 
    }


    public double getSueldo(){
        return sueldo_base ; 
    }
    
}