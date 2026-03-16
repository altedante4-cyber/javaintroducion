package sistemadegestiondeunatiendaonline;

public class ProductoDigital extends Producto  {

     private double tamanoMB;

     public ProductoDigital(int id , String nombre , double precio , String categoria , double tamanoMB ){

           super(id, nombre, precio, categoria);
           this.tamanoMB = tamanoMB ; 
     }


     @Override
     public double calcularPrecioFinal(){
            return precio + 1.21 ; 
     }

     @Override
     public void obtenerDescripcion(){
         System.out.println(" el id " + id + " el nombre " + nombre + " el precio es  " + precio + "la categoria es " + categoria  + " el tamanoMG " + tamanoMB);

     }

}
