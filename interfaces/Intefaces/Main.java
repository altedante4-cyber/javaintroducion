package Intefaces;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args){

          ArrayList<Comunicador> comunicadores =  new ArrayList<>();
         
          comunicadores.add(new Paloma(true, "aaa", "rojo", "hembra"));
         comunicadores.add(new Paloma(false, "palomo ", "amarillo", "macho"));

         comunicadores.get(0).enviarMensaje("123", "hola");
         comunicadores.get(0).enviarMensaje("345", "como");

         
        
         







    }
    
}
