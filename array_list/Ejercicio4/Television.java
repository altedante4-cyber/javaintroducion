package Ejercicio4;

public class Television extends Electrodomestico {

    private int pulgadas ; 
    private boolean sintonizador ; 



    public Television(double precio_base , String color , double peso ,char Consumo_energetico , double pulgadas  ){

           super(precio_base , color , Consumo_energetico , peso );
           this.pulgadas = 20 ; 
           this.sintonizador = false ;  
    }
     public Television(double precio_base , double peso  ){
         super( precio_base , peso );
    }

    public Television(){
         this.pulgadas = 20; 
    }


    public int getpulgadas(){

        return pulgadas ;
    }
    public boolean getsintonizador(){
        return sintonizador ;
    }


    @Override
    public double precioFinal() {
    

        if(pulgadas >= 40 ){
            return super.precioFinal() + (super.precioFinal() * 0.30);

        }

        if (sintonizador){
            return super.precioFinal() + 50 ; 
        }

        return super.precioFinal() ;

    }
    

    public String toString(){
        String mostrar = "";
        if (sintonizador){
            mostrar += "tiene sintonizador";

        }else{
            mostrar += "no tiene sintonizador";
        }
        return super.toString() + "pulgadas " + pulgadas + " sintonisador " + mostrar ;   
    }
}
