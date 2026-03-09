package Ejercio28;

public class ItemMenu {

    private String nombre , descripcion ;
    private double precioBase ; 

    public ItemMenu(String nombre , String descripcion , double precioBase ){

         this.nombre  = nombre ;
         this.descripcion = descripcion ;
         this.precioBase = precioBase ; 
    }

    public double  calcularPrecioFinal(){
        return precioBase ; 
    }

    public String toString(){
        return " El nombre es  " + nombre + "  la descripcion " + descripcion  + "el precio base es  " + precioBase ; 
    }

    
}
