package javaintroducion;

public class Producto {
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    // Getters y Setters
    public void setNombre(String nombre) { this.nombre = nombre; }
    public void setPrecio(double precio) { this.precio = precio; }
    public void setStock(int stock) { this.stock = stock; }

    public String getNombre() {
        return this.nombre;
    }

    @Override
    public String toString() {
        return "Producto: " + nombre + " | Precio: " + precio + "€ | Stock: " + stock;
    }
}