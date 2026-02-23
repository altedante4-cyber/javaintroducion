package Sistemadevideoclub;

public class Cliente {
    private String dni , nombre;


    public Cliente(String dni , String nombre ){

         this.dni = dni ;
         this.nombre = nombre ; 
    }



    public String toString(){

        return "Nombre : " + nombre + " DNI " + dni ; 
    }
}
