package Alumnos_notas;

public class PruebaAlumno {
    public static void main(String[] args ){

         Alumno michael = new Alumno("micha");

         michael.addNota(new Nota("mates", 10));
         michael.addNota(new Nota("programacion", 8));
         michael.addNota(new Nota("entornos ", 5));
         michael.addNota(new Nota("BBDD", 5));

         System.out.println(michael);
         System.out.println("Media " + michael.calcularMedia());
         System.out.println("Aprobado " + michael.estaAprobado());

         
         
    }
    
}
