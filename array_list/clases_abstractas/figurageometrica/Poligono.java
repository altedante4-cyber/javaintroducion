package figurageometrica;

// Cambiado: package en minúsculas (convención Java)
// Error original: package en mayúsculas (confunde, parece constante)
public abstract class Poligono {
    
    protected String color;

    public Poligono(String color) {
        this.color = color;
    }

    public abstract double calcularArea();
    public abstract double calcularPerimetro();

    public void mostrarInfo() {
        // Cambiado: formateo más limpio
        System.out.println("Color: " + color + 
                           ", Area: " + calcularArea() + 
                           ", Perimetro: " + calcularPerimetro());
    }
}
