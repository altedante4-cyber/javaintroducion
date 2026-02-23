package Alumnos_notas;

public class Nota {

    private String asignatura ;
    private double nota ; 


    public Nota(String asignatura , double nota ){
         this.asignatura = asignatura ;
         this.nota = nota ;
    }



    public double dameNota(){
        return  nota ; 
    }
    
}
