package Sanvalentin;

public class GestorSanValentin {

    public static void main(String[] args){

        Persona p1 = new Persona("1234", "michael");
        Persona p2 = new Persona("12345", "valeria");

        Pareja pareja1 = new Pareja(p1, p2);

        Regalo p1r = new Regalo("zapato nike ", "rojos ", 290);
        Regalo p2r = new Regalo("zapato banlan ", "blancos ", 300);
        
        pareja1.setRegaloPersona1(p1r);
        pareja1.setRegaloPersona2(p2r);

      pareja1.mostrarDetalles();        
    }
    
}
