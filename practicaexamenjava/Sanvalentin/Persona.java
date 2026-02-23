package Sanvalentin;

public class Persona {

    private String dni , nombre ;

    public Persona(String dni , String nombre ){

         this.dni = dni ; 
         this.nombre = nombre ; 
    }


    public String getdni(){
        return dni ;
    }

    public String getnombre(){
        return nombre ; 
    }

    public String toString(){

        return "Nombre " + nombre  + " DNI " + dni ; 
    }
    
}
