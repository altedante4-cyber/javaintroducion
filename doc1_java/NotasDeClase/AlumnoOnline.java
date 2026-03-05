package NotasDeClase;

public class AlumnoOnline extends Alumno  {
    
    private int entregasRealisadas ;

    public AlumnoOnline(String nombre , int nota , int entregasRealisadas){
        super(nombre, nota);
        this.entregasRealisadas = entregasRealisadas;
    }

    @Override

    public boolean estaAprobado(){
        return super.estaAprobado() &&  entregasRealisadas >= 8 ; 
    }


    public String toString(){
        return "El alumno online " + super.toString() ; 
    }

}
