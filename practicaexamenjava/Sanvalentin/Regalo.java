package Sanvalentin;

public class Regalo {

    private String nombre , descripcion;
    private double precio ;


    public Regalo(String nombre , String descripcion , double precio ) {
        this.nombre = nombre ;
        this.descripcion  = descripcion ;
        this.precio = precio ; 
    }



    public String getNombre(){
        return nombre ; 
    }
    public String getDescripcion(){
        return descripcion ;
    }
    public double getPrecio(){
        return precio ; 
    }

    public void setNombre(String nombre ){
        this.nombre = nombre ; 
    }

    public void setDescripcion(String descripcion ){
        this.descripcion = descripcion ; 
    }

    public void setPrecio(double precio  ){
        this.precio = precio ; 
    }


    public String toString(){
        return "Nombre " + nombre + "descripcion " + descripcion + " precio = " + precio ; 
    }
    
}
