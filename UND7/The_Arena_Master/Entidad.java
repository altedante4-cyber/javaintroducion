package The_Arena_Master;

public class Entidad {
    
    private String nombre ;
    private int fila ;
    private int columna ; 
    private int vida ; 
    private int magia ; 

    public Entidad(String nombre , int fila , int columna , int vida , int magia  ){

        this.nombre = nombre ;
        this.fila = fila;
        this.columna = columna ; 
        this.vida = vida;
        this.magia = magia ; 

    }

    public int getVida(){
        return vida ; 
    }

    public int getmagia(){

        return magia ; 
    }
    public int getcolumna(){
        return  columna ; 
    }

    public int getfila(){
        return fila ; 
    }

    public String getSimbolo(){

        return "E";
    }
    public int atacar(){

        return 10 ; 
    }
    public int getatacar(){

        return 10 ; 
    }
    public String getNombre(){
        return nombre ; 
    }

    public void setfila(int fila ){

        this.fila = fila ; 
    }

    public void setcolumna(int columna){

        this.columna = columna ; 
    }


  public String toString(){

    return "INFO: " + getNombre() + "| Vida: " +  vida + " |  Pos:  [ "+fila+","+columna+"]";  
  }
}
