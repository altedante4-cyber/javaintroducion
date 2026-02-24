package Mini;
import java.util.Random;

import javax.print.DocFlavor.READER;

public class Producto {
    
    private int id  ;
    private String nombre , categoria   ; 
    private double precio ; 


    public Producto (int id , String nombre, String categoria , double precio ){
        this.id = id ;  
        this.nombre  = nombre ; 
        this.categoria = categoria ;
        this.precio = precio ; 
    }

    public Producto(String nombre , double precio ){
        this.nombre = nombre;
        this.precio = precio ;
        this.id = getGenerarid();
        setPrecio(precio);
        this.categoria = "General";
    }


    public void setPrecio(double precio ){

        if(precio < 0  ){
            this.precio  = 0 ; 
        }

        this.precio = precio ; 
    }

    public int  getGenerarid(){
        Random rand = new Random();

        int ale = rand.nextInt(100) + 0 ; 

        return ale ; 
    }

    public int getid(){
        return id ; 
    }
    public String getNombre(){
        return nombre ; 
    }

    public double getprecio(){
        return precio ; 
    }
    

    public String toString(){

        return  " id => " + id + " nombre " + nombre + " la categoria " + categoria + " precio  " + precio ;  
    }


}


