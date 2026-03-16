package sistemadegestiondeunatiendaonline;

public class ProductoFisico  extends Producto {

    private double peso , costoEnvio;

    
    public ProductoFisico(int id , String nombre  , double precio , String categoria , double peso , double costoEnvio ){

         super(id, nombre, precio, categoria);
         this.peso = peso ;
         this.costoEnvio = costoEnvio ;
         
    }

    @Override
    public double calcularPrecioFinal(){
         return precio + 1.21 + costoEnvio ; 
    }

    @Override
    public void  obtenerDescripcion(){
         System.out.println(" el id " + id + " el nombre " + nombre + " el precio es  " + precio + "la categoria es " + categoria + " el peso es " + peso + " el coste de envio es  " + costoEnvio);

    }



}
