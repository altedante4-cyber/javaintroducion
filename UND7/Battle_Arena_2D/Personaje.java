package Battle_Arena_2D;

public class Personaje {

    private String nombre ;
    private int vida ; 
    private int  magia ; 
    


    public Personaje(String nombre , int vida , int  magia ){

        this.nombre = nombre ;
        this.vida = vida ; 
        this.magia = magia ; 
    }


    public int getmagia(){
        return  magia ; 
    }

    public void setmagia(){

         magia -= 5 ; 
    }

    public int atacar(){

        return  10 ; 
    }

    public int getatacar(){
        return 10 ; 
    }

    public String getnombre(){
        return nombre; 
    }


    public String toString(){

        return "Nombre " + nombre + " vida  " + vida + " magia " + magia  + " atacar   " + atacar() ;
    }


    
}
