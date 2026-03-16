package ejercicio4interfases;

public abstract class Persona {

    private String nombre ;
    private String apellidos;

    public Persona(String nombre, String apellidos ){
        this.nombre = nombre;
        this.apellidos = apellidos;
    }

     public abstract String modificarNombre(String nombre);
     public abstract String modificarApellidos(String apellidos);
    
    
    
}
