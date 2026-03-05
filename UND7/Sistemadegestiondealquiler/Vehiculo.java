package Sistemadegestiondealquiler;

public class Vehiculo {

    private String matricula , modelo ;
    private double tarifaBase ; 



    public Vehiculo(String matricula , String modelo , double tarifaBase ){

        this.matricula = matricula;
        this.modelo = modelo;
        this.tarifaBase = tarifaBase ; 
    }

    public double calcularAlquiler(int dias ){
        return tarifaBase * dias ; 
    }

    public double getTarifaBase(){

        return tarifaBase ;
    }

    public String getMatricula(){
        return matricula ;
    }

    public String getmodelo(){
        return modelo;
    }

    public String toString(){
        return  "Matricula " + matricula  + " | MODELO " + modelo + " | TARIFA BASE "+ tarifaBase ;
    }

    
}
