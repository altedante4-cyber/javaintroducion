package NotasDeClase;

public class mainAlumnos {

    public static void main(String[] args ){

        AlumnoPresencial alumnos_presenciales = new AlumnoPresencial("mika", 4, 10);
        AlumnoPresencial alumnos_presenciale1 = new AlumnoPresencial("victor", 6, 75);
        AlumnoPresencial alumnos_presenciale2 = new AlumnoPresencial("angel", 7, 13);

        AlumnoOnline alumnos_online1 = new AlumnoOnline("peredo ", 5, 10);
        AlumnoOnline alumnos_online2 = new AlumnoOnline("aguilar", 4, 14);
        AlumnoOnline alumnos_online3 = new AlumnoOnline("perez ", 10, 10);
        

        Clase cl = new Clase();

        cl.agregarAlumno(alumnos_online1);
        cl.agregarAlumno(alumnos_presenciale1);
        cl.mostrarResultados();
    }
    
}
