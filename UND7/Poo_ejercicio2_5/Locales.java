package Poo_ejercicio2_5;

public class Locales extends Inmuebles {

    private int numero_ventanas;
    // ademas cualquiera de estos inmue
    // bles puede ser nuevo o de segunda mano 

    public Locales(String direccion , int num , double precio_base , int anios , int numero_ventanas){

         super(direccion, num, precio_base , anios );
         this.numero_ventanas = numero_ventanas ;
    }



    @Override

    public double calcularPrecioInmuble(){
         
       double precio = super.calcularPrecioInmuble();

       if(getnumerodemetros() > 50 ){

           precio += getPrecioBase() * 0.01;
       }

       if(numero_ventanas <= 1 ){
          precio -= getPrecioBase() * 0.02;

       }else if(numero_ventanas > 4 ){
          precio += getPrecioBase() * 0.02;
       }

       return precio  ;
        
    }

    
}
