package Ejercicio4;
 
public class Lavadora extends Electrodomestico {

    private double carga ; 

    public Lavadora(double precio_base , String color , char Consumo_energetico , double peso , double carga  ){

           super(precio_base , color , Consumo_energetico , peso );
           this.carga = 5 ; 
    }
     public Lavadora(double precio_base , double peso  ){
         super( precio_base , peso );
    }

    public Lavadora(){
         this.carga = 5 ; 
    }

    
    @Override 

    public double precioFinal(){
         
        if ( carga >= 30 ){ 
        
         return  super.precioFinal() + 50;  
        
        };

        return super.precioFinal() ; 
          
    }



    public String toString(){

        return super.toString() + " con una carga " + carga ;
    }




    





    
}
