package NotasDeClase;

public class Alumno {

    private String nombre ;
    private double nota ; 


    public Alumno(String nombre , double nota ){
        this.nombre = nombre ;
        this.nota =  nota ; 
    }

    public boolean estaAprobado(){
        return nota >= 5 ;
    }


    public String toString(){
        String aprobado = "";
        if(estaAprobado()){
            aprobado += "Aprobado";
        }else{
            aprobado += "Suspenso";
        }
        return "El nombre " + nombre + " la nota " + nota + "usted esta " +  aprobado ; 
    }
    
}
