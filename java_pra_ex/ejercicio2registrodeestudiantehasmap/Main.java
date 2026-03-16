package ejercicio2registrodeestudiantehasmap;

public class Main {
    public static void main(String[] args) {
        Universidad u = new Universidad();
        
        Estudiante e1 = new Estudiante("2023001", "Juan Perez", "Ingenieria", 85.5);
        Estudiante e2 = new Estudiante("2023002", "Maria Lopez", "Medicina", 90.0);
        Estudiante e3 = new Estudiante("2023003", "Carlos Garcia", "Ingenieria", 78.3);
        
        System.out.println("--- Registrar estudiantes ---");
        System.out.println("Registrar e1: " + u.registrarEstudiante(e1));
        System.out.println("Registrar e2: " + u.registrarEstudiante(e2));
        System.out.println("Registrar e3: " + u.registrarEstudiante(e3));
        
        System.out.println("\n--- Intentar registrar estudiante duplicado ---");
        System.out.println("Registrar e1 de nuevo: " + u.registrarEstudiante(e1));
        
        System.out.println("\n--- Buscar estudiante ---");
        Estudiante encontrado = u.BuscarEstudiante("2023002");
        System.out.println("Estudiante con matricula 2023002: " + (encontrado != null ? encontrado.toString() : "No encontrado"));
        
        Estudiante noEncontrado = u.BuscarEstudiante("9999999");
        System.out.println("Estudiante con matricula 9999999: " + (noEncontrado != null ? noEncontrado.toString() : "No encontrado"));
        
        System.out.println("\n--- Actualizar promedio ---");
        System.out.println("Promedio actual de e1: " + e1.getClass());
        u.actualizarPromedioEstudiante(e1, 88.0);
        System.out.println("Nuevo promedio de e1 actualizado");
        
        System.out.println("\n--- Mostrar estudiantes de Ingenieria ---");
        u.mostrarEstudiantesDeUnacarreraEspecifica("Ingenieria");
        
        System.out.println("\n--- Mostrar estudiantes de Medicina ---");
        u.mostrarEstudiantesDeUnacarreraEspecifica("Medicina");
        
        System.out.println("\n--- Mostrar estudiantes de Derecho (no hay) ---");
        u.mostrarEstudiantesDeUnacarreraEspecifica("Derecho");
    }
}
