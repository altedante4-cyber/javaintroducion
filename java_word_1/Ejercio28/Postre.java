package Ejercio28;

public class Postre extends ItemMenu { 

    private int calorias;
    private boolean contieneGluten;


    public Postre(String nombre , String descripcion , double precioBase , int calorias) {
     
           super(nombre, descripcion, precioBase);
           this.calorias = calorias ;
           this.contieneGluten = false ;
    }


    @Override

    public double calcularPrecioFinal(){

         if (!contieneGluten){return super.calcularPrecioFinal() +  1.0 ;  }
   
   
        return super.calcularPrecioFinal()    ;
     }

     
     


    

}