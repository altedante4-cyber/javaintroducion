package Sistemadegestiondealquiler;

import otros.Coche;

public class Cochae extends Vehiculo {

    public Cochae(String matricula , String modelo  , double tarifaBase ){

        super(matricula, modelo , tarifaBase);
    }


    @Override

    public double calcularAlquiler(int dias ){
         
        return  super.calcularAlquiler(dias) + 10 ; 
    }


    
}
