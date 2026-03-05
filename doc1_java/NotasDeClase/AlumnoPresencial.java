package NotasDeClase;

public class AlumnoPresencial extends Alumno {
    
    private int asistencia ; 
    public AlumnoPresencial(String nombre , int nota , int asistencia ){
        super(nombre, nota);
        validarasistencia(asistencia);
    }

    public void validarasistencia(int asistencia ){

        if(asistencia < 0 || asistencia > 100 ){
             this.asistencia = 0 ; 
        }

        this.asistencia = asistencia ;
    }

    @Override

    public boolean estaAprobado(){
        return super.estaAprobado() &&  asistencia >= 75 ; 
    }

    public String toString(){

        return "El alumnopresencial llamado " + super.toString() ; 
    }
}
