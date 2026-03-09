package Supercalculadora;

public class Operacion {

    private String tipo ;
    private double resultado ;
    private String fecha ;



    public Operacion(String tipo , double resultado , String fecha ){
         this.tipo = tipo ;
         this.resultado = resultado ;
         this.fecha = fecha ;
    }
    
    public void setTipo(String tipo ){

         this.tipo = tipo ; 
    }

    public void mostrarDetalle(){
         
        // mostrar el resmen de la operación

        System.out.println("tipo de operacion " + tipo + "el resultado es " + resultado  + "la fecha es " + fecha );
    }
}




