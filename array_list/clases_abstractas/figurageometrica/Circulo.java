package figurageometrica;

public class Circulo extends Poligono {
    private double radio;

    public Circulo(String color, double radio) {
        super(color);
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;  // Mejor que Math.pow (más legible)
    }

    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }
}
