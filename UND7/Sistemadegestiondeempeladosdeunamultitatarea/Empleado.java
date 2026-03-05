package Sistemadegestiondeempeladosdeunamultitatarea;

public class Empleado {

   private String nombre ;
   private int id ; 
   private double salarioBase  ; 

    public Empleado(String nombre , int id , double salarioBase ){

        this.nombre = nombre ;
        this.id = id ; 
        this.salarioBase  = salarioBase ; 
    }

   public double calcularBono(){
           return salarioBase ;
   }

   public int getId(){
    return id ; 
   }


   public String toString(){

        return " ID "+ id + " Nombre " + nombre ; 
   }



    
}
