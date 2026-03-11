package sistemavehiculos;

public class Coche extends Vehiculo {
    private int numPuertas;

    public Coche(String marca, String modelo, double velocidadMaxima, int numPuertas) {
        super(marca, modelo, velocidadMaxima);
        this.numPuertas = numPuertas;
    }

    @Override
    public void acelerar(int kmh) {
        if (velocidadActual + kmh <= velocidadMaxima) {
            velocidadActual += kmh;
        } else {
            velocidadActual = velocidadMaxima;
        }
    }

    @Override
    public void frenar(int kmh) {
        if (velocidadActual - kmh >= 0) {
            velocidadActual -= kmh;
        } else {
            velocidadActual = 0;
        }
    }
}
