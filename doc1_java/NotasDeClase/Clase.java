package NotasDeClase;

import java.util.ArrayList;

public class Clase {

    private ArrayList<Alumno> alumnos = new ArrayList<>();
    
    // metdo para anadir alumno 

    public void agregarAlumno(Alumno a ){
        alumnos.add(a);
    }

    public void mostrarResultados(){
        int aprobados = 0 ;
        int suspensos = 0 ; 

        System.out.println("===RESULTADO DE LA CLASE === ");

        for(int i = 0 ; i< alumnos.size() ; i++ ){
             
                // if (alumnos.get(i) instanceof AlumnoPresencial ){
                //      AlumnoPresencial ap = (AlumnoPresencial) alumnos.get(i);
                //      System.out.println(ap.toString());
                // }else if (alumnos.get(i) instanceof AlumnoOnline){
                //     AlumnoOnline ao = (AlumnoOnline) alumnos.get(i);
                //     System.out.println(ao.toString());
                // }else{
                //     System.out.println("NO ENCONTRADO");
                // }  // ESTO NO HACE FALTA JAVA YA SABE EL TIPO
                Alumno a = alumnos.get(i);

                // magia no importa el tipo java usa el tostring y el estaaprbado

                System.out.println(a.toString());

                if(a.estaAprobado()){
                    aprobados ++;
                }else{
                    suspensos ++;
                }
        }

        System.out.println("\n RESUMEN");
        System.out.println("Aprobados " + aprobados);
        System.out.println("Suspenso " + suspensos );
    }
    
}
