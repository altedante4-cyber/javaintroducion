package Sistemaderegistrodedispositivos;

public class Router extends Dispositivo  {

    private double frecuenciaWifi;

    public Router(String nombre , String idSerie , String SistemaOperativo ,double frecuenciaWifi ){
         super(nombre,idSerie);
        this.frecuenciaWifi = frecuenciaWifi;
    }


    @Override

    public void realizarAccion(){
         System.out.println("Router " + getNombre() + " transmitiendo señal a " + frecuenciaWifi );
    }
}
