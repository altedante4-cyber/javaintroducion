package Sistemademaquinaexpendedora;

public class Producto {

    private String nombre ;
    private double precio ; 
    private int cantidadStock ; 


    public Producto(String nombre , double precio , int cantidadStock ){

        this.nombre = nombre ;
        this.precio = precio ;
        this.cantidadStock = cantidadStock ; 
    }


    public boolean vender(){

        if(cantidadStock > 0 ){
            cantidadStock  -= 1 ;
            return true ; 
        }

        return false ; 
    }

    // metodo geter para saber el precio del producto

    public double getPrecio(){
        return precio ; 
    }

    public int getcatidadstock(){
        return cantidadStock ; 
    }


    public void agregarPrecio(double precio ){


        if (this.precio > 0 ){
             this.precio += precio ; 

        }
        this.precio = 0 ; 
    }

    public void quitarCatidadstock(){

        if ( this.cantidadStock  > 0 ){

              this.cantidadStock  -= 1; 
        }


    }

    public String toString(){

        return "Nombre " + nombre + " |  precio " + precio  + " |  stock : " + cantidadStock;
    }



    
}
