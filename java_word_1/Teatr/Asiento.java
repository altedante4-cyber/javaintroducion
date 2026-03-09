package Teatr;

public class Asiento {

    private boolean reservado ;
    private String nombreTitular;


    public Asiento(){

         this.reservado = false ;
         this.nombreTitular = null ;
    }

    public boolean estaReservado(){

         return reservado ;
    }

    public void reservar(String nombre ){
         this.reservado = true ;
         this.nombreTitular = nombre ;
    }
    
}
