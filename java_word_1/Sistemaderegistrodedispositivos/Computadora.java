package Sistemaderegistrodedispositivos;

public class Computadora extends Dispositivo {

    private String sistemaOperaivo;

    public Computadora(String nombre , String idSerie , String SistemaOperativo ){
         super(nombre,idSerie);
         this.sistemaOperaivo = SistemaOperativo ;
    }
    

    @Override
    public void realizarAccion(){
         System.out.println("Computador " + getNombre() + " ejecutando scripto en sistema operativo " + sistemaOperaivo );
    }

    public String toString(){

        return  super.toString() + " el sistema operativo que utiliza es  " + sistemaOperaivo ;
    }



    
}
