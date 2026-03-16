package ejercicio4interfases;
public class Español extends Persona implements Hablador{

    public Español(String nombre , String apellidos){
        super(nombre, apellidos);
    }

    @Override
    public void saludar(){
        System.out.println("Esto es una persona español");
    }

    

    
    
}
