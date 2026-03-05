package The_Arena_Master;

public class Guerrero extends Entidad {


    private  int fuerzaExtra ; 
    public Guerrero(String nombre , int fila , int columna , int fuerzaExtra , int vida , int magia ){
        super(nombre,fila,columna , vida , magia  );
        this.fuerzaExtra = fuerzaExtra ;
    }



    
      @Override

    public int atacar(){

        return getatacar() + fuerzaExtra ;
    
    }

    public void moverse(int nuevaF , int nuevaC){

        setfila(nuevaF);
        setcolumna(nuevaC); 
    }



    public String toString(){
        return "INFO: " + getNombre() + "Guerrero " + "| Vida: " +  getVida() + " |  Pos:  [ "+getfila()+","+getcolumna()+"]";


    }

}
