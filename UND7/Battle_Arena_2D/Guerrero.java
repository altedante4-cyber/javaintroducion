package Battle_Arena_2D;

public class Guerrero extends Personaje {
    
    private int fuerzaExtra ; 

    public Guerrero (String nombre , int vida  , int  magia , int fuerzaExtra ){

        super(nombre,vida,magia);

        this.fuerzaExtra = fuerzaExtra ;
    }


    @Override

    public int atacar(){

        return getatacar() + fuerzaExtra ;
    
    }


    // un metdo lanzar un grito

    public void lanzarGrito(){

        System.out.println("YEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA PUTTOOOOOOOOOOOOOOOOOO");
    }


    public String toString(){

        return  super.toString() + " fuerza " + fuerzaExtra ; 
    }


}
