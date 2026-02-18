public class Estudiante extends Persona {
    private String curso;

    public Estudiante(String nombre, String apellido, String DNI, String estado_civil, String curso) {
        super(nombre, apellido, DNI, estado_civil);
        this.curso = curso;
    }

    public String getCurso() { return curso; }

    @Override
    public String toString() {
        return super.toString() + " | Curso: " + curso;
    }
}