package sistemadegestiondeunatiendaonline;

public abstract class Producto {
    protected int id,
    protected String nombre ;
    protected  double precio ;
    protected String categoria ;


    public Producto(int id , String nombre  , double precio , String categoria ){
          
         this.id = id ;
         this.nombre = nombre ;
         this.precio = precio ;
         this.categoria = categoria;
         
    }

    public abstract double calcularPrecioFinal();
    public abstract String obtenerDescripcion();

    public int getid(){return id; }
    public String getnombre(){return nombre ;}
    public double getPrecio(){return precio ;}
    public String getCategoria(){return categoria ;}


    public String toString(){
         return  "el id " + id  + " el nombre "  + nombre +"el precio " + precio + "la categoria  " + categoria ; 
    }

    


}
