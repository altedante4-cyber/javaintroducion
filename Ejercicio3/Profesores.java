public class Profesores extends Empleado {
    private String departamento;

    public Profesores(String nombre, String apellido, String DNI, String estado_civil, int ano, int despacho, String departamento) {
        // Llama al constructor de Empleado con todos sus datos
        super(nombre, apellido, DNI, estado_civil, ano, despacho);
        this.departamento = departamento;
    }

    @Override
    public String toString() {
        return super.toString() + " | Departamento: " + departamento;
    }
}