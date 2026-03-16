package ejercicio2registrodeestudiantehasmap;

public class Estudiante{

     private String num_matricula;
     private String nombre;
     private String carrera;
     private double promedio ;

     public Estudiante(String num_matricula , String nombre , String carrera , double promedio ){
         this.num_matricula= num_matricula;
         this.nombre = nombre;
         this.carrera = carrera;
         this.promedio = promedio ;
     }

    public String getMatricula(){
         return num_matricula;
    }
    public String getCarrera(){
         return carrera ; 
    }
    public void setPromedio(double nuevo_promedio){
         this.promedio = nuevo_promedio;
    }
     
     public String toString(){
         return "Num_matricula | " + num_matricula + " Nombre | "+nombre + " Carrera "+ carrera + " Promedio | " + promedio ;
     }

}