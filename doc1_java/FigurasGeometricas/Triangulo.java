package FigurasGeometricas;

public class Triangulo extends Figura {

    private double base , altura , ladoA , ladoB,ladoC ; 


    public Triangulo(double base , double altura , double ladoA , double ladoB , double ladoC ){
        this.base = base ;
        this.altura = altura;
        this.ladoA = ladoA;
        this.ladoB = ladoB;
        this.ladoC = ladoC;

    }
    @Override

    public double calcularArea(){
           
        return (base * altura) / 2 ; 
        
    }

    @Override
    public double calcularPerimetro(){

        return ladoA + ladoB + ladoC;
      

    }

     public String toString(){

        return "El triangulo tiene un area de " + calcularArea() + " y un perimetro de " + calcularPerimetro();
    }
    
}
