package Sistemaderegistrodedispositivos;

public class Dispositivo {


    private String nombre , idSerie ;
    private boolean encendido ;


    public Dispositivo(String nombre , String idSerie ){
         this.nombre = nombre ;
         this.idSerie = idSerie;
         this.encendido= false ;
    }

    public void realizarAccion(){
         System.out.println("el dispositivo realiza un proceso estandar ");
    }

    public String getNombre(){
        return nombre ;

    }

    public String toString(){

        return "el nombre " + nombre + " el idseria " + idSerie + " esta " + encendido ;
    }

    
}
