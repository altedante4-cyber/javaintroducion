package FigurasGeometricas;

public class Rectangulo extends Figura{

    private double base , altura , ladoA, ladoB , ladoC ;


    public Rectangulo(double base , double altura ){
        this.base = base;
        this.altura =altura ;
    }
    @Override

    public double calcularArea(){

        // el ara de un rectangulo es A=b* h 
        // el perimetro es p=2*(b+h)

        return base * altura ; 
    }

    @Override
    public double calcularPerimetro(){

        return 2 *(base + altura );

    }

    public String toString(){

        return "El rectangulo tiene un area de " + calcularArea() + " y un perimetro de " + calcularPerimetro();
    }
    
}
