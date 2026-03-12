package sistemadegestiondeunatiendaonline;

public class ProductoFisico  extends Producto {

    private double peso , costoEnvio;

    
    public ProductoFisico(int id , String nombre  , double precio , String categoria , double peso , double costoEnvio ){

         super(id, nombre, precio, categoria);
         this.peso = peso ;
         this.costoEnvio = costoEnvio ;
         
    }
}
