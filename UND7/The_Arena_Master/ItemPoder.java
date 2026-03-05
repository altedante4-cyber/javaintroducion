package The_Arena_Master;

public class ItemPoder extends Entidad {

    private int bonoVida ;

    public ItemPoder(String nombre , int fila , int columna , int bonovida , int vida , int magia  ){

        super(nombre , fila , columna , vida , magia );
        this.bonoVida  = bonovida ; 
    }


    public String getSimbolo(){

        return "[P]";
    }
}
