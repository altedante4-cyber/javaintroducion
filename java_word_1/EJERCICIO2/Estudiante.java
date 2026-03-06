package EJERCICIO2;

public class Estudiante {

    private String nombre ;
    private String matricula ;
    private String carrera ;
    private double promedio ;



    public Estudiante(String nombre , String matricula , String carrera , double promedio ){
         this.nombre = nombre ;
         this.carrera = carrera ;
         this.matricula = matricula;
         this.promedio = promedio ;
    }
    public Estudiante(String nombre , String matricula  ){
         this.nombre = nombre ;
         this.matricula = matricula;
    }

    public boolean actualizarPromedio(double nuevoPromedio){
        if(nuevoPromedio < 0 ){return false ;}
        this.promedio = nuevoPromedio; return true ; 
    }
    public void cambiarCarrera(String nuevaCarrera){
            this.carrera = nuevaCarrera ; 
    }

    public String toString(){
        return "Nombre " + nombre + "MATRICULA " + matricula + " la carrerara " + carrera + " el promedia " + promedio ;  
    }



}
