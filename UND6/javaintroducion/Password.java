package javaintroducion;
import java.util.Random;

public class Password {

    private int longitud;
    private String contrasena;

    // Constructor por defecto
    public Password() {
        this.longitud = 8;
        // Inicializamos para que no sea null
        this.contrasena = ""; 
        generarPassword();       
    }

    // Constructor con longitud
    public Password(int longitud) {
        this.longitud = longitud;
        this.contrasena = ""; 
        generarPassword();
    }

    public int devolverlongitud() {
        return this.longitud; 
    }

    public void generarPassword() {
        Random lete = new Random();
        String palabras_numeros = "0123456789qqwrtyuioppasdfghjklzxcvbnm";
        
        // Reiniciamos la contraseña por si ya tenía algo
        this.contrasena = ""; 
        
        for (int i = 0; i < this.longitud; i++) {
            // Sacamos un índice aleatorio
            int indice = lete.nextInt(palabras_numeros.length());
            
                this.contrasena += palabras_numeros.charAt(indice);

        }
    }

    public String toString() {
        return "La longitud es " + longitud + " y la contraseña es: " + contrasena; 
    }
}