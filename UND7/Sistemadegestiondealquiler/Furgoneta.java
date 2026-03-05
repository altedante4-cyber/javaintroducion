package Sistemadegestiondealquiler;

public class Furgoneta extends Vehiculo {


    public Furgoneta(String matricula  , String modelo   , double tarifaBase ){

        super(matricula, modelo , tarifaBase);
    }


    @Override

    public double calcularAlquiler(int dias ){

        if ( dias >= 7 ){
            // calcular el 15% del total de alquiler
            // 10 - 100
            // x  - 15  
            //sacamo primerio el 15%
            double sacar_porciento = (super.calcularAlquiler(dias) * 15) / 100 ;
            return super.calcularAlquiler(dias) + sacar_porciento ;  
        }

        return super.calcularAlquiler(dias)
        
    }


    
    
}
