package Poo_ejercicio2_5;

public class Inmuebles {

    private String direccion ;
    private int num;
    private double precio_base ; 
    private int anios ; 
    public Inmuebles(String direccion , int num , double precio_base , int anios  ){
        this.direccion = direccion ;
        this.num = num ; 
        this.precio_base = precio_base ; 
        this.anios = anios ; 
    }

    public double calcularPrecioInmuble(){
        
        double precioConDescuento = precio_base ;

        if(anios < 15){
            precioConDescuento -= precio_base * 0.01 ; // rebaja 1%
        }else{
            precioConDescuento -= precio_base * 0.02 ; /// rebaja el 2%
        }

        return precioConDescuento ; 

    }

    public double getPrecioBase(){
        return precio_base ;
    }
    public int getanios(){
        return anios ; 
    }

    public int getnumerodemetros(){
        return num ; 
    }
    public String toString(){

        return "La direccion  " + direccion + " el numero es  " + num ; 
    }
}
