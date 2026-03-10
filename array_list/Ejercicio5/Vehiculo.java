public class Vehiculo {
    protected String marca;
    protected String modelo;
    protected int año;
    protected double precio;
    
    public Vehiculo(String marca, String modelo, int año, double precio) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precio = precio;
    }
    
    // Método que será sobrescrito por las clases derivadas
    public void mostrarInfo() {
        System.out.println("Marca: " + marca + ", Modelo: " + modelo + 
                         ", Año: " + año + ", Precio: $" + precio);
    }
    
    public double calcularImpuesto() {
        return precio * 0.10; // 10% de impuesto
    }
    
    public String getMarca() {
        return marca;
    }
    
    public String getModelo() {
        return modelo;
    }
    
    public int getAño() {
        return año;
    }
    
    public double getPrecio() {
        return precio;
    }
    
    public void setPrecio(double precio) {
        this.precio = precio;
    }
}
