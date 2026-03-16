public abstract class Producto {
    private int id;
    private String nombre;
    private double precio;
    private String categoria;

    public Producto(int id, String nombre, double precio, String categoria) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public String getCategoria() {
        return categoria;
    }

    public abstract double calcularPrecioFinal();

    public abstract String obtenerDescripcion();

    @Override
    public String toString() {
        return "Producto{id=" + id + ", nombre='" + nombre + "', precio=" + precio + 
               ", categoria='" + categoria + "'}";
    }
}
