package Intefaces;

public class Paloma extends Ave implements Comunicador  {
    private String color , sexo  ;
    public Paloma(boolean vuela , String especie , String color , String sexo   ){
        super(vuela,especie); 
        this.color = color ;
         this.sexo = sexo ;
    }
@Override
    public void enviarMensaje(String destino , String mensaje ){
         System.out.println("se ha enviado el mensaje  " + mensaje + "desde  " + destino );
    }

}
