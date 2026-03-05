package The_Arena_Master;

public class Mago extends Entidad {


      public Mago(String nombre , int fila  , int columna , int vida , int magia  ){

        super(nombre, fila,columna , vida , magia );

    }


    @Override

    public int atacar(){

            return getatacar() * 3 ; 
    }



    // to string para saber si es un mago 


    public String toString(){

        return "INFO: " + getNombre() + "Mago" + "| Vida: " +  getVida() + " |  Pos:  [ "+getfila()+","+getcolumna()+"]";
    }
    
}
