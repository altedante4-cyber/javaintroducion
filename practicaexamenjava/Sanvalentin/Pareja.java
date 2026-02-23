package Sanvalentin;

public class Pareja {

    private Persona persona1;
    private Persona persona2;
    private Regalo regalopersona1;
    private Regalo regalopersona2;


    public Pareja(Persona p1 , Persona p2 ){
        this.persona1 = p1;
        this.persona2 = p2 ; 
        this.regalopersona1 = null;
        this.regalopersona2 = null ; 
    }

    
 public void setRegaloPersona1(Regalo regalo1 ){
      this.regalopersona1   =  regalo1 ; 
 }

 public void setRegaloPersona2(Regalo regalo2 ){
    this.regalopersona2 = regalo2 ; 
}

 public double calcularCosteTotal(){
    double total = 0 ; 
    
    return total += this.regalopersona1.getPrecio() + this.regalopersona2.getPrecio() ; 
 }

 public void mostrarDetalles(){

    System.out.println("Los regalos de la persona " + persona1.toString() + " son " +  regalopersona1.toString() );
    System.out.println("Los regalos de la persona " + persona2.toString() + " son " + regalopersona2.toString() );
    System.out.println(" El total de costetoltal de los regalos es  " + calcularCosteTotal() );

 }

 public String toString() {

    return " la persona " + persona1.toString() + " regalo " + regalopersona1.toString()  + " la persona " + persona2.toString() + " regalo " + regalopersona2.toString() ; 
 }
    
}
