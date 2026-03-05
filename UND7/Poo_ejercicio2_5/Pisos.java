package Poo_ejercicio2_5;

public class Pisos extends Inmuebles  {

    // cualquiera de estos inmubels puede ser nuevo o de segunda mano 

    private int numero_piso;

        

        
    public Pisos (String direccion , int num , double precio_base , int anios , int numero_piso){

         super(direccion, num , precio_base , anios );
          this.numero_piso = numero_piso ;         
    }

    

        @Override

    public double calcularPrecioInmuble(){
        
        double precio = super.calcularPrecioInmuble() ;

        if(numero_piso >= 3 ){
             precio += getPrecioBase()  * 0.03 ;
        }
        return precio ; 

        
        
    }
}
