package sistemavehiculos;

public abstract class Vehiculo {
    
    protected String marca;
    protected String modelo;
    protected double velocidadMaxima;
    protected double velocidadActual;  // NUEVO: tracking de velocidad

    public Vehiculo(String marca, String modelo, double velocidadMaxima) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidadMaxima = velocidadMaxima;
        this.velocidadActual = 0;  // Inicia detenido
    }

    public abstract void acelerar(int kmh);
    public abstract void frenar(int kmh);

    public void mostrarInfo() {
        System.out.println("Marca: " + marca + 
                           ", Modelo: " + modelo + 
                           ", Velocidad maxima: " + velocidadMaxima +
                           ", Velocidad actual: " + velocidadActual);
    }
}
