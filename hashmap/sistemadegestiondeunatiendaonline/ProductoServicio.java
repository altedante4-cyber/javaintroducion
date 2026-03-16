package sistemadegestiondeunatiendaonline;

public class ProductoServicio  extends Producto {
        private  int duracionDias ; 
    public ProductoServicio(int id , String nombre  , double precio , String categoria  , int duracionDias ){

         super(id, nombre, precio, categoria);
         this.duracionDias = duracionDias;
    }

    @Override
    public double calcularPrecioFinal(){

         double aplicar_iva = precio + 1.21 ; 
         return aplicar_iva - 0.05 ; 
    }
    @Override
    public void  obtenerDescripcion(){
         System.out.println(" el id " + id + " el nombre " + nombre + " el precio es  " + precio + "la categoria es " + categoria + "la duracion " + duracionDias );

    }


    
}
