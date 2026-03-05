package Sistemadegestiondealquiler;

public class Mato extends Vehiculo  {

    public Mato (String nombre , String matricula , double tarifaBase ){
        super(nombre , matricula , tarifaBase );
    }

    @Override

    public double calcularAlquiler( int dias){

        if(dias == 1 || dias == 2 ){

            double calcular_porciento = (super.calcularAlquiler(dias)) * 5 / 100 ; 

            return super.calcularAlquiler(dias) - calcular_porciento ;
        }


        return super.calcularAlquiler(dias);
    }
    
}
