public class Empleado extends Persona {
    private int ano_incorporacion, numero_despacho;

    public Empleado(String nombre, String apellido, String DNI, String estado_civil, int ano_incorporacion, int numero_despacho) {
        super(nombre, apellido, DNI, estado_civil);
        this.ano_incorporacion = ano_incorporacion;
        this.numero_despacho = numero_despacho;
    }

    @Override
    public String toString() {
        return super.toString() + " | Incorporación: " + ano_incorporacion + " | Despacho: " + numero_despacho;
    }
}