package sistemadegestiondeunatiendaonline;

public class ItemCarrito {

    private Producto producto ;
    private int cantidad ; 

    public ItemCarrito(Producto p , int cantidad ){
            this.producto = p ;
            this.cantidad = cantidad ; 
    }

    public double calcularSubtotal(){

         double sub = producto.calcularPrecioFinal() * cantidad ;

         return sub ; 
    }



    public int getCantidadProducto(){

        return cantidad ; 
    }

    public String toString(){

        return producto.toString() + cantidad ; 
    }
    
}
