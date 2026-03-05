package FigurasGeometricas;

public class Circulo extends Figura {
    
    private double radio ;

    public Circulo(double radio ){
        this.radio = radio ;
    }

    @Override

    public double calcularArea(){

        return  Math.PI * radio * radio ;
    }

    @Override

    public double calcularPerimetro(){

        return  2 * Math.PI * radio ; 
    }

    public String toString(){

        return "El circulo tienene un area de  " + calcularArea() + " y un perimetro de " + calcularPerimetro();
    }
}
