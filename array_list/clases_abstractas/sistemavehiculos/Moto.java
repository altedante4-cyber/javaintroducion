package sistemavehiculos;

public class Moto extends Vehiculo {
    private int cilindrada;

    public Moto(String marca, String modelo, double velocidadMaxima, int cilindrada) {
        super(marca, modelo, velocidadMaxima);
        this.cilindrada = cilindrada;
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
