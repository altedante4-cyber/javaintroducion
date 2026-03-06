package EJERCICOI2_8;

public class PlatoPrincipal extends ItemMenu{

    private String ingredientes [] = new String [10];
    private int tiempoPreparacion ;
    private boolean esVegetariano ;  

    public PlatoPrincipal(String nombre , String descripcion , double precioBase , int tiempoPreparacion){
         super(nombre, descripcion, precioBase);
         this.tiempoPreparacion = tiempoPreparacion ; 
    }

    
 @Override 

  public double calcularPrecioFinal(){
      if(esVegetariano) return super.calcularPrecioFinal() + 2.0 ; 
    
      return super.calcularPrecioFinal();
    }

}
