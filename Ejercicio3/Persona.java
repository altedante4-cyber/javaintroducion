public class Persona {
    private String nombre, apellido, DNI, estado_civil;

    public Persona(String nombre, String apellido, String DNI, String estado_civil) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.DNI = DNI;
        this.estado_civil = estado_civil;
    }

    // Getters y Setters...
    @Override
    public String toString() {
        return "Nombre: " + nombre + " " + apellido + " | DNI: " + DNI + " | Estado Civil: " + estado_civil;
    }
}