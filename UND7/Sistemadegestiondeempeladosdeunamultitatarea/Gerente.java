package Sistemadegestiondeempeladosdeunamultitatarea;

public class Gerente  extends Empleado {

    private int personasACargo ;


    public Gerente(String nombre , int id , double salarioBase , int personasACargo ){

         super(nombre , id , salarioBase );
         this.personasACargo = personasACargo;
    }

    @Override

    public double calcularBono(){
         
         double calcular = super.calcularBono() + (super.calcularBono() * 0.15 );

         for (int i = 0  ; i < personasACargo ; i++ ){

                 calcular += 100 ; 
         }

         return calcular ; 
    }



    public String toString(){
 
        return  "El gerente " + super.toString() + " tiene un salario de " + calcularBono() + " Se le da un plus por cuidar a  " + personasACargo + " Personas "; 
    }
    
}
