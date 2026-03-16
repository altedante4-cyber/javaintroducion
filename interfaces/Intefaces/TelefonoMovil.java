package Intefaces;

public class TelefonoMovil extends  Telefono implements Comunicador {
    private int numero_telefono ; 
    public TelefonoMovil(int numero , String marca , int numero_telefono ){
         super(numero,marca);
        this.numero_telefono = numero_telefono;
    }

    @Override
    public void enviarMensaje(String destino , String mensaje ){
         System.out.println("se ha enviado el mensaje  " + mensaje + "desde  " + destino );
    }
    
}
